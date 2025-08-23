from fastapi import APIRouter
from typing import List
import joblib
import numpy as np
from pydantic_model import MultiplePredictionInput

router = APIRouter()

# Load trained model + scaler
model = joblib.load("rf_model.pkl")
scaler = joblib.load("scaler.pkl")

@router.post("/predict")
def predict(input_data: MultiplePredictionInput):
    try:
        # Convert inputs to NumPy array
        features = np.array([
            [
                data.age,
                data.sleep_hours,
                data.work_pressure,
                data.anxiety_level,
                data.heart_rate,
                data.exercise_hours,
                data.diet_quality,
                data.smoking,
                data.alcohol
            ] for data in input_data.inputs
        ])

        # Scale features
        features = scaler.transform(features)

        # Predict
        predictions = model.predict(features)

        # Human-readable results
        results = ["Not Stressed" if p == 1 else "Stressed" for p in predictions]

        return {"predictions": results}

    except Exception as e:
        return {"error": str(e)}
