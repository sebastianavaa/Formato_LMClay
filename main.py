import streamlit as st
from helpers.LMClay import formatearmayor

st.title('Formatear Libro Mayor💣')
año = st.selectbox(
    "Año",
    ("2023", "2024"),
)

empresa = st.text_input("Empresa", "SMART CFO")

if st.button("Formatear", type="primary"):
    st.write("Se descargara el Mayor")

    formatearmayor(año, empresa)