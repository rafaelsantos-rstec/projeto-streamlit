import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.title("Cliente Cadastrados")
st.divider()

st.dataframe(dados)