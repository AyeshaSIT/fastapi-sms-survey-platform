# FastAPI Project Bootstrap Guide

A reusable professional setup checklist for all backend/AI FastAPI projects.

---

# 1. Install Required Tools

## Python

Recommended:

* Python 3.12 or latest depending on project requirements

Keep newer Python versions installed if needed.

Verify installed versions:

```bash
py -0
```

---

## Install uv

Official Docs:
[https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

Verify:

```bash
uv --version
```

---

## Install Docker Desktop

[https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Verify:

```bash
docker --version
```

---

## Install VS Code Extensions

Recommended:

* Python
* Pylance
* Ruff
* Docker

---

# 2. Create Project Folder

```bash
mkdir my-project
cd my-project
```

---

# 3. Initialize Git

```bash
git init
```

Create GitHub repository early.

Recommended commit style:

```bash
git commit -m "initialize project structure"
```

---

# 4. Initialize uv Project

Use Python 3.12:

```bash
uv init --python 3.12
```

This creates:

```text
README.md
pyproject.toml
.python-version
main.py
```

---

# 5. Create Virtual Environment

```bash
uv venv --python 3.12
```

This creates:

```text
.venv/
```

Why we use it:

* isolates dependencies
* prevents conflicts
* industry standard
* reproducible environments

---

# 6. Activate Virtual Environment

## Windows CMD

```bash
.venv\Scripts\activate
```

## PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Verify:

```bash
python --version
```

Expected:

```text
Python 3.12.x
```

---

# 7. Install Initial Dependencies

## Core FastAPI

```bash
uv add fastapi uvicorn
```

---

## Development Dependencies

```bash
uv add --dev ruff pytest
```

---

## Database Dependencies

```bash
uv add sqlalchemy asyncpg alembic psycopg[binary]
```

---

## Environment Variables

```bash
uv add pydantic-settings python-dotenv
```

---

# 8. Recommended Project Structure

```text
project-name/
├── .venv/
├── .git/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── integrations/
│   ├── workers/
│   └── main.py
│
├── tests/
├── alembic/
├── docker/
├── .env
├── .gitignore
├── docker-compose.yml
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 9. Create .gitignore

Recommended:

```gitignore
.venv/
__pycache__/
.pytest_cache/
.env
.idea/
.vscode/
*.pyc
```

---

# 10. Run FastAPI Server

```bash
uv run uvicorn app.main:app --reload
```

API Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 11. Recommended Architecture Principles

## Follow Thin Controllers

* routes should stay small
* business logic belongs in services

---

## Use Dependency Injection

* use FastAPI Depends properly
* avoid global state

---

## Use Async Everywhere

Recommended:

* async routes
* async SQLAlchemy
* async external API calls

---

## Keep Clear Separation

### API Layer

Handles HTTP only.

### Service Layer

Business logic.

### Repository Layer

Database access.

### Integrations Layer

External services.

---

# 12. Recommended Development Flow

## Start Feature

```bash
git checkout -b feature/authentication
```

---

## Commit Frequently

```bash
git add .
git commit -m "implement JWT authentication"
```

---

## Push To GitHub

```bash
git push origin feature/authentication
```

---

# 13. Docker Workflow

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Stop:

```bash
docker compose down
```

---

# 14. Production Practices

Always include:

* Docker
* environment variables
* README
* API docs
* tests
* clean commits
* architecture diagrams
* deployment instructions

---

# 15. README Template Sections

Every project should include:

```text
# Project Name

## Features
## Tech Stack
## Architecture
## Setup Instructions
## API Endpoints
## Docker Setup
## Environment Variables
## Future Improvements
```

---

# 16. Portfolio Rules

Avoid:

* tutorial clones
* messy structure
* no README
* no deployment
* no Docker

Build:

* business-focused systems
* scalable backends
* AI integrations
* production-ready APIs

---

# 17. Recommended Backend Stack

| Area             | Recommendation       |
| ---------------- | -------------------- |
| Framework        | FastAPI              |
| ORM              | SQLAlchemy 2.0 Async |
| Database         | PostgreSQL           |
| Queue            | Celery               |
| Broker           | Redis                |
| Auth             | JWT                  |
| Config           | pydantic-settings    |
| Testing          | Pytest               |
| Linting          | Ruff                 |
| Containerization | Docker               |
| Cloud            | AWS                  |

---

# 18. General Learning Roadmap

## Beginner Foundation

* FastAPI basics
* routing
* dependency injection
* SQLAlchemy
* Docker

---

## Intermediate Backend

* JWT auth
* async architecture
* Alembic migrations
* Redis
* Celery
* caching

---

## Advanced Backend

* distributed systems
* scaling workers
* observability
* retries
* rate limiting
* microservices

---

## AI Engineering

* OpenAI APIs
* embeddings
* RAG systems
* vector databases
* AI agents
* async AI workflows

---

# Final Advice

Build fewer projects.

But make them:

* polished
* deployed
* documented
* scalable
* production-ready

Three excellent backend systems are better than ten unfinished tutorial projects.
