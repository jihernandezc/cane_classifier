## 🌱 Descripción del proyecto  

Este proyecto tiene como objetivo analizar la calidad de trozos de caña de azúcar a partir de imágenes, utilizando técnicas de visión artificial. Para ello, se implementaron distintos procesos en tres notebooks principales: **segmentación**, **extracción de características** y **clasificación**, además de un bot de Telegram que permite la clasificación automática de imágenes enviadas por los usuarios.  

## 📂 Estructura del proyecto  

### 1️⃣ `01-segmentation.ipynb`  
En este notebook se lleva a cabo la segmentación de las imágenes, separando los trozos de caña del fondo. Se probaron distintos métodos para mejorar la precisión, pero algunos desafíos surgieron debido a las similitudes de color entre la caña y el fondo. A pesar de estas dificultades, se logró una segmentación funcional que permitió continuar con el procesamiento de las imágenes, obteniendo buenos resultados con las técnicas disponibles.  

### 2️⃣ `02-feature-extraction.ipynb`  
En este notebook se procesan las imágenes segmentadas para obtener información relevante mediante detección de puntos clave (Harris), gradientes, patrones locales y análisis de textura (GLCM). También se generaron mapas de densidad para visualizar la distribución de características. 

### 3️⃣ `03-classification-model.ipynb`  
En este notebook se entrena un modelo de clasificación utilizando las características extraídas previamente. A pesar de contar con un dataset limitado y enfrentar problemas de sobreajuste, se probaron distintos modelos y técnicas de aumento de datos para mejorar la precisión en la clasificación de los trozos de caña. Los resultados obtenidos fueron positivos, demostrando la efectividad de las características seleccionadas y las técnicas aplicadas.  

### 🤖 `bot.py` - Implementación del bot de Telegram  

El [Bot de Telegram](https://t.me/CaneClassifierBot) fue desarrollado para facilitar la clasificación de imágenes de caña de azúcar de forma rápida y accesible. En lugar de ejecutar manualmente los notebooks, cualquier usuario puede enviar una foto al bot y recibir una clasificación instantánea basada en el modelo entrenado.  

Para demostrar su viabilidad, desplegamos el bot en **Railway**, permitiendo su funcionamiento sin necesidad de ejecutar código localmente. Si bien actualmente opera con ciertas limitaciones debido a la falta de un servidor dedicado, esta implementación muestra el potencial del proyecto. Con recursos adecuados, podríamos mejorar su capacidad y disponibilidad, haciéndolo aún más útil en entornos reales, como el monitoreo de cultivos de caña.  
