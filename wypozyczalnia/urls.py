"""wypozyczalnia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from wypozyczalnia.views import BookCreate, MovieCreate, CDCreate, SongCreate, HomeView, BookListView, MovieListView, \
    CdListView, RentalListView, BookUpdateView, BookDeleteView, MovieUpdateView, MovieDeleteView, CdUpdateView, \
    CdDeleteView, RegisterView, BookCreateView, MovieCreateView, CdCreateView, RentalCreateView
from django.views.generic import TemplateView

book_patterns = ([
path('book_list', BookListView.as_view(), name='book_list'),
path('book_create', BookCreateView.as_view(), name='book_create'),
path('book_update/<int:pk>', BookUpdateView.as_view(), name='book_update'),
path('book_delete/<int:pk>', BookDeleteView.as_view(), name='book_delete'),
],'book')

movie_patterns = ([
path('movie_list', MovieListView.as_view(), name='movie_list'),
path('movie_create', MovieCreateView.as_view(), name='movie_create'),
path('movie_update/<int:pk>', MovieUpdateView.as_view(), name='movie_update'),
path('movie_delete/<int:pk>', MovieDeleteView.as_view(), name='movie_delete'),
],'movie')

cd_patterns = ([
path('cd_list', CdListView.as_view(), name='cd_list'),
path('cd_create', CdCreateView.as_view(), name='cd_create'),
path('cd_update/<int:pk>', CdUpdateView.as_view(), name='cd_update'),
path('cd_delete/<int:pk>', CdDeleteView.as_view(), name='cd_delete'),
],'cd')

rental_patterns = ([
path('rental_list', RentalListView.as_view(), name='rental_list'),
path('rental_create', RentalCreateView.as_view(), name='rental_create'),
],'rental')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('login/', TemplateView.as_view(template_name="login.html")),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add/cd', CDCreate.as_view()),
    path('add/song', SongCreate.as_view()),
    path('', HomeView.as_view()),
    path('', include(book_patterns)),
    path('', include(movie_patterns)),
    path('', include(cd_patterns)),
    path('', include(rental_patterns)),
]
