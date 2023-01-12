from django.urls import path, include
from .views import BookAPI, BooksAPI

urlpatterns = [
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/books/<int:bid>/", BookAPI.as_view()),
]