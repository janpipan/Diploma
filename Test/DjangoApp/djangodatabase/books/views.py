from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from .models import Book, Author
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ListBookView(ListView):
    model = Book
    template_name = 'books.html'

class AddBookView(CreateView):
    model = Book
    template_name = 'add_book.html'
    fields = ('title', 'total_pages', 'rating', 'isbn', 'author')

    def form_valid(self, form):
        return super().form_valid(form)

class DeleteBookView(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('list_book')

class AddAuthorView(CreateView):
    model = Author
    template_name = 'add_author.html'
    fields = ('name', 'last_name')

    def form_valid(self, form):
        return super().form_valid(form)