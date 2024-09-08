# Sistema de Recomendación de Películas y Series de Netflix

## ¿Qué hace el sistema?

Este proyecto es un sistema de recomendación de películas y series de Netflix desarrollado en Python. Contiene un archivo CSV en el que se almacenan cientos de producciones con información detallada respecto al título, descripción, género, director, reparto, país de producción y tipo de contenido. Los usuarios pueden seleccionar un título específico y luego buscar recomendaciones similares en función de la información proporcionada por el título seleccionado. Las recomendaciones se facilitarán atendiendo a **TODOS los criterios seleccionados por el usuario**, lo que puede limitar las recomendaciones a medida que se añaden más filtros.

## Instrucciones de Uso

1. Asegúrate de que el archivo "netfliData.csv" se encuentre en el mismo directorio que "main.py"
2. Ejecuta la aplicación. Te aparecerá una interfaz en la que podrás ver un listbox con una serie de títulos. 
3. Desplázate por el listbox y selecciona la película o serie que te interese.
4. En la parte "Criterios de búsqueda" te aparecerán todos los criterios por los que puedes buscar. Selecciona los que te interesen y pulsa "Buscar"
No olvides que cuantos más criterios selecciones, más restrictivos serán los resultados.
5. Te aparecerá una tabla con todos las películas y/o series que coincidan con tus criterios de búsqueda. 
6. Enciende la televisión, coge las palomitas y ¡feliz tarde de sábado con Netflix!

## Características importantes
+ **Recomendaciones precisas:** el sistema proporcionará recomendaciones que coincidan con TODOS los criterios seleccionados.
+ **Resultados limitados:** a medida que se añaden más criterios, las opciones de recomendación se reducirán, pudiendo llegar a un único resultado.
+ **Interfaz amigable:** una interfaz de usuario sencilla y fácil de usar para realizar búsquedas y obtener recomendaciones relacionadas.

## Preguntas frecuentes (FAQ)

1. **¿Qué pasa si no obtengo ninguna recomendación?**
Si no obtienes ninguna recomendación, es posible que los criterios seleccionados sean demasiado específicos. Intenta reducir el número de criterios para obtener más resultados.

2. **¿Puedo buscar por más de un criterio a la vez?**
Sí, puedes seleccionar múltiples criterios de búsqueda. El sistema utilizará TODOS los criterios seleccionados para encontrar las recomendaciones.

3. **¿Qué tipo de contenido puedo buscar?**
Puedes buscar tanto películas como series de televisión. El tipo de contenido está especificado en el archivo CSV.

4. **¿Cómo se almacenan los datos de las películas y series?**
Los datos se almacenan en un archivo CSV que contiene información detallada sobre cada título, incluyendo título, descripción, género, director, reparto, país de producción, tipo de contenido y otros

5. **¿Puedo añadir más películas y series al archivo CSV?**
Sí, puedes añadir más títulos al archivo CSV siempre que respetes el formato del archivo existente.
