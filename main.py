from fastapi import FastAPI
from controllers.prediction_controller import router as prediction_router

app = FastAPI()
app.include_router(prediction_router)
