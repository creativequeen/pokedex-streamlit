import streamlit as st
from dados import pokemon
from PIL import Image

st.set_page_config(page_title="Pokédex", layout="wide")
st.title("📱 Pokédex em Python com Streamlit")

busca = st.text_input("🔍 Buscar Pokémon por nome ou tipo:")

colunas = st.columns(3)

for i, (nome, info) in enumerate(pokemon.items()):
    if busca.lower() in nome.lower() or busca.lower() in info["tipo"][1].lower():
        with colunas[i % 3]:
            st.markdown(f"### {nome}")
            st.image(info["tipo"][2], width=150)
            st.markdown(f"**Tipo:** {info['tipo'][1]}")
            st.markdown(f"**Habilidades:** {', '.join(info['habilidades'])}")
            st.markdown(f"**Status:**")
            for status in info["status"]:
                st.markdown(f"- {status}")
