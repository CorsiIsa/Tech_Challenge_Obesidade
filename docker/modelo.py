# ============================================
# Importando bibliotecas
# ============================================

import pandas as pd
import numpy as np
from pathlib import Path

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import pickle
import os

# ============================================
# Leitura do dataset
# ============================================

# Aqui realizamos a leitura do dataset utilizado no modelo
df = pd.read_csv("/data/Obesity.csv")


# Visualização inicial dos dados
print(df.head())
print(df.info())
print(df.describe())

# ============================================
# Separando a variável target das variáveis categóricas e numéricas
# ============================================

X = df.drop(columns=["Obesity"])  
y = df["Obesity"]

# ============================================
# Separação das colunas numéricas e categóricas
# ============================================

num_cols = X.select_dtypes(include=["int64", "float64"]).columns

cat_cols = X.select_dtypes(include=["object", "category", "bool"]).columns

print("Colunas numéricas:", list(num_cols))
print("Colunas categóricas:", list(cat_cols))

# ============================================
# Separação em treino e teste
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Pipeline para variáveis numéricas
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])


# Pipeline para variáveis categóricas
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])


# Aqui unimos os pipelines numérico e categórico
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, num_cols),
    ("cat", categorical_pipeline, cat_cols)
])

# ============================================
# Pipeline que iremos instânciar nosso modelo
# ============================================

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression(max_iter=1000))
])

# ============================================
# Hiperparâmetros
# ============================================

param_grid = {
    "model__C": [0.01, 0.1, 1, 10],
    "model__solver": ["lbfgs"]
}

grid_search = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    scoring="accuracy",
    cv=3,
    n_jobs=-1,
    verbose=2
)

# ============================================
# Treinamento do modelo
# ============================================

grid_search.fit(X_train, y_train)

print("Melhores hiperparâmetros encontrados:")
print(grid_search.best_params_)

# ============================================
# Avaliação do modelo
# ============================================

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("Matriz de Confusão:\n")
print(confusion_matrix(y_test, y_pred))

# ============================================
# Salvando o modelo para deploy
# ============================================

model_path = '/model_data/pipeline.pkl'
os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, 'wb') as f:
    pickle.dump(best_model, f)
print(f"Modelo salvo em {model_path}")
