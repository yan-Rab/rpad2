from fastapi import APIRouter
from models.student import Student
from services.prediction_service import predict_evasion
from joblib import load

router = APIRouter()

@router.post("/predict")
def predict(student: Student):
    return predict_evasion(student.dict())

@router.get('/')
def health():
    model = load("core/logistic_model.pkl")
    model_loaded = 'false'
    
    if model:
        model_loaded = 'true'
        
    return {
        "status": "ok",
        "model_loaded": model_loaded   
    }
