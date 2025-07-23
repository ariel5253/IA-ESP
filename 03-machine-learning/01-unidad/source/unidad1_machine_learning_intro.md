
# 👩‍🏫 Bienvenida a la Unidad 1: Fundamentos de Machine Learning

¡Hola, estimados estudiantes!

Es un gusto darles la bienvenida a esta primera unidad de la asignatura **Machine Learning**, un componente esencial de la especialización en **Inteligencia Artificial**. En esta clase digital nos acercaremos a los fundamentos del aprendizaje automático, sus tipos, aplicaciones, y conceptos clave como la regresión lineal, las funciones de pérdida y el descenso del gradiente.

Al finalizar esta clase, tendrán una comprensión general de cómo funciona el aprendizaje automático, cuáles son sus componentes esenciales y por qué es tan relevante en la actualidad.

Antes de iniciar con los contenidos de esta unidad, es importante asegurarnos de que cuenten con las herramientas necesarias para programar en Python y ejecutar los cuadernos Jupyter.

A continuación, te comparto un video corto donde te explico paso a paso cómo instalar Python en tu equipo y cómo configurar Jupyter Notebook:

📽️ *(Inserta aquí el enlace al video de instalación)*

> 💡 **Importante**: Si ya tienes Python y Jupyter instalados, puedes pasar al siguiente bloque de contenido. De lo contrario, te recomiendo seguir el video con calma y asegurarte de poder ejecutar un cuaderno `.ipynb` correctamente.

---

## 1. ¿Qué es Machine Learning?

El **Machine Learning (ML)** es una forma de programar sistemas para que puedan aprender a partir de los datos. A diferencia de la programación tradicional, donde se escriben reglas explícitas, en ML los modelos *aprenden* patrones desde ejemplos.

📌 **Ejemplo práctico**: Reconocer si un correo es spam. Es difícil programar todas las reglas, pero es posible entrenar un modelo con miles de correos clasificados.

🔍 **Analogía**: Enseñar a un niño a reconocer frutas mostrando ejemplos, no dándole reglas.

🎥 *(Inserta aquí el video explicativo sobre qué es ML)*

---

## 2. Tipos de Aprendizaje

- **Supervisado**: el modelo aprende con datos etiquetados (ej. horas de estudio y nota final).
- **No supervisado**: el modelo encuentra patrones sin etiquetas (ej. agrupamiento de clientes).
- **Por refuerzo**: el modelo aprende por recompensas (ej. robots que aprenden a caminar).

---

## 3. Aprendizaje Supervisado

Es el más utilizado en la práctica. El modelo recibe *inputs* (features) y una salida esperada (*target*), y aprende a predecirla.

📌 **Ejemplo**: Predecir el precio de una casa con base en el número de habitaciones y metros cuadrados.

**Flujo básico**: Entrenar → Evaluar → Predecir

---

## 4. Aprendizaje No Supervisado

Se aplica cuando no tenemos salidas conocidas. Se utiliza para descubrir patrones, reducir dimensiones o segmentar datos.

📌 **Ejemplo**: Agrupar estudiantes por hábitos de estudio sin saber sus resultados.

**Técnicas comunes**: Clustering (agrupamiento), PCA (reducción de dimensionalidad)

---

## 5. Regresión Lineal: El modelo base

Permite modelar relaciones lineales entre variables. Su fórmula general es:

```
y = w * x + b
```

📌 **Ejemplo**: Relación entre horas de estudio (x) y nota final (y).

**Interpretación**: Cada coeficiente indica cuánto cambia `y` si `x` aumenta una unidad.

---

## 6. Funciones de Pérdida y Costo

Nos permiten cuantificar el error de un modelo. Las más comunes son:

- **MSE**: penaliza errores grandes.
- **MAE**: mide error absoluto promedio.

🧭 **Visualización**: Superficie que queremos minimizar para encontrar el mejor modelo.

---

## 7. Descenso del Gradiente

Es el algoritmo más usado para encontrar los parámetros que minimizan la pérdida.

📌 **Idea**: Calcula la pendiente de la función de costo y ajusta los pesos en dirección contraria.

**Analogía**: Bajar una montaña en la niebla guiado solo por la pendiente bajo tus pies.

---

## 8. Tasa de Aprendizaje

Controla el tamaño de cada paso del descenso del gradiente.

- Muy alta: puede saltarse el mínimo.
- Muy baja: muy lento o se estanca.

🔧 Es un **hiperparámetro clave**: se elige por prueba y error.

---

## 🧠 Cierre y Reflexión Final

**Machine Learning** es una herramienta poderosa que requiere entender sus fundamentos para aplicarla adecuadamente. En esta unidad hemos sentado las bases. A medida que avancemos, profundizaremos en los algoritmos y su aplicación.

📌 **Recomendación**: Repasa los conceptos en la tabla resumen de la unidad y experimenta con ejemplos sencillos en Python.
