# Blogging Platform API

## Description

A blogging platform API that allows users to create, read, update, and delete blog posts and categories. Users can filter posts by category and author.

## Core Features and Functionality

- User authentication and authorization
- CRUD operations for blog posts and categories
- Filtering posts by category and author

## API Endpoints to Implement

- `POST /api/posts/` - Create a new post
- `GET /api/posts/` - Retrieve a list of posts (with optional filtering by category and author)
- `GET /api/posts/{id}/` - Retrieve a specific post
- `PUT /api/posts/{id}/` - Update a specific post
- `DELETE /api/posts/{id}/` - Delete a specific post
- `POST /api/categories/` - Create a new category
- `GET /api/categories/` - Retrieve a list of categories
- `GET /api/categories/{id}/` - Retrieve a specific category
- `PUT /api/categories/{id}/` - Update a specific category
- `DELETE /api/categories/{id}/` - Delete a specific category

## Tools and Libraries

- Django
- Django REST framework
- PostgreSQL
- Docker
- pytest

## Data Model Design

[ERD Diagram](https://link-to-your-erd-diagram.com)

### Explanation of Data Relationships

- **User**: Represents the users of the platform. Each user can author multiple posts.
- **Post**: Represents the blog posts. Each post is authored by a user and belongs to a category.
- **Category**: Represents the categories to which posts can belong. Each category can have multiple posts.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Access the API at `http://127.0.0.1:8000/`
