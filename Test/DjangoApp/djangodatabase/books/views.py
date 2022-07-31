from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Books, Author

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ListBookView(ListView):
    model = Books
    template_name = 'books.html'

class AddBookView(CreateView):
    model = Books
    template_name = 'add_book.html'
    fields = ('title', 'total_pages', 'rating', 'isbn', 'author')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteBookView(TemplateView):
    template_name = 'delete_book.html'

class AddAuthorView(CreateView):
    model = Author
    template_name = 'add_author.html'
    fields = ('name', 'last_name')

    def form_valid(self, form):
        return super().form_valid(form)