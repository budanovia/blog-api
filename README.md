Blogging Platform API

A production-ready, asynchronous REST API built with FastAPI. This platform allows users to manage articles and uses OpenAI’s GPT-3.5 to automatically generate relevant content tags. The architecture is fully containerized and includes a multi-layer caching strategy and CI/CD integration.
![alt text](https://github.com/budanovia/blog-api/actions/workflows/python-app.yml/badge.svg)

Key Features
AI Auto-Tagging: Leverages OpenAI API to analyze article content and automatically generate categorized tags upon creation.
Advanced Caching: Implements Redis to cache article data, significantly reducing database load and improving read latency.
Complex Data Modeling: Managed via SQLAlchemy with support for One-to-Many (User-Article) and Many-to-Many (Article-Tag) relationships.
Secure Authentication: OAuth2 with JWT (JSON Web Tokens) and password hashing using Bcrypt.
Database Migrations: Version-controlled schema changes using Alembic.
Reverse Proxy: Integrated NGINX configuration for load balancing and request routing.
Automated Testing: Comprehensive test suite using Pytest with dependency overrides for a dedicated testing database.
CI/CD: GitHub Actions pipeline configured for automated linting (Flake8) and unit testing on every push.

Tech Stack
Framework: FastAPI (Python 3.10+)
Database: PostgreSQL
ORM: SQLAlchemy
Caching: Redis
Task Handling: Asynchronous Python (Async/Await)
AI Integration: OpenAI SDK
Infrastructure: Docker, Docker Compose, NGINX
Testing: Pytest

Project Structure
code
Text
├── alembic/            # Database migration scripts
├── nginx/              # Nginx reverse proxy configuration
├── routers/            # API endpoints (Articles, Users, Auth, Tags)
├── tests/              # Pytest suite & conftest configuration
├── config.py           # Pydantic-based environment settings
├── database.py         # SQLAlchemy engine and session setup
├── models.py           # SQLAlchemy database models
├── schemas.py          # Pydantic models for data validation
├── oauth2.py           # JWT authentication logic
├── utils.py            # Password hashing & OpenAI integration
└── docker-compose.yml  # Multi-container orchestration

Installation & Setup
Prerequisites
Docker & Docker Compose
OpenAI API Key
1. Clone the repository
code
Bash
git clone https://github.com/budanovia/blog-api.git
cd blog-api
2. Configure Environment Variables
Create a .env file in the root directory and populate it based on config.py:
code
Env
DATABASE_HOSTNAME=db
DATABASE_PORT=5432
DATABASE_PASSWORD=your_password
DATABASE_NAME=postgres
DATABASE_USERNAME=postgres
SECRET_KEY=your_jwt_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPEN_API_KEY=your_openai_api_key
3. Spin up the containers
code
Bash
docker-compose up --build
The API will be available at http://localhost:8000 (or http://localhost:80 through Nginx).

Testing
The project uses pytest with a separate test database to ensure data integrity.
code
Bash
# Run tests locally
pytest

API Documentation
Once the server is running, you can explore the interactive API documentation:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

Security & Optimization
Background Logic: Tags are generated asynchronously to prevent blocking the main thread during article creation.
Data Integrity: Foreign key constraints and ON DELETE CASCADE are utilized to maintain a clean relational state.
Caching Strategy: Article lookups first check Redis; on a cache miss, the API queries PostgreSQL and populates the cache with a 10-minute TTL.
Developed by [Your Name] as a demonstration of modern backend architectural patterns.
