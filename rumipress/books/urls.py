from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('categories/', views.book_category_list, name='book_category_list'),
    path('categories/new/', views.book_category_create, name='book_category_create'),
    path('categories/<int:pk>/edit/', views.book_category_update, name='book_category_update'),
    path('categories/<int:pk>/delete/', views.book_category_delete, name='book_category_delete'),
    # Add more paths as needed for other views
]
