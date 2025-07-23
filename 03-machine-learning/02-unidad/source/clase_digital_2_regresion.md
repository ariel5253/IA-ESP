
# 📘 Clase Digital 2: Aprendizaje Supervisado - Regresión

## ✅ Requisitos de finalización

| Requisito     | Estado  |
|---------------|---------|
| Ver contenido | ✅ Hecho |

---

## 👋 ¡Bienvenido!

Bienvenidos a la clase digital 2 sobre **"Aprendizaje Supervisado - Regresión"**. Estoy seguro de que están aquí porque quieren aprender sobre regresión y los algoritmos de predicción.

---

## 📌 ¿Qué son los algoritmos de regresión?

Los **algoritmos de regresión** son un conjunto de técnicas en el campo del aprendizaje automático (Machine Learning) que se utilizan para modelar y predecir relaciones entre variables. En particular, se utilizan para predecir un valor numérico continuo en función de una o más variables independientes.

### Características Principales

- **Variable Dependiente y Variables Independientes**: se predice una variable dependiente con base en una o más independientes.
- **Modelo Matemático**: se construye un modelo que describe la relación entre variables.
- **Predicción Continua**: se predicen valores numéricos, no etiquetas.

### Usos Principales

- **Predicción**: como precios futuros, ventas, rendimiento de inversiones.
- **Estimación de Parámetros**: por ejemplo, pendiente e intersección.
- **Modelado de Relaciones**: entender el impacto entre variables.
- **Análisis de Tendencias**: como crecimiento poblacional o climático.
- **Optimización**: encontrar combinaciones óptimas de variables.

---

## 📈 Regresión Lineal

La regresión lineal modela la relación entre una variable dependiente y una o más independientes mediante una línea recta.

### Fórmula general:

```
Y = a + bX + e
```

- **Y**: variable dependiente.
- **X**: variable independiente.
- **a**: intersección (cuando X = 0).
- **b**: pendiente de la línea.
- **e**: error o residuo.

🔍 El objetivo es minimizar la suma de los errores al cuadrado usando el método de **mínimos cuadrados**.

📘 Recurso práctico: [Documentación oficial de Scikit-Learn – LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

🎥 [Video: REGRESIÓN LINEAL - SCIKIT LEARN (AprendeIA)](https://youtu.be/SZyH6YkQqIk)

---

## 🔷 Extensiones y conceptos adicionales

### 🔹 ¿Qué es la regresión polinomial?

Extiende la regresión lineal permitiendo relaciones no lineales al agregar potencias de las variables: `x²`, `x³`, etc.

### 🔹 ¿Qué es el escalado de características?

El **feature scaling** normaliza los valores de entrada, ayudando a que algoritmos como el descenso del gradiente converjan más rápido.

### 🔹 Descenso de Gradiente en Regresión Polinomial

El descenso del gradiente sigue siendo el algoritmo de optimización, pero requiere más cuidado por el número mayor de características (x, x², x³, …).

---

## ✅ Recomendaciones

- Revisa los cuadernos de práctica en orden.
- Aplica **escalado** antes de entrenar modelos polinomiales.
- Compara modelos **con y sin escalado** para ver diferencias.
- Usa interpretaciones gráficas y numéricas para justificar resultados.

---

## 📚 Bibliografía recomendada

- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (2nd ed.). O'Reilly Media.
- Guyon, I., & Elisseeff, A. (2003). *An Introduction to Variable and Feature Selection*. JMLR.
- Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.
- James, G., et al. (2013). *An Introduction to Statistical Learning*. Springer.
- Kuhn, M., & Johnson, K. (2019). *Feature Engineering and Selection*. CRC Press.
- Müller, A. C., & Guido, S. (2017). *Introduction to Machine Learning with Python*. O'Reilly Media.
- Raschka, S., & Mirjalili, V. (2019). *Python Machine Learning* (3rd ed.). Packt Publishing.
- Witten, I. H., et al. (2011). *Data Mining: Practical Machine Learning Tools and Techniques*. Morgan Kaufmann.

---

🎓 **Concluimos la clase digital 2**. Ahora los invito a realizar la actividad de aprendizaje correspondiente. ¡Éxitos!
