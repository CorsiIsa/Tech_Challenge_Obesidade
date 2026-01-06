import streamlit as st
import requests

def render():
    st.title("📝 Formulário de Avaliação")

    st.write("Preencha os dados abaixo para avaliação do risco de obesidade.")

    with st.form("form_obesity"):

        # =====================
        # Dados demográficos
        # =====================
        gender = st.selectbox(
            "Sexo biológico",
            options=["Female", "Male"],
            format_func=lambda x: "Feminino" if x == "Female" else "Masculino"
        )

        age = st.number_input(
            "Idade (anos)",
            min_value=14,
            max_value=61,
            step=1
        )

        height = st.number_input(
            "Altura (em metros)",
            min_value=1.40,
            max_value=2.10,
            step=0.01
        )

        weight = st.number_input(
            "Peso (em kg)",
            min_value=30.0,
            max_value=200.0,
            step=0.1
        )

        # =====================
        # Histórico e hábitos
        # =====================
        family_history = st.selectbox(
            "Histórico familiar de excesso de peso",
            options=["yes", "no"],
            format_func=lambda x: "Com histórico" if x == "yes" else "Sem histórico"
        )

        favc = st.selectbox(
            "Consumo frequente de alimentos muito calóricos",
            options=["yes", "no"],
            format_func=lambda x: "Sim" if x == "yes" else "Não"
        )

        fcvc = st.selectbox(
            "Consumo de vegetais",
            options=[1, 2, 3],
            format_func=lambda x: {1: "Raramente", 2: "Às vezes", 3: "Sempre"}[x]
        )

        ncp = st.selectbox(
            "Número de refeições principais por dia",
            options=[1, 2, 3, 4],
            format_func=lambda x: {
                1: "Uma",
                2: "Duas",
                3: "Três",
                4: "Quatro ou mais"
            }[x]
        )

        caec = st.selectbox(
            "Consumo de lanches entre refeições",
            options=["no", "Sometimes", "Frequently", "Always"],
            format_func=lambda x: {
                "no": "Não consome",
                "Sometimes": "Às vezes",
                "Frequently": "Frequentemente",
                "Always": "Sempre"
            }[x]
        )

        smoke = st.selectbox(
            "Fuma?",
            options=["yes", "no"],
            format_func=lambda x: "Sim" if x == "yes" else "Não"
        )

        ch2o = st.selectbox(
            "Consumo diário de água",
            options=[1, 2, 3],
            format_func=lambda x: {
                1: "< 1L/dia",
                2: "1–2L/dia",
                3: "> 2L/dia"
            }[x]
        )

        scc = st.selectbox(
            "Monitora ingestão calórica?",
            options=["yes", "no"],
            format_func=lambda x: "Sim" if x == "yes" else "Não"
        )

        faf = st.selectbox(
            "Atividade física semanal",
            options=[0, 1, 2, 3],
            format_func=lambda x: {
                0: "Nenhuma",
                1: "1–2x/sem",
                2: "3–4x/sem",
                3: "5x ou mais"
            }[x]
        )

        tue = st.selectbox(
            "Tempo em telas por dia",
            options=[0, 1, 2],
            format_func=lambda x: {
                0: "0–2h",
                1: "3–5h",
                2: ">5h"
            }[x]
        )

        calc = st.selectbox(
            "Consumo de bebida alcoólica",
            options=["no", "Sometimes", "Frequently", "Always"],
            format_func=lambda x: {
                "no": "Não bebe",
                "Sometimes": "Às vezes",
                "Frequently": "Frequentemente",
                "Always": "Sempre"
            }[x]
        )

        mtrans = st.selectbox(
            "Meio de transporte habitual",
            options=[
                "Automobile",
                "Motorbike",
                "Bike",
                "Public_Transportation",
                "Walking"
            ],
            format_func=lambda x: {
                "Automobile": "Carro",
                "Motorbike": "Moto",
                "Bike": "Bicicleta",
                "Public_Transportation": "Transporte Público",
                "Walking": "A pé"
            }[x]
        )

        submitted = st.form_submit_button("Enviar")

    # =====================
    # Resultado (por enquanto)
    # =====================
    if submitted:
        dados = {
            "Gender": gender,
            "Age": float(age),
            "Height": float(height),
            "Weight": float(weight),
            "family_history": family_history,
            "FAVC": favc.lower(),
            "FCVC": float(fcvc),
            "NCP": float(ncp),
            "CAEC": caec,
            "SMOKE": smoke.lower(),
            "CH2O": float(ch2o),
            "SCC": scc.lower(),
            "FAF": float(faf),
            "TUE": float(tue),
            "CALC": calc,
            "MTRANS": mtrans
        }



        response = requests.post("http://api:5000/predict", json=dados)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Classificação prevista: {result['data']['prediction']}")
        else:
            st.error("Erro ao realizar a predição. Verifique os valores de entrada.")
