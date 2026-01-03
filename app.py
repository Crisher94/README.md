import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.header('Análisis de Anuncios de Vehículos')

car_data = pd.read_csv('../vehicles_us.csv')

# --- SECCIÓN DE HISTOGRAMA ---
st.write('### Visualización de Inventario')
build_histogram = st.checkbox('Construir histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Creando un histograma para la columna odómetro...')
    
    # Creamos un histograma usando Plotly Express 
    fig = px.histogram(car_data, x="odometer", title="Distribución del Kilometraje (Odómetro)")
    
    # Mostrar el gráfico
    st.plotly_chart(fig, use_container_width=True)

# --- SECCIÓN DE GRÁFICO DE DISPERSIÓN ---
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creando un gráfico de dispersión: Precio vs. Odómetro')
    
    # Crear gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", 
                             title="Relación entre Precio y Kilometraje",
                             labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'},
                             opacity=0.5)
    
    # Mostrar el gráfico
    st.plotly_chart(fig_scatter, use_container_width=True)