1. pip install django djangorestframework

Create a Post: POST /api/posts/
Update a Post: PUT /api/posts/{id}/
Delete a Post: DELETE /api/posts/{id}/
View Posts by Category: GET /api/posts/?category={category_id}
View Posts by Author: GET /api/posts/?author={author_id}


2. pip install django djangorestframework djangorestframework-simplejwt

API endpoints:

Create a Post: POST /api/posts/ (requires authentication)
Update a Post: PUT /api/posts/{id}/ (requires authentication)
Delete a Post: DELETE /api/posts/{id}/ (requires authentication)
View Posts by Category: GET /api/posts/?category={category_id}
View Posts by Author: GET /api/posts/?author={author_id}
Search Posts: Implement search functionality in the get_queryset method of PostViewSet.

post (user, Category, tag)