from django.urls import path

from .views import ListBookView, AddBookView, DeleteBookView, AddAuthorView

urlpatterns = [
    path('', ListBookView.as_view(), name='list_book'),
    path('add/', AddBookView.as_view(), name='add_book'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='delete_book'),
    path('addAuthor/', AddAuthorView.as_view(), name='add_author'),
]