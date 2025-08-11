# Propuesta de proyecto — Asignación óptima de tutorías para estudiantes (Corhuila)
**Unidad 1 · Optimización clásica en IA**

## 1) Contexto
Tenemos resultados de **pruebas diagnósticas** por estudiante (Lectura Crítica, Competencia Ciudadana, Razonamiento Cuantitativo, Inglés), con metadatos de **Programa** y **Semestre**. La Universidad desea **reducir estudiantes en riesgo** (bajo desempeño) asignando horas de tutoría por área, sujeto a un presupuesto de horas y a la disponibilidad de tutores.

## 2) Tipo de problema
Determinista · **Lineal** (con variables adicionales para linearizar “máximo”) · **Con restricciones** · Variables **continuas** (horas).  
> Método elegido para resolver: **Programación lineal (Simplex)**.

## 3) Formulación matemática

**Conjuntos**  
- \(P\): programas académicos  
- \(S\): semestres  
- \(A=\{\text{LC},\text{CC},\text{RQ},\text{ING}\}\): áreas (Lectura Crítica, Competencia Ciudadana, Razonamiento Cuantitativo, Inglés)

**Datos**  
- \(r_{p,s,a}\): número de estudiantes “en riesgo” en \((p,s,a)\) (p.ej., < p40 de su cohorte).  
- \(k_a>0\): **efecto por hora** en el área \(a\): reducción esperada del conteo en riesgo por cada hora de tutoría asignada.  
- \(H\): presupuesto total de horas de tutoría.  
- \(C_a\): capacidad máxima de horas que puede impartir el equipo de tutores del área \(a\).  
- \(h^{\min}_{p,s}\): horas mínimas para cada cohorte \((p,s)\) (opcional, por equidad).

**Variables de decisión**  
- \(x_{p,s,a} \ge 0\): horas de tutoría asignadas a \((p,s,a)\).  
- \(y_{p,s,a} \ge 0\): estudiantes **esperados** en riesgo **después** de la intervención (variable auxiliar).

**Objetivo (minimizar riesgo residual total)**
\[
\min \;\; \sum_{p\in P}\sum_{s\in S}\sum_{a\in A} y_{p,s,a}
\]

**Restricciones**
\[
\begin{aligned}
& y_{p,s,a} \;\ge\; r_{p,s,a} - k_a \, x_{p,s,a} && \forall p,s,a \quad\text{(lineariza } \max\{r-kx,0\}) \\
& y_{p,s,a} \;\ge\; 0,\;\; x_{p,s,a} \;\ge\; 0 && \forall p,s,a \\
& \sum_{p,s,a} x_{p,s,a} \;\le\; H && \text{(presupuesto de horas)} \\
& \sum_{p,s} x_{p,s,a} \;\le\; C_a && \forall a \in A \quad \text{(capacidad por área)} \\
& \sum_{a} x_{p,s,a} \;\ge\; h^{\min}_{p,s} && \forall p,s \quad \text{(equidad, opcional)}
\end{aligned}
\]

> **Interpretación**: con \(y \ge r-kx\) y \(y \ge 0\) logramos \(y=\max(r-kx,0)\). Minimizar \(y\) empuja \(x\) a donde el impacto \(k_a\) sea mayor y el riesgo \(r\) sea más alto.

---

## 4) Implementación en Python (Simplex con PuLP)

> Reemplaza `ruta/datos.csv` por tu archivo real. Aquí se asume la estructura:  
> `PERIODO, ESTUDIANTE, IDENTIFICACIÓN, NOMBRES, APELLIDOS, PROGRAMA ACADÉMICO, SEMESTRE, LECTURA CRÍTICA, COMPETENCIA CIUDADANA, RAZONAMIENTO CUANTITATIVO, INGLÉS`.

```python
# 1) Cargar y preparar datos
import pandas as pd
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, PULP_CBC_CMD

df = pd.read_csv("ruta/datos.csv")

# Normalizar por cohorte (programa, semestre) y marcar "riesgo" por área (p40)
areas = ["LECTURA CRÍTICA", "COMPETENCIA CIUDADANA", "RAZONAMIENTO CUANTITATIVO", "INGLÉS"]
grp = df.groupby(["PROGRAMA ACADÉMICO","SEMESTRE"])

def flag_risk(g, col, q=0.4):
    thr = g[col].quantile(q)
    return (g[col] < thr).astype(int)

for a in areas:
    df[f"RISK_{a}"] = grp[a].transform(lambda g: flag_risk(g.to_frame(), a))

# Conteos r_{p,s,a}
risk_counts = (
    df.groupby(["PROGRAMA ACADÉMICO","SEMESTRE"])
      [[f"RISK_{a}" for a in areas]]
      .sum()
      .reset_index()
)

# 2) Parámetros del modelo
H_total = 120                                  # horas totales disponibles
cap_area = {"LECTURA CRÍTICA": 40, "COMPETENCIA CIUDADANA": 30,
            "RAZONAMIENTO CUANTITATIVO": 40, "INGLÉS": 30}  # capacidad por área

# Impacto esperado por hora (ejemplo; calibra con histórico o juicio experto)
k = {"LECTURA CRÍTICA": 0.25, "COMPETENCIA CIUDADANA": 0.20,
     "RAZONAMIENTO CUANTITATIVO": 0.30, "INGLÉS": 0.15}

# Equidad mínima por cohorte (opcional)
hmin = 1.0  # 1 hora mínima por cohorte
cohortes = list(zip(risk_counts["PROGRAMA ACADÉMICO"], risk_counts["SEMESTRE"]))

# 3) Construcción del LP
model = LpProblem("Asignacion_optima_tutorias", LpMinimize)

# Variables x_{p,s,a} y y_{p,s,a}
X, Y = {}, {}
for (p,s), row in risk_counts.set_index(["PROGRAMA ACADÉMICO","SEMESTRE"]).iterrows():
    for a in areas:
        X[(p,s,a)] = LpVariable(f"x_{hash((p,s,a))}", lowBound=0)
        Y[(p,s,a)] = LpVariable(f"y_{hash(('y',p,s,a))}", lowBound=0)

# r_{p,s,a}
def r(p,s,a):
    return risk_counts.loc[
        (risk_counts["PROGRAMA ACADÉMICO"]==p) &
        (risk_counts["SEMESTRE"]==s), f"RISK_{a}"
    ].values[0]

# Objetivo
model += lpSum(Y[(p,s,a)] for (p,s,a) in X.keys())

# Restricciones de linearización y no negatividad (y ya tiene lowBound=0)
for (p,s,a) in X.keys():
    model += Y[(p,s,a)] >= r(p,s,a) - k[a] * X[(p,s,a)]

# Presupuesto total
model += lpSum(X[(p,s,a)] for (p,s,a) in X.keys()) <= H_total

# Capacidad por área
for a in areas:
    model += lpSum(X[(p,s,aa)] for (p,s,aa) in X.keys() if aa==a) <= cap_area[a]

# Equidad mínima por cohorte (opcional)
for (p,s) in cohortes:
    model += lpSum(X[(pp,ss,a)] for (pp,ss,a) in X.keys() if (pp,ss)==(p,s)) >= hmin

# 4) Resolver
status = model.solve(PULP_CBC_CMD(msg=False))
print("Estado:", LpStatus[status])

# 5) Resultados
asignacion = []
for (p,s,a), var in X.items():
    asignacion.append({"PROGRAMA": p, "SEMESTRE": s, "AREA": a,
                       "HORAS": var.value(), "RIESGO_BASE": r(p,s,a),
                       "RIESGO_POST_ESP": max(r(p,s,a) - k[a]*var.value(), 0)})
res_df = pd.DataFrame(asignacion).sort_values(["PROGRAMA","SEMESTRE","AREA"])
res_df.head(20)
