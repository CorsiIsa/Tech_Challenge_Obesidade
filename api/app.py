from flask import Flask, request, jsonify, Response, send_file
from pydantic import BaseModel, ValidationError
import pickle
import pandas as pd
import traceback
import os
from datetime import datetime

HISTORY_PATH = "/model_data/history.csv"

app = Flask(__name__)

# ============================================
# Carregar o pipeline do modelo treinado
# ============================================
pipeline_path = '/model_data/pipeline.pkl'
with open(pipeline_path, 'rb') as f:
    pipeline = pickle.load(f)

# ============================================
# Classe para validar as entradas
# ============================================

class InputData(BaseModel):
    Gender: str
    Age: float
    Height: float
    Weight: float
    family_history: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

# ============================================
# Endpoint de predição
# ============================================

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("JSON recebido:", request.get_json())
        input_data = InputData(**request.get_json())

        features = pd.DataFrame([{
                "Gender": input_data.Gender,
                "Age": input_data.Age,
                "Height": input_data.Height,
                "Weight": input_data.Weight,
                "family_history": input_data.family_history,
                "FAVC": input_data.FAVC,
                "FCVC": input_data.FCVC,
                "NCP": input_data.NCP,
                "CAEC": input_data.CAEC,
                "SMOKE": input_data.SMOKE,
                "CH2O": input_data.CH2O,
                "SCC": input_data.SCC,
                "FAF": input_data.FAF,
                "TUE": input_data.TUE,
                "CALC": input_data.CALC,
                "MTRANS": input_data.MTRANS
            }])


        prediction = pipeline.predict(features)

        status_code = 200
        status_message = Response(status=status_code).status

        history_row = request.get_json().copy()
        history_row["prediction"] = prediction
        history_row["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        history_df = pd.DataFrame([history_row])

        # Se já existir, concatena
        if os.path.exists(HISTORY_PATH):
            history_df.to_csv(
                HISTORY_PATH,
                mode="a",
                header=False,
                index=False
            )
        else:
            history_df.to_csv(
                HISTORY_PATH,
                index=False
            )

        return jsonify({
            "status": status_message,
            "data": {
                "prediction": prediction[0]
            }
        }), status_code

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "error": str(e),
            "type": type(e).__name__
        }), 500


@app.route('/history', methods=['GET'])
def history():
    if not os.path.exists(HISTORY_PATH):
        return jsonify({"data": []}), 200

    df = pd.read_csv(HISTORY_PATH)
    return jsonify({
        "data": df.to_dict(orient="records")
    }), 200

@app.route("/history/csv", methods=["GET"])
def history_csv():
    return send_file(
        HISTORY_PATH,
        mimetype="text/csv",
        as_attachment=False
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
