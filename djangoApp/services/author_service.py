from django.db.models import QuerySet, Count

from djangoApp.models import Author


class AuthorService:

    @staticmethod
    def get_top_five_authors() -> QuerySet[Author]:
        return Author.objects.annotate(books_count=Count('authors_books')).order_by("-books_count")[:5]
