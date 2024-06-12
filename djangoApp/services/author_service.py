from django.db.models import QuerySet, Count

from djangoApp.models import Author


class AuthorService:

    @staticmethod
    def get_top_five_authors() -> QuerySet[Author]:
        """Returns queryset of authors with the most written books."""
        return Author.objects.annotate(books_count=Count('authors_books')).order_by("-books_count")[:5]
