FastAPI Starter Project
A production-ready FastAPI project with clean architecture, JWT authentication, role-based authorization, and PostgreSQL.
Setup

Clone the repository:
git clone <repo-url>
cd fastapi_starter


Create and activate virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Set up environment variables:Copy .env.example to .env and update values.

Run PostgreSQL and app with Docker:
docker-compose up --build


Run tests:
pytest



Endpoints

POST /token: Login to get JWT.
POST /users: Create a user.
GET /users: List users (Admin/Management only).
PUT /users/{user_id}: Update a user (Admin only).
DELETE /users/{user_id}: Delete a user (Admin only).

Features

Clean architecture with dependency injection.
JWT authentication and role-based authorization (Admin, Management, User).
Async PostgreSQL with SQLAlchemy.
90%+ test coverage with pytest.
Dockerized for production.
