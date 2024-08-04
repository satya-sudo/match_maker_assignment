# Marriage Matchmaking App

## Description

The Marriage Matchmaking App is a backend application built with FastAPI. It allows users to create, read, update, and delete profiles. Profiles include details such as name, age, gender, email, city, and interests.

## Features

- **Create** user profiles
- **Read** all user profiles or a specific profile by ID
- **Update** user profiles
- **Delete** user profiles
- **Find Matches** based on city and interests
- **Email Validation** to ensure valid email addresses

## Setup

1. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Initialize the database:**

    ```sh
    python start_db.py
    ```

4. **add dummy data (optional)**

    ```sh
    python create_dummy_data.py
    ```

5. **Run the FastAPI application:**

    ```sh
    uvicorn main:app --reload
    ```

6. **Access the application:**

    - **API Documentation (Swagger UI):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - **API Documentation (Redoc):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints

- **POST /users/**: Create a new user
- **GET /users/**: Read all users
- **GET /users/{user_id}**: Read a user by ID
- **PUT /users/{user_id}**: Update a user by ID
- **DELETE /users/{user_id}**: Delete a user by ID
- **GET /users/{user_id}/matches**: Find potential matches for a user
