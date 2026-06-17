# 🚀 Production-Ready Loan Prediction API with MLOps

> A production-ready Machine Learning API that predicts loan approval outcomes in real time and demonstrates the complete MLOps lifecycle—from model serving with FastAPI to automated CI/CD deployment on AWS EC2.

---

# 📖 Overview

This project goes beyond a notebook experiment by taking a loan approval classifier from training to a live, production-style API.

It demonstrates how a Machine Learning model can be served, containerized, automatically built, and deployed to the cloud with a fully automated CI/CD pipeline.

Given applicant information such as income, marital status, and credit history, the API predicts whether a loan application is likely to be approved.

---

# ✨ Key Features

| Category            | Description                                                     |
| ------------------- | --------------------------------------------------------------- |
| 🤖 Machine Learning | Scikit-learn model for loan approval prediction                 |
| 🚀 API              | FastAPI REST API with interactive Swagger UI                    |
| ✅ Validation        | Request and response validation using Pydantic                  |
| 🐳 Containerization | Dockerized application                                          |
| ⚙️ CI/CD            | GitHub Actions pipeline                                         |
| 📦 Docker Hub       | Automatic image build and push                                  |
| ☁️ Cloud Deployment | Automated deployment to AWS EC2                                 |
| 🔐 SSH Automation   | Secure remote deployment                                        |
| 🔄 Reliability      | Running containers are automatically replaced during deployment |

---

# 🏗 Architecture

```
Developer
    │
git push
    ▼
GitHub Repository
    ▼
GitHub Actions
    │
    ├── Validate Application
    ├── Build Docker Image
    ├── Push Image to Docker Hub
    ▼
SSH into AWS EC2
    ▼
Pull Latest Docker Image
    ▼
Stop & Remove Old Container
    ▼
Run Updated Container
    ▼
🚀 Live API
```

---

# 🛠 Tech Stack

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

## Backend

* FastAPI
* Uvicorn
* Pydantic

## MLOps / DevOps

* Docker
* GitHub Actions
* Docker Hub
* AWS EC2
* SSH
* YAML

---

# 📂 Project Structure

```
loan-prediction-fastapi/

├── app/
│   ├── main.py
│   ├── model.py
│   ├── predictor.py
│   └── schema.py
│
├── data/
├── model1.pkl
├── Dockerfile
├── requirements.txt
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Mohith1503/loan-prediction-fastapi.git

cd loan-prediction-fastapi
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Application:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🐳 Run with Docker

## Build

```bash
docker build -t loan-prediction-api .
```

## Run

```bash
docker run -d -p 8000:8000 loan-prediction-api
```

---

# 📡 API Reference

## Home

```
GET /
```

## Swagger UI

```
GET /docs
```

## Prediction Endpoint

```
POST /predict
```

---

# 📥 Sample Request

```json
{
  "Gender": "Male",
  "Married": "Yes",
  "ApplicantIncome": 5000
}
```

---

# 📤 Sample Response

```json
{
  "loan_status": "Approved"
}
```

---

# ⚙️ CI/CD Pipeline

Every push to the **main** branch automatically:

✅ Validates the application

🐳 Builds a Docker image

📦 Pushes the image to Docker Hub

🔐 Connects to AWS EC2 using SSH

⬇️ Pulls the latest image

🔄 Stops and removes the existing container

🚀 Deploys the updated application

No manual deployment steps are required.

---

# ☁️ Deployment

The application is deployed on an AWS EC2 instance inside a Docker container.

A GitHub Actions workflow automates the complete deployment pipeline, ensuring that every push to the main branch updates the live application.

---

# 📚 What This Project Demonstrates

* Building and serving a Machine Learning model through a REST API
* FastAPI and Pydantic for clean API development
* Docker containerization
* CI/CD with GitHub Actions
* Docker Hub integration
* Automated AWS EC2 deployment
* SSH-based deployment automation
* YAML workflow development
* Practical MLOps concepts
* Production-oriented project structure

---

# 🔮 Future Improvements

* Nginx reverse proxy
* Docker Compose
* MLflow integration
* Kubernetes deployment
* Monitoring and logging

---

# 👨‍💻 Author

## Mohith Ram Garaga

GitHub:

https://github.com/Mohith1503

---

# ⭐ Support

If you found this project interesting or helpful for learning MLOps concepts, consider giving it a ⭐.
