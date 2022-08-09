from django.urls import path

from .views import ListBookView, AddBookView, DeleteBookView, AddAuthorView, ListAuthorView, DeleteAuthorView

urlpatterns = [
    path('list/book/', ListBookView.as_view(), name='list_book'),
    path('add/', AddBookView.as_view(), name='add_book'),
    path('delete/book/<int:pk>', DeleteBookView.as_view(), name='delete_book'),
    path('addAuthor/', AddAuthorView.as_view(), name='add_author'),
    path('list/author/', ListAuthorView.as_view(), name='list_author'),
    path('delete/author/<int:pk>', DeleteAuthorView.as_view(), name='delete_author'),
]