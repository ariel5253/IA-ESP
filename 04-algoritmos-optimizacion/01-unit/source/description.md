---
title: Notas De Optimización En IA – Análisis Profundo
author: Jesús Ariel González Bonilla
date: 07 Ago 2025
---

# Introducción  

Este documento amplía el resumen previo, ofreciendo **análisis profundos** y **reflexiones críticas** de los nueve cuadernos de práctica sobre optimización en inteligencia artificial. Cada sección contiene:  

* **Objetivo**  
* **Teoría esencial**  
* **Fórmulas clave**  
* **Análisis detallado**  
* **Reflexiones para la práctica**

---

## 1. Gradiente Descendente Clásico  

**Objetivo**  
Minimizar la función cuadrática \(f(x)=x^{2}\) con descenso por gradiente completo.

**Teoría esencial**  
El algoritmo aplica  
\[
x_{t+1}=x_{t}-\eta \nabla f(x_{t}), \qquad \text{donde } \nabla f(x)=2x
\]  
En funciones cuadráticas la convergencia es lineal si \(0<\eta<1/L\) con \(L=2\).

**Fórmulas clave**  

* Razón de descenso:  
  \[
  f(x_{t+1})-f(x^\star)\le (1-\eta L)\bigl(f(x_t)-f(x^\star)\bigr)
  \]
* Solución óptima cerrada: \(x^\star=0\).

**Análisis detallado**  

* Al ser una función convexa unidimensional, sirve para **visualizar la mecánica del algoritmo** y su sensibilidad a \(\eta\).  
* Se evidencia el **compromiso**: \(\eta\) muy pequeño → convergencia lenta; \(\eta\) grande → posible divergencia.  
* Comparar la curva de error en escala semilog y log-log muestra la tasa lineal frente a la sublineal de métodos estocásticos.

**Reflexiones**  

1. Prueba que con \(\eta=1/L\) la iteración alcanza la cota mínima teórica de razón de error para GD clásico.  
2. ¿Cómo cambia la tasa si la función incluye un término \(bx\)?  

---

## 2. Gradiente Descendente Por Lotes (Mini-batch)  

**Objetivo**  
Contrastar descenso por gradiente completo frente a mini-batch sobre datos sintéticos.

**Teoría esencial**  

* El estimador de gradiente por lote \(B\) es  
  \[
  \hat g_B=\frac{1}{|B|}\sum_{i\in B}\nabla \ell_i(\theta)
  \]  
  con varianza \(\sigma^{2}/|B|\).  
* El tamaño de lote óptimo equilibra **ruido** y **costo computacional**.

**Fórmulas clave**  

\[
\mathbb{E}\bigl[\|\hat g_B-g\|^{2}\bigr]=\frac{\sigma^{2}}{|B|}
\]  

**Análisis detallado**  

* Al disminuir \(|B|\) se gana velocidad por iteración pero aumenta la varianza → se necesitan más épocas.  
* El cuaderno muestra curvas de pérdida frente a tiempo real: evidencia que \(|B|=32\) suele ser un punto dulce en hardware común.  
* Faltan técnicas como *gradient accumulation* y *learning-rate warm-up* que permiten lotes virtuales grandes sin memoria extra.

**Reflexiones**  

1. Implementa *cyclical learning rate* y observa su efecto con \(|B|=8\).  
2. Discute por qué en redes profundas la relación rendimiento-tamaño de lote se vuelve no lineal.  

---

## 3. Mini-batch Con Dataset Diabetes  

**Objetivo**  
Aplicar Mini-batch GD real para regresión lineal en un conjunto de datos médico.

**Teoría esencial**  

* Pérdida MSE:  
  \[
  \mathcal{L}(\theta)=\frac{1}{n}\sum_{i=1}^{n}(y_i-\mathbf{x}_i^\top\theta)^2
  \]  
* Al normalizar características, la superficie de error se vuelve **más isotrópica**, mejorando el paso de GD.

**Fórmulas clave**  

* Gradiente de MSE:  
  \[
  \nabla_\theta \mathcal{L} = -\frac{2}{n}\mathbf{X}^\top (y-\mathbf{X}\theta)
  \]

**Análisis detallado**  

* El cuaderno incorpora **early stopping** basado en validación, reduciendo sobreajuste.  
* Comparación con la solución cerrada de mínimos cuadrados revela la cercanía del óptimo obtenido en pocas épocas.  
* Se podría añadir regularización \(l_1\) y \(l_2\) para explorar **bias–variance**.

**Reflexiones**  

1. Grafica coeficientes \(\theta\) frente a \(\lambda\) en *ridge regression* para visualizar *shrinkage*.  
2. ¿Qué ocurriría si introducimos variables altamente correlacionadas sin normalizar?  

---

## 4. Gradiente Descendente Estocástico (SGD)  

**Objetivo**  
Mostrar la ruta serpenteante de SGD actualizando con un solo ejemplo.

**Teoría esencial**  

* SGD satisface  
  \[
  \mathbb{E}\bigl[\nabla \ell_i(\theta)\bigr]=\nabla \mathcal{L}(\theta)
  \]  
* Convergencia esperada:  
  \[
  \mathbb{E}\bigl[\|\theta_t-\theta^\star\|\bigr]\le \mathcal{O}\bigl(\tfrac{1}{\sqrt{t}}\bigr)
  \]

**Fórmulas clave**  

* Decaimiento de learning rate: \(\eta_t = \eta_0 / (1+\gamma t)\).

**Análisis detallado**  

* Al no reordenar datos entre épocas, se introduce **sesgo de ordenación**.  
* Momentum suaviza la ruta:  
  \[
  v_{t+1}= \beta v_t + (1-\beta)\nabla \ell_i(\theta_t), \quad \theta_{t+1}= \theta_t - \eta v_{t+1}
  \]
* El cuaderno carece de comparación con optimizadores adaptativos como Adam, que usan segundos momentos.

**Reflexiones**  

1. Demuestra empíricamente la cota \(\mathcal{O}(1/\sqrt{t})\) en error.  
2. Analiza la sensibilidad a la baraja de datos (*shuffle vs. no shuffle*).  

---

## 5. Programación Lineal Clásica  

**Objetivo**  
Plantear un problema de maximización de utilidad y resolverlo con `scipy.optimize.linprog`.

**Teoría esencial**  

* Forma estándar:  
  \[
  \max\; c^\top x \quad \text{suj. a}\quad Ax\le b,\; x\ge 0
  \]  
* Teorema de la dualidad fuerte: \( \min b^\top y : A^\top y \ge c \).

**Fórmulas clave**  

* Condición de optimalidad primal-dual:  
  \[
  x_i(Ax-b)_i=0,\quad y_j(A^\top y-c)_j=0
  \]

**Análisis detallado**  

* El cuaderno usa método Simplex; comparar con barrera interior revela diferencias de iteraciones y robustez.  
* Análisis de sensibilidad: variando \(b\) +1 %, el óptimo cambia linealmente según multiplicadores de sombra \(y^\star\).  
* Variables enteras transforman el problema en MILP: se plantea el uso de `pulp` u `or-tools`.

**Reflexiones**  

1. Implementa el dual y verifica que el valor óptimo coincide numéricamente.  
2. Discute por qué Simplex puede ciclar y cómo lo evita la regla Bland.  

---

## 6. Programación Lineal En Dataset Cáncer De Mama  

**Objetivo**  
Reformular la separación lineal como LP que maximiza el margen.

**Teoría esencial**  

* Formulación Perceptrón-LP:  
  \[
  \max \rho \quad  
  \text{suj. a } y_i(\mathbf{w}^\top\mathbf{x}_i+b)\ge \rho,\; \|\mathbf{w}\|_\infty\le 1
  \]

**Fórmulas clave**  

* Al fijar \(\|\mathbf{w}\|_1\le 1\), se mantiene linealidad.  
* El margen óptimo \(\rho^\star\) se relaciona con la norma de \(\mathbf{w}\): \( \gamma =\rho^\star/\|\mathbf{w}\| \).

**Análisis detallado**  

* El cuaderno muestra que la factibilidad puede fallar (datos no separables). Se sugiere introducir **variables de holgura** \(\xi_i\) y penalizarlas.  
* Comparación con SVM lineal expone cómo la regularización \(C\) en SVM actúa como peso de holgura.  

**Reflexiones**  

1. Grafica el hiperplano óptimo y puntos soporte, resaltando mal clasificados.  
2. Analiza la diferencia entre margen geométrico y funcional.  

---

## 7. Algoritmos Metaheurísticos  

**Objetivo**  
Explorar búsqueda aleatoria, recocido simulado y algoritmo genético sobre la función Rastrigin  
\[
f(\mathbf{x}) = 10d + \sum_{i=1}^{d}\bigl(x_i^{2} - 10\cos 2\pi x_i\bigr).
\]

**Teoría esencial**  

* Recocido simulado acepta empeoramientos con probabilidad \(\exp(-\Delta E/T)\).  
* El algoritmo genético usa operadores de **crossover** y **mutación** para explorar el espacio.

**Fórmulas clave**  

* Temperatura geométrica: \(T_k = T_0 \alpha^{k}\).  
* Probabilidad de mutación: \(p_m = \tfrac{1}{d}\) típica para dimensión \(d\).

**Análisis detallado**  

* Se observa que recocido alcanza rápidamente un buen valor, pero necesita enfriamiento lento para refinado.  
* El algoritmo genético encuentra múltiples óptimos locales, mostrando **diversificación**; tuning de \(p_c, p_m\) es crucial.  
* Falta un marco estandarizado para comparar tiempo y evaluaciones; se propone registrar **hypervolume** de frentes de Pareto para multiobjetivo.

**Reflexiones**  

1. Diseña un *benchmark* con semilla fija y genera tablas de convergencia.  
2. ¿Cómo afecta la dimensionalidad (d = 2 → 30) al rendimiento relativo de cada heurística?  

---

## 8. Optimización De Hiperparámetros  

**Objetivo**  
Emplear Grid Search y Random Search para ajustar un modelo de Bosque Aleatorio.

**Teoría esencial**  

* El número esperado de muestras necesarias para cubrir completamente un hiperespacio crece exponencialmente (maldición de la dimensionalidad).  
* Random Search uniformemente muestrea y, con la misma cantidad de evaluaciones, **cubre más combinaciones relevantes** que una grilla.

**Fórmulas clave**  

* Probabilidad de que al menos un punto esté en la región de interés \(R\):  
  \[
  P = 1 - (1-\operatorname{vol}(R))^{N}
  \]

**Análisis detallado**  

* El cuaderno compara accuracy y tiempo; Random Search alcanza >95 % de la mejor métrica con 10 % de evaluaciones de Grid.  
* Faltan métricas tipo II como F1 o AUC, importantes en datasets desbalanceados.  
* Se sugiere añadir validación cruzada estratificada y *early-stopping* basada en tiempo.

**Reflexiones**  

1. Discute cuándo Grid podría ser preferible (espacio pequeño, interacciones precisas).  
2. Incorpora *successive halving* (ASHA) para asignar cómputo adaptativamente.  

---

## 9. Optimización Bayesiana  

**Objetivo**  
Optimizar una función caja negra con procesos gaussianos y criterio de adquisición *Expected Improvement* (EI).

**Teoría esencial**  

* Suponemos \(f\sim \mathcal{GP}(m,k)\).  
* EI:  
  \[
  \text{EI}(x)=\bigl(\mu(x)-f^\star -\xi\bigr)\Phi(z)+\sigma(x)\phi(z),\quad z=\frac{\mu(x)-f^\star -\xi}{\sigma(x)}
  \]

**Fórmulas clave**  

* Actualización posterior:  
  \[
  \mu(x)=k^\top(K+\sigma_n^2I)^{-1}\mathbf{y},\qquad
  \sigma^{2}(x)=k(x,x)-k^\top(K+\sigma_n^2I)^{-1}k
  \]

**Análisis detallado**  

* El cuaderno visualiza el **surrogate** y puntos evaluados, ayudando a entender **exploración vs. explotación**.  
* Sensibilidad a la elección de kernel RBF y sus hiperparámetros; kernel Matérn 5/2 puede modelar funciones menos suaves.  
* Ampliación a espacio mixto (continuo + categórico) requiere técnicas como one-hot o embeddings y GP heterogéneos.

**Reflexiones**  

1. Compara EI con **Upper Confidence Bound** (UCB) y **Probability Of Improvement**.  
2. Mide la ganancia de BO frente a Random Search en ≤20 evaluaciones; reporta media y desviación estándar.

---

# Conclusiones Generales  

1. La adecuación del **algoritmo de optimización** depende de la convexidad, dimensión y costo de la función objetivo.  
2. Comprender los **supuestos teóricos** (Lipschitz, convexidad, ruido) permite elegir hiperparámetros fundamentados.  
3. Las técnicas **estocásticas** (SGD, metaheurísticos) sacrifican exactitud puntual pero escalan a datos masivos o funciones no diferenciables.  
4. La **optimización de hiperparámetros** es un caso especial de optimización global; los métodos bayesianos reducen evaluaciones costosas.  
5. Documentar experimentos con métricas reproducibles y visualizaciones es crítico para validar resultados y transferir conocimiento.  

---

# Referencias  

Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*. Cambridge University Press.  
Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.  
Nocedal, J., & Wright, S. (2006). *Numerical Optimization* (2nd ed.). Springer.  
Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research, 12*, 2825-2830.
