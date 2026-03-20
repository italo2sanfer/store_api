# Store API — FastAPI + Cloud Run + Cloud SQL (PostgreSQL)
A lightweight and production‑ready REST API for managing **Products** and **Suppliers**, built with **FastAPI**, deployed on **Google Cloud Run**, and backed by **Cloud SQL (PostgreSQL)**.

This project is designed as a **public demonstration** of cloud deployment, API design, security practices, and CI/CD automation.

## Features
- Fast and typed REST API using **FastAPI**
- Database persistence with **SQLAlchemy + PostgreSQL**
- Fully containerized with **Docker**
- Automatic deployment via **Cloud Build Trigger** on every push to `main`
- Hosted on **Google Cloud Run** with automatic scaling
- Secure connection to **Cloud SQL** using IAM authentication
- Public documentation available at `/docs` (Swagger UI)
- **Rate limiting** for abuse protection (SlowAPI)
- **API Key protection** for write operations (POST, PUT, DELETE)
- Database populated with **fictional demo data only**

## Security Architecture
This demo API is publicly accessible, but it follows several important security measures:

### **1. Cloud SQL IAM Authentication**
The PostgreSQL instance does **not** accept username/password logins.   Only authenticated Google Cloud identities can generate valid connection tokens. This means:
- The database **cannot** be accessed directly from the internet; 
- Only Cloud Run (and authorized IAM identities) can connect.

### **2. API Key for Write Operations**
To prevent unauthorized modifications, all write endpoints require a valid API Key:
```
x-api-key: <your_token>
```
Read endpoints (`GET`) remain public for demonstration purposes.

### **3. Rate Limiting**
To avoid abuse and unnecessary Cloud Run/SQL costs:
- Read endpoints: **100 requests/minute per IP**
- Write endpoints: **20 requests/minute per IP**

### **4. Demo‑Only Data**
The database contains **no real or sensitive information**.

All records are fictional and created exclusively for demonstration.

## API Documentation
Once deployed, the API exposes interactive documentation:
```
/docs      → Swagger UI
/openapi.json → OpenAPI schema
```
## Tech Stack
- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL (Cloud SQL)**
- **Docker**
- **Google Cloud Run**
- **Google Cloud Build (CI/CD)**
- **SlowAPI (rate limiting)**

# ☁️ Deployment (Google Cloud)
This project is deployed using:
- Cloud Build Trigger: Automatically builds and deploys the container on every push to main.
- Cloud Run: Stateless, autoscaling, secure execution environment.
- Cloud SQL: Connected via IAM authentication and Cloud SQL Auth Proxy
- Secrets (such as API_KEY) are stored in Secret Manager and injected into Cloud Run as environment variables.

## Demo Purpose
This project is intentionally designed as a public demo for:
- Cloud architecture
- API design
- Deployment pipelines
- Security best practices
- Containerization
- Database integration
- All data is fictional, and the environment is isolated from any production systems.