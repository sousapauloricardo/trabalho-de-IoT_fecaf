import streamlit as st
import pandas as pd
import plotly.express as px
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.database import get_engine

st.set_page_config(page_title="IoT Dashboard", layout="wide")
engine = get_engine()

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.title('📊 Dashboard de Temperaturas IoT')

try:
    # Gráfico 1: Média por Dispositivo
    st.header('Média de Temperatura por Dispositivo')
    df_avg = load_data('avg_temp_por_dispositivo')
    fig1 = px.bar(df_avg, x='device_id', y='avg_temp', color='avg_temp')
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico 2: Leituras por Hora
    st.header('Leituras por Hora do Dia')
    df_hora = load_data('leituras_por_hora')
    fig2 = px.line(df_hora, x='hora', y='contagem')
    st.plotly_chart(fig2, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}. Certifique-se de que as Views SQL foram criadas.")