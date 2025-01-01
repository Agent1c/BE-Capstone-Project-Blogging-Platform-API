## Backend_Blue_Print

# Blogging Platform API

## Overview

This project is a Blogging Platform API built using Django and Django REST Framework. The API allows users to manage blog posts by creating, updating, deleting, and viewing posts. It also includes features like categorization and author-based filtering to enhance the blogging experience.

## Features

- **Blog Post Management (CRUD)**: Create, Read, Update, and Delete blog posts.
- **User Management (CRUD)**: Create, Read, Update, and Delete users.
- **View Posts by Category or Author**: Retrieve posts filtered by category or author.
- **Search and Filter Blog Posts**: Search for blog posts by title, content, tags, or author.
- **Authentication**: User authentication using Django’s built-in authentication system and JWT.
- **Pagination and Sorting**: Pagination for blog post listings and sorting options.

## API Endpoints

### Blog Posts

- **Create a Post**: `POST /api/posts/` (requires authentication)
- **Retrieve Posts**: `GET /api/posts/`
  - Optional filtering by category and author: `GET /api/posts/?category={category_id}&author={author_id}`
- **Retrieve a Specific Post**: `GET /api/posts/{id}/`
- **Update a Post**: `PUT /api/posts/{id}/` (requires authentication)
- **Delete a Post**: `DELETE /api/posts/{id}/` (requires authentication)

### Categories

- **Create a Category**: `POST /api/categories/`
- **Retrieve Categories**: `GET /api/categories/`
- **Retrieve a Specific Category**: `GET /api/categories/{id}/`
- **Update a Category**: `PUT /api/categories/{id}/`
- **Delete a Category**: `DELETE /api/categories/{id}/`

### Authentication

- **Obtain JWT Token**: `POST /api/token/`
- **Refresh JWT Token**: `POST /api/token/refresh/`
- **Register a New User**: `POST /api/register/`

# Authentication Setup

## Overview

This project uses JWT (JSON Web Token) for authentication. Users must obtain a token by providing their credentials and use this token to access protected endpoints.

## Installation

Ensure you have the required packages installed:

```bash
pip install djangorestframework djangorestframework-simplejwt

## Deployment

To deploy the API on Heroku or PythonAnywhere, follow their respective documentation for deploying Django applications.
