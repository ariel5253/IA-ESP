# Ideas de Proyecto — Tarea 1  
Optimización aplicada a IA (Unidad 1)

> Cada sección incluye **contexto**, **objetivo**, **variables**, **restricciones**, **tipo de problema** y **método sugerido**.  

---

## 1. Detección temprana de uso inadecuado de IA por estudiantes

**Contexto**  
Analizar patrones de entrega (hora, similitud de texto, cambios de estilo) para identificar plagio asistido por IA.

**Objetivo**  
Reducir falsos negativos (casos no detectados) sin aumentar demasiado las horas de revisión manual.

**Variables de decisión**  
- `umbral_similitud`  
- `peso_tiempo`  
- `peso_estilo`

**Restricciones**  
- Horas de revisión ≤ 2 h por profesor a la semana.  
- Tasa de falsos positivos ≤ 10 %.

**Tipo de problema**  
Determinista · Lineal · Con restricciones · Variables continuas.

**Método sugerido**  
Programación lineal (Simplex) — maximizar cobertura con límites de tiempo.

---

## 2. *Vibe Coding*: asignación óptima de tareas en un sprint

**Contexto**  
Asignar bloques de concentración y tareas a desarrolladores para subir la “velocity” del equipo y bajar cambios de contexto.

**Objetivo**  
Maximizar puntos de historia completados, penalizando cada cambio de tarea dentro del día.

**Variables de decisión**  
- `x_ij` = 1 si la tarea *j* se asigna al dev *i* en su bloque; 0 en otro caso.

**Restricciones**  
- Cada tarea asignada a un solo desarrollador.  
- Horas asignadas a cada dev ≤ horas disponibles.

**Tipo de problema**  
Determinista · Entero lineal (MILP) · Con restricciones · Variables binarias.

**Método sugerido**  
Simplex + Branch-and-Bound (herramientas: PuLP u OR-Tools).

---

## 3. Frecuencia óptima de extracción de datos en sistemas POS

**Contexto**  
Elegir cada cuánto extraer datos (ventas, inventario) para dashboards sin sobrecargar la base de datos.

**Objetivo**  
Minimizar el costo computacional manteniendo la frescura de la información (latencia < 30 s).

**Variables de decisión**  
- `freq_ventas` ∈ {15 min, 30 min, 1 h}  
- `freq_inventario` ∈ {15 min, 30 min, 1 h}

**Restricciones**  
- Latencia del dashboard < 30 seg.  
- Capacidad de CPU ≤ 80 %.

**Tipo de problema**  
Determinista · No lineal discreto · Con restricciones · Variables discretas.

**Método sugerido**  
Gradiente descendente (relajando las variables a continuas) + redondeo final.

---

## Pasos siguientes

1. **Revisar datos disponibles** y la viabilidad de medir las variables.  
2. **Elegir la idea** que mejor se adapte a los conocimientos y al tiempo del grupo.  
3. Completar la **formulación detallada** (función objetivo exacta, ecuaciones de restricción).  
4. Implementar el método en Python y redactar el informe siguiendo la rúbrica (comprensión, justificación, código, análisis y presentación).
