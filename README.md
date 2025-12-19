# 📝 Blogging Platform API

[![Python application](https://github.com/budanovia/blog-api/actions/workflows/python-app.yml/badge.svg)](https://github.com/budanovia/blog-api/actions/workflows/python-app.yml)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx)

A production-ready, asynchronous REST API built with **FastAPI**. This system allows users to manage articles with automated semantic tagging via **OpenAI**, high-performance caching via **Redis**, and a fully containerized deployment architecture.

---

### 🚀 Key Features

*   **AI-Driven Auto-Tagging:** Integrates **OpenAI GPT-3.5** to analyze article content and automatically generate categorized tags.
*   **Performance Optimization:** Implements **Redis** caching (Cache-Aside pattern) to reduce PostgreSQL read latency.
*   **Relational Data Modeling:** Managed via **SQLAlchemy** with One-to-Many (Users/Articles) and Many-to-Many (Articles/Tags) relationships.
*   **Security:** Full OAuth2 flow with **JWT (JSON Web Tokens)** and Bcrypt password hashing.
*   **Database Migrations:** Schema versioning and management using **Alembic**.
*   **Infrastructure:** Multi-container orchestration with **Docker Compose** and **NGINX** as a reverse proxy.
*   **CI/CD:** Automated testing and linting (Flake8) via GitHub Actions.

---

### 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Database** | PostgreSQL |
| **Caching** | Redis |
| **ORM** | SQLAlchemy |
| **Migrations** | Alembic |
| **AI SDK** | OpenAI (Async) |
| **Web Server** | Nginx / Uvicorn |
| **Testing** | Pytest |

---

### 📂 Project Structure

```text
├── alembic/            # Database migration scripts
├── nginx/              # Nginx reverse proxy configuration
├── routers/            # API Endpoints (Articles, Users, Auth, Tags)
├── tests/              # Pytest suite & Test configuration
├── config.py           # Pydantic-based environment management
├── database.py         # SQLAlchemy engine setup
├── models.py           # SQLAlchemy relational models
├── schemas.py          # Pydantic data validation
├── oauth2.py           # JWT Authentication logic
└── docker-compose.yml  # Multi-container orchestration
```

---

### ⚡ Installation & Setup (Docker)

The easiest way to run the application is using **Docker Compose**, which spins up the API, PostgreSQL database, and Redis cache automatically.

**1. Clone the repository**
```bash
git clone https://github.com/budanovia/blog-api.git
cd blog-api
```

**2. Configure Environment Variables**
Create a `.env` file in the project root and add your credentials:
```env
DATABASE_HOSTNAME=db
DATABASE_PORT=5432
DATABASE_PASSWORD=your_secure_password
DATABASE_NAME=postgres
DATABASE_USERNAME=postgres
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPEN_API_KEY=your_openai_api_key
```

**3. Run the Application**
```bash
docker-compose up --build
```
The API will be live at `http://localhost:8000`.

---

### 📖 API Documentation

Once the server is running, you can access the interactive documentation to test the endpoints directly from your browser:

*   **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
*   **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

#### **Key Endpoints:**
*   `POST /user/` - Register a new user account.
*   `POST /login/` - Authenticate and receive a JWT Bearer token.
*   `POST /articles/` - Create an article (triggers OpenAI auto-tagging).
*   `GET /articles/{id}` - Retrieve an article (checks Redis cache first).

---

### 🧪 Running Tests

This project uses **Pytest** for automated testing. The test suite includes a specialized `conftest.py` that sets up a clean, isolated PostgreSQL database for every test run to ensure production data remains untouched.

```bash
# To run tests locally
pytest
```

---
*Developed as a demonstration of production-level backend engineering.*
