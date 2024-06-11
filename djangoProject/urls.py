"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from djangoApp.views import AuthorApi, BookApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path("authors/top", AuthorApi.as_view({"get": "get_top_five_authors"})),
    path("authors/<id>", AuthorApi.as_view({"get": "get_object"})),
    path("authors", AuthorApi.as_view({"get": "get"})),
    path("authors", AuthorApi.as_view({"post": "post"})),
    path("authors/<id>", AuthorApi.as_view({"put": "put"})),
    path("authors/<id>", AuthorApi.as_view({"delete": "delete"})),
    path("books/search", BookApi.as_view({"get": "search_books"})),
    path("books/<id>", BookApi.as_view({"get": "get_object"})),
    path("books", BookApi.as_view({"get": "get"})),
    path("books", BookApi.as_view({"post": "post"})),
    path("books/<id>", BookApi.as_view({"put": "put"})),
    path("books/<id>", BookApi.as_view({"delete": "delete"})),
    path("authors/<id>/books", BookApi.as_view({"get": "get_books_by_author"})),
    path("books/recent", BookApi.as_view({"get": "get_books_published_last_year"})),
]
