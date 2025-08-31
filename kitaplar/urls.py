from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorListCreateView, AuthorDetailView,
    BookListCreateView, BookDetailView
)


urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
