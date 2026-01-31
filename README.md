# 🩺 Tech Challenge – Previsor de Obesidade com Machine Learning

Este repositório contém um *projeto completo* de Machine Learning que usa **regressão logística**, Docker e Streamlit para criar um modelo que **auxilia equipes médicas a diagnosticar e prever níveis de obesidade em pacientes** com base em características clínicas e de estilo de vida.

---

## 🚀 Visão Geral

O objetivo deste projeto é criar um sistema interativo, simples de usar e **portátil** para prever o risco de obesidade com base em dados de pacientes. O modelo é servido por uma interface web construída com **Streamlit** e containerizada com **Docker** para facilitar sua execução em qualquer ambiente.

O aplicativo:

- ✅ Recebe informações do paciente  
- ✅ Exibe a previsão de obesidade e seu nível estimado  
- ✅ Foi empacotado com Docker para fácil execução  

---

## 📌 Funcionalidades

- ✔ Modelo de **Regressão Logística** treinado com dados clínicos  
- ✔ **Aplicação web interativa** com Streamlit  
- ✔ **Container Docker** para execução local ou em produção  
- ✔ Interface simples para visualização de previsões  

---

## 🗂 Estrutura do Projeto

```bash
Tech_Challenge_Obesidade/
├── api/                      # Código da API de predição (Flask)
├── app/                      # Código principal do Streamlit
├── data/                     # Dados e/ou artefatos do modelo
├── docker/                   # Configurações Docker
├── src/                      # Código fonte do modelo
├── docker-compose.yml        # Orquestração dos containers
└── start.ps1                 # Scripts auxiliares (Windows) ```

---
## 🧩 Tecnologias Utilizadas

- Python  
- Scikit-Learn  
- Pandas  
- NumPy  
- Streamlit  
- Flask (API)  
- Docker  
- Docker Compose  

---

## 🛠️ Como Executar o Projeto

### 🐳 Executando com Docker

**Pré-requisitos:** Docker e Docker Compose instalados

```bash
# Clonar o repositório
git clone https://github.com/CorsiIsa/Tech_Challenge_Obesidade.git
cd Tech_Challenge_Obesidade

# Build dos containers
docker compose build

# Subir a aplicação
docker compose up

# Após iniciar
acesse no navegador http://localhost:8501
