from pydantic import BaseModel
from typing import List

class StressData(BaseModel):
    user_id: int
    stress_level: int
    timestamp: str

class PredictionInput(BaseModel):
    age: int
    sleep_hours: float
    work_pressure: float
    anxiety_level: float
    heart_rate: int
    exercise_hours: float
    diet_quality: float
    smoking: int
    alcohol: float

class MultiplePredictionInput(BaseModel):
    inputs: List[PredictionInput]
