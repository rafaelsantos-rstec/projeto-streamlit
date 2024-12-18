import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome,data_nascimento,tipo_cliente):
    if nome and data_nascimento <= date.today():
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{data_nascimento},{tipo_cliente}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de Clientes",
    page_icon="💾"
)

st.title("Cadastro de Clientes")
st.divider()

nome = st.text_input("Digite o nome do Cliente",
              key="txt_nome_cliente")

dt_nascimento = st.date_input("Selecione a data de Nascimento",
                              key="dtip_nasc",
                              format="DD/MM/YYYY"
                              )

tipo_cliente = st.selectbox("Tipo do Cliente",
                    ["Pessoa Física","Pessoa Jurídica"],
                    key="slb_tipo_cliente"
                    )


btn_cadastrar = st.button("Cadastrar",
                          on_click=gravar_dados,
                          args=[nome, dt_nascimento, tipo_cliente])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com Sucesso",
                   icon="👌")
    else:
        st.error("Erro de gravação de dados",
                 icon="😒")
        