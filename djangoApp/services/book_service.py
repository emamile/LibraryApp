from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from django.db.models import QuerySet, Q

from djangoApp.models import Book


class BookService:
    @staticmethod
    def get_books_published_last_year() -> QuerySet[Book]:
        return Book.objects.filter(published_date__gte=(datetime.now() - relativedelta(years=1)))

    @staticmethod
    def get_books_by_author(author_id: int) -> QuerySet[Book]:
        return Book.objects.filter(author_id=author_id)

    @staticmethod
    def search_books(text: str) -> QuerySet[Book]:
        return Book.objects.filter(Q(title__icontains=text) | Q(description__icontains=text))
