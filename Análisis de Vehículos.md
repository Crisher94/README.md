Resumen del Proyecto: Dashboard de Análisis de Vehículos
Descripción General
Este proyecto consiste en el desarrollo de una aplicación web interactiva de análisis de datos construida con Python. La herramienta está diseñada para explorar un conjunto de datos 
de anuncios de venta de coches en Estados Unidos, permitiendo a los analistas de datos o usuarios interesados visualizar tendencias de mercado de manera rápida y sencilla.

El objetivo principal es transformar un archivo CSV estático en una plataforma dinámica donde se puedan identificar patrones, como la relación entre el desgaste de un vehículo (kilometraje) y su valor de venta.

Funcionalidades Principales
La aplicación proporciona una interfaz limpia y funcional con las siguientes capacidades:

 Mediante el uso de Streamlit, el usuario puede decidir qué gráficos ver en tiempo real utilizando componentes como botones y casillas de verificación.

Análisis de Distribución (Histogramas): Permite visualizar la frecuencia de los datos en la columna del odómetro, ayudando a entender qué tan "viejos" o "nuevos" son los autos en el inventario.

Análisis de Correlación (Gráficos de Dispersión): Facilita la comparación de dos variables numéricas (como Precio vs. Kilometraje) para observar cómo influye el uso del vehículo en su depreciación.

Visualizaciones Dinámicas: Gracias a la integración con Plotly, los gráficos no son imágenes estáticas; el usuario puede hacer zoom, pasar el cursor sobre los puntos para ver detalles específicos y descargar las capturas de las gráficas.

Pre-procesamiento de Datos: La aplicación incluye una etapa de limpieza donde se gestionan los valores ausentes (NaN) en columnas críticas como el año del modelo y el kilometraje, garantizando que los gráficos sean precisos y representativos.
