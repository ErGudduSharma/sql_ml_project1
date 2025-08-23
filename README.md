🧠 # Student Stress Analysis & Prediction (SQL + ML + FastAPI)
📌 ## Overview

This project aims to analyze and predict student stress levels using Machine Learning integrated with SQL Database and deployed via FastAPI. The project includes data preprocessing, model training, API development, and testing.

🚀 ## Project Workflow

1️⃣ Project Setup

Created a project folder in VS Code.
Set up a virtual environment:

python -m venv .venv

Activated the environment:
.venv\Scripts\activate

Created requirements.txt with all dependencies:

numpy
pandas
matplotlib
scikit-learn
sqlalchemy
pymysql
jupyter
fastapi
uvicorn
joblib
pydantic

2️⃣ Database Setup

Connected VS Code with SQL Database using:
SQL Tools Extension
MariaDB Driver

Created 2–3 tables inside the database containing student stress data.

Data was related to student stress analysis and prediction.

3️⃣ Machine Learning Pipeline (ml_pipeline.ipynb)

Imported data from SQL.
Found that data was highly imbalanced → used SMOTE to balance it.
Handled overfitting issue by applying techniques like:
Regularization
Proper train-test split
Trained ML Model (Random Forest).

Saved artifacts:

rf_model.pkl (Trained model)
scaler.pkl (Scaler object)

4️⃣ FastAPI Development

Built API using FastAPI (app.py, main.py).
Created Pydantic model (pydantic_model.py) for input validation.
Implemented prediction route (predict_routes.py) to load model & return predictions.
API successfully tested with Postman:
✅ 200 OK response received

Predictions returned for given student input data

5️⃣ API Testing

Used Postman to send input JSON requests.

Input:

{
  "inputs": [
    {
      "age": 25,
      "sleep_hours": 6.5,
      "work_pressure": 8.0,
      "anxiety_level": 7.0,
      "heart_rate": 90,
      "exercise_hours": 1.0,
      "diet_quality": 6.0,
      "smoking": 0,
      "alcohol": 2.5
    },
    {
      "age": 30,
      "sleep_hours": 9.0,
      "work_pressure": 2.0,
      "anxiety_level": 1.0,
      "heart_rate": 65,
      "exercise_hours": 3.0,
      "diet_quality": 9.0,
      "smoking": 0,
      "alcohol": 0.0
    }
  ]
}

Output:

{"predictions":["Stressed","Not Stressed"]}



🛠️ Files in Project

ml_pipeline.ipynb   → ML training notebook
pydantic_model.py   → Input validation schema
predict_routes.py   → API routes for prediction
app.py              → FastAPI app instance
main.py             → Entry point to run app
requirements.txt    → Dependencies
scaler.pkl          → Saved scaler
rf_model.pkl        → Saved RandomForest model
steps.txt           → Project steps

▶️ Run the Project

1. Start FastAPI server
uvicorn main:app --reload

2. Test in Browser
Open:

http://127.0.0.1:8000/docs

3. Test with Postman
Choose POST request

Endpoint:

http://127.0.0.1:8000/predict


Send JSON body → Get stress prediction

✅ Features

SQL Database Integration

Machine Learning Pipeline with SMOTE

Random Forest Model

FastAPI REST API

Postman Testing