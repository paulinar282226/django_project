from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from wypozyczalnia.models import Books, Movies, CD, Songs, Rental

class RegisterView(View):
    def get(self, request):
        return render(request, 'registration/register.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))

        return render(request, 'registration/register.html', { 'form': form })


class BookCreate(CreateView):
    model = Books
    fields = ['title', 'author', 'genre', 'isbn', 'rental']
    success_url = '/'

class MovieCreate(CreateView):
    model = Movies
    fields = ['director', 'title', 'genre', 'rental', 'duration']
    success_url = '/'

class CDCreate(CreateView):
    model = CD
    fields = ['band', 'title', 'genre', 'rental', 'duration']
    success_url = '/'

class SongCreate(CreateView):
    model = Songs
    fields = ['title', 'Cd']
    success_url = '/'

class HomeView(TemplateView):
    template_name = "home.html"





class RentalBaseView(View):
    model = Rental
    fields = '__all__'
    success_url = '/rental_list'

class RentalCreateView(RentalBaseView,CreateView):
   pass

class RentalListView(RentalBaseView, ListView):
    pass


class BookBaseView(View):
    model = Books
    fields = '__all__'
    success_url = '/book_list'

class BookUpdateView(BookBaseView, UpdateView):
    pass

class BookListView(BookBaseView, ListView):
    pass

class BookDeleteView(BookBaseView, DeleteView):
    pass

class BookCreateView(BookBaseView,CreateView):
   pass


class MovieBaseView(View):
    model = Movies
    fields = '__all__'
    success_url = '/movie_list'

class MovieUpdateView(MovieBaseView, UpdateView):
    pass

class MovieListView(MovieBaseView, ListView):
    pass

class MovieDeleteView(MovieBaseView, DeleteView):
    pass

class MovieCreateView(MovieBaseView,CreateView):
   pass

class CdBaseView(View):
    model = CD
    fields = '__all__'
    success_url = '/cd_list'

class CdUpdateView(CdBaseView, UpdateView):
    pass

class CdListView(CdBaseView, ListView):
    pass

class CdDeleteView(CdBaseView, DeleteView):
    pass

class CdCreateView(CdBaseView,CreateView):
   pass


