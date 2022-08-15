from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView
from .models import Book, Author
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class ListBookView(ListView):
    model = Book
    template_name = 'books.html'

class ListAuthorView(ListView):
    model = Author
    template_name = 'authors.html'

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

class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'delete_author.html'
    success_url = reverse_lazy('list_author')

class UpdateAuthorView(UpdateView):
    model = Author
    template_name = 'update_author.html'
    fields = ('name', 'last_name')
    success_url = reverse_lazy('list_author')

class UpdateBookView(UpdateView):
    model = Book
    template_name = 'update_book.html'
    fields = ('title', 'total_pages', 'rating', 'isbn', 'author')
    success_url = reverse_lazy('list_book')