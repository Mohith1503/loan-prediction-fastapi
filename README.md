# Loan Prediction API (FastAPI + Machine Learning)

## 📌 Overview
This project is an end-to-end Loan Prediction System built using Machine Learning and FastAPI.  
It predicts whether a loan will be approved or rejected based on user inputs.

## 🚀 Features
- Machine Learning model (Scikit-learn)
- FastAPI REST API
- Real-time prediction endpoint
- Clean modular structure

## 🛠 Tech Stack
- Python
- FastAPI
- Scikit-learn
- Pandas, NumPy

## 📂 Project Structure
- app/ → API and logic
- model1.pkl → trained ML model
- requirements.txt → dependencies

## ▶️ Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📡 API Endpoint
POST `/predict`

## 💡 Example Output
```json
{
  "loan_status": "Approved"
}
```

## 📌 Author
Mohith Ram Garaga
