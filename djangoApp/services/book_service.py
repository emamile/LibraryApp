from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.db.models import QuerySet, Q

from djangoApp.models import Book


class BookService:
    @staticmethod
    def get_books_published_last_year() -> QuerySet[Book]:
        """Returns books published within last year"""
        return Book.objects.filter(published_date__gte=(datetime.now() - relativedelta(years=1)))

    @staticmethod
    def get_books_by_author(author_id: int) -> QuerySet[Book]:
        """Returns books written by author with provided id"""
        return Book.objects.filter(author_id=author_id)

    @staticmethod
    def search_books(text: str) -> QuerySet[Book]:
        """Returns books whose title or description contains provided text"""
        return Book.objects.filter(Q(title__icontains=text) | Q(description__icontains=text))
