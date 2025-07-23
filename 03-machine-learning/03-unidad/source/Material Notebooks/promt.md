# Prompt Profesional para Documentar y Analizar Ejercicios en Notebooks

---

## Objetivo

Este prompt está diseñado para guiar la edición, documentación y análisis de notebooks de ejercicios de machine learning, asegurando que cada cambio realizado sea claramente identificado, explicado y justificado. El objetivo es facilitar el aprendizaje, la revisión y la comprensión profunda de cada ejercicio.

---

## Instrucciones para el Editor/Analista

1. **Recorre todo el notebook antes de realizar cambios.**
   - Identifica las secciones clave: introducción, objetivos, código principal, resultados, conclusiones.
   - Detecta el bloque de código que requiere ajuste o mejora.

2. **Antes de modificar cualquier código:**
   - Inserta una celda markdown resaltada (color, tamaño de letra) justo antes del bloque a modificar.
   - En esa celda, especifica:
     - Qué línea se va a cambiar.
     - La línea original y la línea modificada, ambas resaltadas y con salto de línea automático.
     - Explicación clara del motivo del cambio y su impacto en el ejercicio.

3. **Después de modificar el código:**
   - Verifica que el cambio cumple el objetivo (por ejemplo, mejorar la clasificación binaria usando regresión logística).
   - Si es relevante, muestra resultados esperados o ejemplos visuales.

4. **Conclusiones personales:**
   - Inserta un recuadro destacado antes de las conclusiones, indicando que a partir de ese punto todo son reflexiones personales.
   - Documenta de forma clara y extensa:
     - Qué aprendiste del ejercicio.
     - Por qué el cambio fue necesario.
     - Recomendaciones para abordar retos similares.
     - Fórmulas clave y pasos metodológicos.

5. **Formato y visualización:**
   - Usa colores y estilos para separar claramente avisos, cambios de código y conclusiones.
   - Asegúrate de que las líneas largas hagan salto de línea automático.
   - Mantén la documentación profesional, clara y orientada al aprendizaje.

---

## Ejemplo de Celda Markdown para Cambios de Código

```markdown
<div style='background-color: #ff9800; color: #222; padding: 8px 12px; border-radius: 6px; font-weight: bold; font-size: 1.1em; margin-bottom: 10px;'>¡ATENCIÓN!<br>En el siguiente bloque de código se realizó el siguiente cambio para mejorar la clasificación binaria:</div>
<pre style='background-color: #fff3e0; color: #d32f2f; font-size: 1em; border-left: 6px solid #d32f2f; padding: 8px; white-space: pre-wrap; word-break: break-word;'><b>Línea original:</b>
addpt = plt_one_addpt_onclick( x_train, y_train, w_in, b_in, logistic=False )</pre>
<pre style='background-color: #e0f7fa; color: #00796b; font-size: 1em; border-left: 6px solid #00796b; padding: 8px; white-space: pre-wrap; word-break: break-word;'><b>Línea modificada:</b>
addpt = plt_one_addpt_onclick( x_train, y_train, w_in, b_in, logistic=True )</pre>
<div style='background-color: #ffecb3; color: #333; padding: 6px 10px; border-radius: 4px; font-size: 0.95em; margin-top: 8px;'>Este cambio activa el modelo de regresión logística, que es más adecuado para problemas de clasificación binaria.</div>
```

---

## Ejemplo de Celda Markdown para Conclusiones Personales

```markdown
<div style='background-color: #ffe066; color: #333; padding: 10px 14px; border-radius: 6px; font-weight: bold; font-size: 1.1em; margin-bottom: 10px;'>A partir de aquí, todas las secciones corresponden únicamente a <u>conclusiones personales</u> y reflexiones del autor.</div>
<span style='background-color: #ffe066; color: #333; padding: 4px 8px; border-radius: 4px; font-weight: bold;'>Conclusiones personales</span>

- El uso de regresión logística mejora la clasificación binaria, ajustando mejor los datos y prediciendo probabilidades entre 0 y 1.
- La regresión lineal no es adecuada para este tipo de problemas, ya que puede generar predicciones fuera del rango y no separa bien las clases.
- Es importante elegir el modelo correcto según la naturaleza de los datos.
```

---

## Recomendación

Utiliza este prompt como plantilla para documentar cualquier ejercicio, asegurando que cada cambio y reflexión quede registrado de forma profesional y clara. Esto te permitirá revisar, aprender y compartir tu trabajo de manera efectiva.

---
