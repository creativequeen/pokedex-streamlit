import streamlit as st
from PIL import Image
from dados import pokemon

st.set_page_config(page_title="Pokédex em Python", layout="wide")
st.title("📘 Pokédex em Python")
st.markdown("Feito com 💙 por Cris, usando Python + Streamlit")

# Filtros
filtro_nome = st.sidebar.text_input("🔍 Buscar por nome")
filtro_tipo = st.sidebar.selectbox("🌈 Filtrar por tipo", ["Todos"] + list(set(p['tipo'][1] for p in pokemon.values())))

# Layout em cards
colunas = st.columns(3)

i = 0
for nome, dados in pokemon.items():
    tipo_nome = dados['tipo'][1]
    if (filtro_nome.lower() in nome.lower()) and (filtro_tipo == "Todos" or filtro_tipo == tipo_nome):
        with colunas[i % 3]:
            st.markdown(f"### {nome}")
            st.image(dados['tipo'][2], width=150)
            st.markdown(f"**Tipo:** {tipo_nome}")
            st.markdown(f"**Habilidades:** {', '.join(dados['habilidades'])}")
            for stat in dados['status']:
                st.markdown(f"- {stat}")
            st.markdown("---")
        i += 1
