📝 AI-Powered Blogging Platform API
![alt text](https://github.com/budanovia/blog-api/actions/workflows/python-app.yml/badge.svg)

![alt text](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)

![alt text](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)

![alt text](https://img.shields.io/badge/Redis-DC382D?style=flat&logo=redis&logoColor=white)

![alt text](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
A high-performance, asynchronous backend system built with FastAPI. This platform features automated content classification via OpenAI, multi-level caching with Redis, and a fully containerized deployment pipeline.
🚀 Core Architecture
Asynchronous Processing: Utilizes async/await for database operations and external API calls (OpenAI).
Smart Caching: Implements a Cache-Aside pattern with Redis to reduce PostgreSQL read latency for popular articles.
AI Integration: Automatically generates semantic tags for articles using GPT-3.5 based on content analysis.
Security: OAuth2 with JWT Bearer tokens and password hashing via Bcrypt.
DevOps Ready: Nginx reverse proxy, Docker orchestration, and GitHub Actions CI/CD.
🛠️ Tech Stack
Component	Technology
Framework	FastAPI (Python 3.10)
Database	PostgreSQL + SQLAlchemy ORM
Caching	Redis
Migrations	Alembic
Proxy/Server	Nginx + Gunicorn/Uvicorn
AI SDK	OpenAI (Asynchronous)
Validation	Pydantic v2
📂 Project Structure
code
Bash
├── alembic/           # Database migrations
├── nginx/             # Reverse proxy config
├── routers/           # API Route controllers
│   ├── article.py     # Caching logic & AI tagging
│   ├── auth.py        # JWT authentication
│   └── user.py        # User management
├── tests/             # Pytest suite (Integration/Unit)
├── models.py          # SQLAlchemy Relationship models
├── schemas.py         # Pydantic data validation
├── oauth2.py          # Authentication middleware
└── docker-compose.yml # Multi-container setup
⚡ Quick Start (Docker)
Clone & Env Setup
code
Bash
git clone https://github.com/budanovia/blog-api.git
cd blog-api
touch .env # Populate with variables from config.py
Run with Docker Compose
code
Bash
docker-compose up --build
The API will be available at http://localhost:8000 with auto-generated docs at /docs.
🔍 Key Logic Highlights
AI Auto-Tagging (utils.py)
When a user posts an article, the system sends the content to OpenAI's API to generate a list of strings, which are then mapped to the Many-to-Many Tag model in the database.
Redis Cache Implementation (article.py)
code
Python
# Pseudo-logic implemented in the Article router:
cached_data = redis_client.get(f"article_id:{id}")
if cached_data:
    return json.loads(cached_data)

article = db.query(models.Article).filter(id).first()
redis_client.setex(cache_key, 600, article_json) # 10 min TTL
Database Relationships
User ↔ Article: One-to-Many
Article ↔ Tag: Many-to-Many (via article_tag association table)
🧪 CI/CD & Testing
The project includes a robust testing suite that creates a temporary PostgreSQL database for every test run to ensure isolation.
Tools: pytest, httpx, TestClient
Automation: GitHub Actions runs flake8 for linting and pytest on every pull request to main.
