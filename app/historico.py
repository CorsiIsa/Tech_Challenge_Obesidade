import streamlit as st
import requests
import pandas as pd

API_URL = "http://api:5000"

def render():
    st.title("📊 Histórico de Avaliações")

    response = requests.get(f"{API_URL}/history")

    if response.status_code == 200:
        data = response.json()["data"]

        if not data:
            st.info("Nenhuma avaliação realizada ainda.")
            return

        df = pd.DataFrame(data)

        st.dataframe(df, use_container_width=True)
    else:
        st.error("Erro ao carregar histórico")
