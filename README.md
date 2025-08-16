# FastAPI Starter Project 🚀
A production-ready FastAPI project showcasing clean architecture, JWT authentication, role-based authorization, and PostgreSQL integration. Built with best practices, this project is ideal for scalable, enterprise-grade applications and serves as a strong portfolio piece for senior Python developer roles.

## 🎯 Features

- **Clean Architecture**: Modular design with separated layers (routers, services, repositories) for maintainability and scalability.
- **JWT Authentication**: Secure endpoints with JSON Web Tokens, including login and token generation.
- **Role-Based Authorization**: Restricts access based on roles (Admin, Management, User).
- **Async PostgreSQL**: Leverages SQLAlchemy with async support for high-performance database operations.
- **Dependency Injection**: Uses FastAPI’s Depends for clean, reusable dependencies.
- **Pydantic Validation**: Ensures robust request/response validation.
- **Unit Tests**: Achieves 90%+ coverage with pytest and pytest-asyncio.
- **Dockerized**: Ready for production with Docker and docker-compose.
- **VSCode Ready**: Configured with virtual environment and debugging support.

## 🛠️ Tech Stack

- **FastAPI**: High-performance web framework for building APIs.
- **PostgreSQL**: Relational database with async support via asyncpg.
- **SQLAlchemy**: ORM for database interactions.
- **Pydantic**: Data validation and serialization.
- **python-jose & passlib**: JWT authentication and password hashing.
- **pytest**: Comprehensive unit testing.
- **Docker**: Containerized deployment.

## 📋 Prerequisites

- Python 3.11+
- Docker and Docker Compose
- PostgreSQL
- VSCode (recommended for development)

## 🚀 Getting Started
### 1. Clone the Repository
````bash
git clone https://github.com/faojul/fastapi-starter-clean-architecture.git
cd fastapi-starter-clean-architecture
````
### 2. Set Up Virtual Environment
````bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
````
### 3. Install Dependencies
````bash
pip install -r requirements.txt
````
### 4. Configure Environment Variables
Copy .env.example to .env and update the values:
````bash
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/fastapi_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
````
### 5. Run with Docker
````bash
docker-compose up --build
````
The app will be available at http://localhost:8000. Access the interactive API docs at http://localhost:8000/swagger.
### 6. Run Tests
````bash
pytest
````
## 🔗 API Endpoints

| Method  | Endpoint            | Description                    | Access                |
|---------|---------------------|--------------------------------|-----------------------|
| `POST`  | `/token`            | Generate JWT token             | Public                |
| `POST`  | `/users`            | Create a new user              | Public                |
| `GET`   | `/users`            | List users (paginated)         | Admin, Management     |
| `PUT`   | `/users/{user_id}`  | Update a user                  | Admin                 |
| `DELETE`| `/users/{user_id}`  | Delete a user                  | Admin                 |


## 🧪 Testing
The project includes comprehensive unit tests with pytest and pytest-asyncio, achieving 90%+ coverage. Tests cover:

User creation, login, and CRUD operations.
Role-based authorization checks.
JWT token generation and validation.

Run tests with:
pytest

## 🐳 Docker Setup
The project is fully Dockerized for easy deployment:

FastAPI App: Runs on port 8000.
PostgreSQL: Configured with persistent storage.

Start the app and database:
docker-compose up --build

## 🖥️ VSCode Configuration
The project includes VSCode settings for a seamless development experience:

- Virtual environment integration (.venv).
- Code formatting with Black.
- Debugging support for FastAPI with Uvicorn.

## 🏗️ Project Structure
fastapi_starter/
├── app/
│   ├── api/              # API routes and dependencies
│   ├── core/             # Configuration and security utilities
│   ├── models/           # SQLAlchemy models
│   ├── schemas/          # Pydantic schemas
│   ├── services/         # Business logic
│   ├── repositories/     # Database operations
│   └── main.py           # FastAPI app entry point
├── tests/                # Unit tests with pytest
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose setup
├── requirements.txt      # Python dependencies
└── .vscode/              # VSCode settings and debugging

## 🔮 Future Plans
To make this project even more robust, the following enhancements are planned:

Role Management Endpoints: Add CRUD operations for dynamic role management (e.g., create, update, delete roles), restricted to Admin users.
Structured Logging: Integrate Python’s logging module for detailed request tracking and debugging across all layers.
Database Migrations: Implement Alembic for version-controlled schema migrations, ensuring smooth database evolution in production.

## 🌟 Why This Project?
This project demonstrates senior-level Python skills with:

- Clean, modular architecture inspired by Domain-Driven Design.
- Production-ready features like JWT, async database operations, and Docker.
- High test coverage for reliability.
- Best practices for scalability and maintainability.

Perfect for showcasing to recruiters at remote-first companies like Doist, Toggl, or similar.

## 📄 License
MIT License. See LICENSE for details.

## 🤝 Contributing
Contributions are welcome! Please open an issue or pull request for suggestions or improvements.

Built with ❤️ by [faojul](linkedin.com/in/faojul-ahsan)
