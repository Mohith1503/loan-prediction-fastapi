from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from app.schema import InputData
from app.predictor import make_prediction
import pickle
app= FastAPI()



@app.post("/predict")
def predict(data:InputData):
    result = make_prediction(data)
   
    return {
        "loan_status": "Approved" if result == 1 else "Rejected"
         
    }
    