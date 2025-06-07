# Clasificación de Géneros Cinematográficos con sLDA

Este proyecto aplica el modelo Supervised Latent Dirichlet Allocation (sLDA) para representar sinopsis de películas como vectores densos (embeddings) y predecir su género principal mediante aprendizaje supervisado.

## Objetivo

Predecir el género de una película a partir de su sinopsis (`overview`), utilizando el modelo sLDA para generar representaciones estadísticas de texto y entrenar un clasificador supervisado.

## Dataset

Se utiliza el conjunto de datos The Movies Dataset de Kaggle, específicamente el archivo `movies_metadata.csv`, que contiene información sobre más de 45.000 películas.  
Se consideran únicamente sinopsis no vacías y películas clasificadas con un único género dentro de las siguientes 13 categorías:

- Drama, Comedy, Documentary, Horror, Thriller, Western, Action, Animation, Science Fiction, Crime, Music, Adventure.

## Preprocesamiento

- Filtrado de sinopsis vacías.
- Conservación de películas con un solo género válido.
- Fragmentación y limpieza del texto para asegurar su compatibilidad con el modelo sLDA.

## Metodología

- Generación de embeddings mediante sLDA.
- Validación cruzada (k=5) para seleccionar el número óptimo de tópicos (p ∈ [10, 20]).
- Evaluación final con validación cruzada k=10 usando ROC-AUC.
- Entrenamiento final e interpretación de tópicos y coeficientes del modelo.

## Resultados Esperados

- Identificación de la estructura latente del conjunto de sinopsis.
- Predicción eficaz del género usando los embeddings generados.
- Evaluación del modelo y visualización de temas.
- Generación de 3 sinopsis ficticias y análisis de sus resultados.

## Requisitos

Este proyecto requiere las siguientes librerias:

```txt
numpy
pandas
matplotlib
scikit-learn
gensim
seaborn
```

### Instalación

```bash
pip install -r requirements.txt
```

## Estructura

- Proyecto_2.ipynb: Notebook principal con el flujo de análisis.
- utils.py: Funciones auxiliares para preprocesamiento y manejo de datos.
- requirements.txt: Dependencias necesarias para reproducir el entorno.

### Autores: Alejandro Vega, Juan Sebastian Rodriguez y Maria Fernanda Palacio
