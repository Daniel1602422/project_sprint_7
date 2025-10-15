# Import packages
import streamlit as st
import pandas as pd
import plotly.express as px
path = r'C:\Users\HP001\Documents\Cursos\Tripleten\Sprint 7\Project\project_sprint_7-1\vehicles_us.csv'
car_data = pd.read_csv(path)
# car_data.sample(5)
st.header('Car Data Analisys')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir diagrama de dispersión')
if scatter_button:
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
