from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from predict_routes import router as predict_router
import logging

app = FastAPI(title="Stress Detection API")

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
DATABASE_URL = "mysql+pymysql://root:050901@localhost:3306/demo"
try:
    engine = create_engine(DATABASE_URL)
    # Test connection
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    logger.info("✅ Database connected successfully")
except Exception as e:
    logger.error(f"❌ Database connection failed: {e}")
    raise

# Define StressData here itself (no need for separate file)
class StressData(BaseModel):
    user_id: str
    stress_level: float
    timestamp: Optional[datetime] = None

@app.get("/")
def home():
    return {"message": "🚀 API connected successfully with FastAPI + MySQL + ML!"}

@app.get("/data")
def get_data():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM stress_indicators"))
            rows = [dict(row._mapping) for row in result]
        return {"data": rows}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/data")
def insert_data(item: StressData):
    try:
        with engine.connect() as conn:
            query = text(
                "INSERT INTO stress_indicators (user_id, stress_level, timestamp) VALUES (:user_id, :stress_level, :timestamp)"
            )
            conn.execute(query, item.dict())
            conn.commit()
        return {"message": "✅ Data inserted successfully!", "data": item.dict()}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Register ML routes
app.include_router(predict_router)