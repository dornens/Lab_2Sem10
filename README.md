# Laboratorio 2 – Segundo Cómputo  
**Semana 10 – Análisis de datos con Pandas**  

## Colaboradores  
- Franklin Aldahir Portillo Flores  
- Juan Ramon Espinal Cotoy  

---

## Descripción del proyecto  
Este laboratorio tiene como objetivo aplicar herramientas de la librería **Pandas** en Python para el análisis de datos, utilizando un dataset descargado desde **Kaggle**.  

El dataset seleccionado se titula **“Top 500 Songs”**, el cual recopila información sobre quinientas canciones consideradas como las más influyentes e importantes en la historia de la música. Contiene datos como:  
- Título de la canción  
- Descripción y reseña breve  
- Álbum en el que aparece  
- Artista  
- Compositores  
- Productores  
- Fecha de lanzamiento  
- Semanas en lista de popularidad  
- Posición alcanzada  

---

## Funcionamiento del código  
1. **Carga del dataset**: Se utiliza `pd.read_csv()` indicando la codificación correcta (`latin1`) para evitar errores de lectura.  
2. **Exploración inicial**: Con funciones como `head()` y `tail()` se muestran los primeros y últimos registros para conocer la estructura de los datos.  
3. **Tipos de datos**: Con `dtypes` se identifican los tipos de cada columna, distinguiendo entre texto y valores numéricos.  
4. **Resumen estadístico**: Se aplica `describe()` para obtener un panorama general de los datos.  
5. **Ordenamiento**: Se usa `sort_values()` sobre la columna de semanas en lista, para identificar qué canciones permanecieron más tiempo en los rankings.  
6. **Medidas estadísticas**: Se calculan la **media**, **mediana** y **desviación estándar** de las semanas en lista, lo que permite comparar el comportamiento general de las canciones en términos de permanencia en popularidad.  

---

## De qué trata la datasheet  
La datasheet utilizada corresponde a un listado de canciones con información relevante de su contexto musical e histórico. A diferencia de datasets de ventas o financieros, este material está enfocado en **música**, recopilando datos que permiten analizar la trayectoria de artistas, compositores y la permanencia de sus obras en listas de éxito.  

Este análisis es útil para observar **tendencias culturales y musicales** a lo largo de diferentes décadas, así como para comprender qué canciones han tenido mayor impacto y permanencia en el público.  
