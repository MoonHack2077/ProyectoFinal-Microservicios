# Final Project - Microservices

Cooking recipe management system

## Required Technologies
- **Programming Language**: Python
- **Database**: MySQL
- **Framework**: FastAPI
- **Docker**: For container management

## Important Configurations
### `.env` File
Copy the `.env.example` file and rename it to `.env`. 
Contains the environment variables needed to connect to the database and other services.

## Installation and Setup

1. **Clone the repository**:
   git clone https://github.com/MoonHack2077/ProyectoFinal-Microservicios
   cd ProyectoFinal-Microservicios

2. **Start the database with Docker:**:
   docker compose up --build

4. **Run Pylint for code analysis:**
    -If you haven't installed yet. Create a virtual environment and run:
    pip install pylint

    - Then, to analyze the code:
    pylint FastAPI/app/

5. **Stop the database:**
    docker compose down

6. **Apply migration changes to db tables:**
   -After having the containers up and running, we create a virtual environment by
   installing the dependencies from the `requirements.txt` file.
   We execute the following command inside the /app
   -alembic upgrade head
