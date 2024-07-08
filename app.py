import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('C:/Users/User/Documents/Data Analysis/Futebol/Brasileirao2003-2023/dataset/brasileirao_serie_a.csv')
tab1, tab2 = st.tabs(['Time','Confrontos'])


with tab1:
    df_filtro_ano = st.sidebar.select_slider('Ano', sorted(df['ano_campeonato'].unique()))
    df_ano_filtrado = df[df['ano_campeonato'] == df_filtro_ano]
    df_filtro_times = st.sidebar.selectbox('Selecione um time', sorted(df_ano_filtrado['time_mandante'].unique()))
    df_final_filtrado = df_ano_filtrado[df_ano_filtrado['time_mandante'] == df_filtro_times]
    
    col1, col2, col3, col4, col5 = st.columns(5)
    chutes_mandante = round(df_final_filtrado.loc[:,'chutes_mandante'].mean())
    col1.metric('Chutes Mandante',chutes_mandante)