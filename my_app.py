# Import packages
import streamlit as st
import pandas as pd
import plotly.express as px
path = 'vehicles_us.csv'
car_data = pd.read_csv(path)
# car_data.sample(5)
st.header('Análisis Inicial de Automóviles')
hist_button = st.button('Click para construir un histograma')
if hist_button:
    st.write(
        'Creación de un histograma de frecuencias para el análisis de la distribución del kilometraje en los automóviles.')
    fig = px.histogram(car_data, x="odometer",
                       title='Histograma de Frecuencias: Distibución de kilometraje')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Clcik para construir un diagrama de dispersión')
if scatter_button:
    st.write('Creación de un diagrama de dispersión para obervar si hay cierta correlación entre el precio y el kilometraje del automóvil.')
    fig2 = px.scatter(car_data, x='odometer', y='price',
                      title='Diargama de disperción: Kilometraje vs Precio')
    st.plotly_chart(fig2, use_container_width=True)

car_model = car_data.groupby(by='model')['price'].mean(
).sort_values(ascending=False).head(10)
bar_chart = pd.DataFrame(car_model)
bar_chart.reset_index(inplace=True)
build_bar = st.checkbox('Click para construir un gráfico de barras.')
if build_bar:
    st.write('Creación de un gráfico de barras donde se muestra los modelos de automóviles con mayor precio promedio')
    fig3 = px.bar(bar_chart, x='model', y='price')
    st.plotly_chart(fig3, use_container_width=True)
