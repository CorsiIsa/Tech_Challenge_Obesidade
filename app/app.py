import streamlit as st
import menu, formulario, historico, analise


st.set_page_config(
    page_title="PesoSaudável",
    page_icon="🏥",
    layout="wide"
)

if "pagina" not in st.session_state:
    st.session_state.pagina = "Menu"

with st.sidebar:
    st.markdown("## Navegação")

    if st.button("Menu"):
        st.session_state.pagina = "Menu"

    if st.button("Formulário"):
        st.session_state.pagina = "Formulário"

    if st.button("Histórico"):
        st.session_state.pagina = "Histórico"

    if st.button("Análise"):
        st.session_state.pagina = "Análise"

if st.session_state.pagina == "Menu":
    menu.render()
elif st.session_state.pagina == "Formulário":
    formulario.render()
elif st.session_state.pagina == "Histórico":
    historico.render()
elif st.session_state.pagina == "Análise":
    analise.render()
