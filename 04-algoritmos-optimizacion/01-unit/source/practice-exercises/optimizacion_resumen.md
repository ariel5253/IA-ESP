---
title: notas de optimización en ia
author: Jesús Ariel González Bonilla
date: August 07, 2025
---

# resumen

Este documento resume nueve cuadernos de práctica sobre optimización en inteligencia artificial y presenta conclusiones clave para repaso.

## 1. gradiente descendente clásico

- objetivo: minimizar \(f(x)=x^2\) con descenso por gradiente completo  
- punto clave: la tasa de aprendizaje controla la convergencia  
- ejercicios sugeridos: demostrar convergencia analítica, explorar valores de \(\eta\) que divergen

## 2. gradiente descendente por lotes (mini‑batch)

- compara batch completo vs. mini‑batch en datos sintéticos  
- introduce el compromiso varianza‑sesgo del gradiente  
- profundización: medición de velocidad de convergencia y _learning rate_ dinámico

## 3. mini‑batch con dataset diabetes

- aplica mini‑batch gd real sobre regresión lineal  
- agrega normalización de _features_ y _early stopping_  
- tareas: búsqueda manual del _learning rate_ y comparación con mínimos cuadrados cerrados

## 4. gradiente descendente estocástico

- muestra la variabilidad del camino usando un solo ejemplo por iteración  
- recomienda añadir *shuffle*, momentum o adam  
- reto: verificar empíricamente la cota de \(\mathcal{O}(1/\sqrt{t})\)

## 5. programación lineal clásica

- formula un problema lp y lo resuelve con `scipy.optimize.linprog`  
- extensión: comparar simplex vs. barrera interior; introducir variables enteras con pulp

## 6. programación lineal en dataset cáncer de mama

- formula la separación lineal como lp para maximizar el margen  
- mejoras: mostrar puntos mal clasificados y comparar con svm lineal

## 7. algoritmos metaheurísticos

- implementa búsqueda aleatoria, recocido simulado y algoritmo genético sobre función rastrigin  
- actividad: crear un marco común de evaluación que registre iteraciones y tiempo

## 8. optimización de hiperparámetros

- usa grid search y random search para un _random forest_  
- reflexiona sobre exploración vs. explotación  
- preguntas: ¿cuándo random search supera grid search en alta dimensionalidad?

## 9. optimización bayesiana

- introduce procesos gaussianos y _expected improvement_  
- fortalezas: visualización animada del _surrogate_  
- extensión: aplicar a _tuning_ de redes profundas con espacio mixto usando optuna

---

# conclusiones para repaso

1. el **gradiente descendente** y sus variantes equilibran precisión y costo computacional; ajustar correctamente la tasa de aprendizaje es crítico.  
2. la **programación lineal** sigue siendo una herramienta poderosa para problemas deterministas y lineales; entender su dualidad ayuda a interpretar resultados.  
3. los **metaheurísticos** aportan soluciones robustas en espacios no convexos, pero requieren calibración cuidadosa de hiperparámetros.  
4. la **optimización de hiperparámetros** con técnicas aleatorias o bayesianas mejora significativamente el rendimiento de modelos sin sobre‑fitar.  
5. documentar resultados con métricas y visualizaciones claras facilita la comparación entre métodos y respalda la toma de decisiones.

---

# referencias

Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press.  
Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.  
Nocedal, J., & Wright, S. (2006). *Numerical optimization* (2nd ed.). Springer.  
Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit‑learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825‑2830.
