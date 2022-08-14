from django.urls import path

from .views import ListBookView, AddBookView, DeleteBookView, AddAuthorView, ListAuthorView, DeleteAuthorView, UpdateAuthorView, UpdateBookView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list/book/', ListBookView.as_view(), name='list_book'),
    path('list/author/', ListAuthorView.as_view(), name='list_author'),
    path('add/book', AddBookView.as_view(), name='add_book'),
    path('add/author', AddAuthorView.as_view(), name='add_author'),
    path('delete/book/<int:pk>', DeleteBookView.as_view(), name='delete_book'),
    path('delete/author/<int:pk>', DeleteAuthorView.as_view(), name='delete_author'),
    path('update/book/<int:pk>', UpdateBookView.as_view(), name='edit_book'),
    path('update/author/<int:pk>', UpdateAuthorView.as_view(), name='edit_author'),
]   