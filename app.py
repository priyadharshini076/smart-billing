from fastapi import FastAPI
import json

app = FastAPI()
@app.get("/")
def root():
    return {"message": "SmartBillCare backend is running!"}

@app.get("/billing/{patient_id}")
def get_bill(patient_id: str):
    with open("billing_data.json") as f:
        data = json.load(f)
    return data.get(patient_id, {"error": "Patient not found"})
