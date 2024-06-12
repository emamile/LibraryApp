from django.urls import path

from djangoApp.views import AuthorApi, BookApi

urlpatterns = [
    path("authors/top", AuthorApi.as_view({"get": "get_top_five_authors"})),
    path("authors/<id>", AuthorApi.as_view({"get": "get_object"})),
    path("authors", AuthorApi.as_view({"get": "get"})),
    path("authors", AuthorApi.as_view({"post": "post"})),
    path("authors/<id>", AuthorApi.as_view({"put": "put"})),
    path("authors/<id>", AuthorApi.as_view({"delete": "delete"})),
    path("books/search", BookApi.as_view({"get": "search_books"})),
    path("books/recent", BookApi.as_view({"get": "get_books_published_last_year"})),
    path("books/<id>", BookApi.as_view({"get": "get_object"})),
    path("books", BookApi.as_view({"get": "get"})),
    path("books", BookApi.as_view({"post": "post"})),
    path("books/<id>", BookApi.as_view({"put": "put"})),
    path("books/<id>", BookApi.as_view({"delete": "delete"})),
    path("authors/<id>/books", BookApi.as_view({"get": "get_books_by_author"})),
]