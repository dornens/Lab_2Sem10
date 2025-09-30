# Laboratorio 2 – Segundo Cómputo  
**Semana 10 – Análisis de datos con Pandas**  

## Colaboradores  
- Franklin Aldahir Portillo Flores SMSS011624
- Juan Ramon Espinal Coto SMSS102323  

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

### Interpretación de Resultados  

**a. Describe brevemente de qué trata el dataset utilizado**  
El dataset seleccionado contiene información estructurada sobre diferentes variables de interés. Incluye tanto datos numéricos como categóricos, lo que permite analizar patrones, comparaciones y tendencias en el tiempo.  

**b. ¿Qué información permite ver el resumen estadístico?**  
El resumen estadístico muestra medidas como el promedio, valores mínimos y máximos, cuartiles y desviación estándar. Con ello se obtiene una visión general del comportamiento de los datos, se identifican valores atípicos y se observa la variación de cada columna numérica.  

**c. ¿Qué cambios o tendencias se detectan en la información del dataset?**  
Se evidencian ciertas fluctuaciones en los registros. Algunas variables tienden a concentrarse en valores específicos, mientras que otras muestran un crecimiento o disminución progresiva a lo largo del tiempo.  

**d. ¿Qué categorías sobresalen en la comparación y por qué crees que será?**  
En la comparación de categorías, algunas destacan significativamente por su mayor frecuencia o por valores altos en indicadores clave. Esto puede deberse a su popularidad, mayor demanda, condiciones del mercado o características propias que las hacen más representativas en el dataset.  

**e. ¿Qué diferencias se observan entre los primeros y últimos registros?**  
Al observar los primeros registros, se aprecia un comportamiento inicial más estable o con valores moderados. En los últimos registros, en cambio, aparecen variaciones más notorias, ya sea en forma de crecimiento, descenso o dispersión de los datos.  

**f. ¿Qué aportan las medidas estadísticas al análisis del dataset?**  
Las medidas estadísticas permiten profundizar en el análisis:  
- La **media** ayuda a conocer el valor central promedio.  
- La **mediana** es útil para identificar el punto medio y reducir el efecto de valores extremos.  
- La **desviación estándar** indica la variabilidad de los datos, mostrando si se concentran cerca de la media o están muy dispersos.  

---

## De qué trata la datasheet  
La datasheet utilizada corresponde a un listado de canciones con información relevante de su contexto musical e histórico. A diferencia de datasets de ventas o financieros, este material está enfocado en **música**, recopilando datos que permiten analizar la trayectoria de artistas, compositores y la permanencia de sus obras en listas de éxito.  

Este análisis es útil para observar **tendencias culturales y musicales** a lo largo de diferentes décadas, así como para comprender qué canciones han tenido mayor impacto y permanencia en el público.  
