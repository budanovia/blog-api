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
