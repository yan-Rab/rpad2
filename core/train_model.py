import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

df = pd.read_csv("students.csv")

# ==========================
# 2. Separar X e y
# ==========================
X = df.drop("evaded", axis=1)
y = df["evaded"]

# ==========================
# 3. Definir tipos de colunas
# ==========================
categorical_cols = ["gender", "high_school_type"]
boolean_cols = ["works", "scholarship_holder"]
numeric_cols = [
    "age",
    "enem_score",
    "family_income",
    "weekly_work_hours",
    "first_semester_failures",
    "distance_to_campus_km"
]

# ==========================
# 4. Pré-processamento
# ==========================
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("bool", "passthrough", boolean_cols),  # já são 0/1
        ("num", "passthrough", numeric_cols)
    ]
)

# ==========================
# 5. Criar pipeline final
# ==========================
model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("logreg", LogisticRegression(max_iter=1000))
    ]
)

# ==========================
# 6. Dividir treino/teste
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================
# 7. Treinar
# ==========================
model.fit(X_train, y_train)

# ==========================
# 8. Avaliar
# ==========================
preds = model.predict(X_test)
print(classification_report(y_test, preds))

# ==========================
# 9. Salvar modelo
# ==========================
joblib.dump(model, "logistic_model.pkl")
print("Modelo salvo como logistic_model.pkl")
