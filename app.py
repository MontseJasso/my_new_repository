import pandas as pd
import plotly.express as px
import streamlit as st

st.header("PROYECTO 7: 'Analisis de vehiculos'")


car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Construcción del gráfico de dispersión
    scatter_fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre odómetro y precio")

    # Mostrar el gráfico de dispersión
    st.plotly_chart(scatter_fig, use_container_width=True)