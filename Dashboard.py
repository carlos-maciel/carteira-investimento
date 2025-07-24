import yfinance as yf
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import datetime

st.title("INVESTIMENTOS :bar_chart:")

renda_fixa=['IDKA11.SA', 'JURO11.SA']
fii=['XFIX11.SA', 'RVBI11.SA']
acoes=['VALE3.SA', 'BBSE3.SA', 'BBAS3.SA', 'SAPR11.SA', 'CASH3.SA', 'BOVV11.SA']
internacional=['USDB11.SA', 'WRLD11.SA']
cripto=['BTC-USD', 'XRP-USD', 'ETH-USD']
ibovespa = ['^BVSP']

data_final = datetime.date.today()
data_inicial = data_final - datetime.timedelta(days=90)

# Converta para string no formato esperado pelo yfinance
data_inicial = data_inicial.strftime('%Y-%m-%d')
data_final = data_final.strftime('%Y-%m-%d')

df_renda_fixa = yf.download(renda_fixa, data_inicial, data_final)['Close']
df_fii = yf.download(fii, data_inicial, data_final)['Close']
df_acoes = yf.download(acoes, data_inicial, data_final)['Close']
df_internacional = yf.download(internacional, data_inicial, data_final)['Close']
df_cripto = yf.download(cripto, data_inicial, data_final)['Close']
df_ibovespa = yf.download(ibovespa, data_inicial, data_final)['Close']

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Ibovespa", "Renda Fixa", "FII", "Ações", "Internacional", "Cripto"])

with tab1:
    st.subheader("Ibovespa")
    fig = px.line(df_ibovespa)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Renda Fixa")
    fig = px.line(df_renda_fixa)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("FII")
    fig = px.line(df_fii)
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("Ações")
    fig = px.line(df_acoes)
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.subheader("Internacional")
    fig = px.line(df_internacional)
    st.plotly_chart(fig, use_container_width=True)

with tab6:
    st.subheader("Cripto")
    fig = px.line(df_cripto)
    st.plotly_chart(fig, use_container_width=True)
