import pandas as pd
from joblib import load

THRESHOLD = 0.5
model = load("core/logistic_model.pkl")

def predict_evasion(student_dict):
    # Cria DataFrame com 1 linha e as colunas corretas
    X = pd.DataFrame([student_dict])

    # Predição da probabilidade
    prob = model.predict_proba(X)[0][1]

    predicted_class = 1 if prob >= THRESHOLD else 0

    return {
        "prob_evasion": float(prob),
        "predicted_class": predicted_class,
        "threshold": THRESHOLD
    }
