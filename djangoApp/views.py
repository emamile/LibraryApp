from rest_framework import status, viewsets
from rest_framework.response import Response

from djangoApp.constants import MESSAGE_OBJECT_DELETED_SUCCESSFULLY, ERROR_MESSAGE_QUERY_STRING_NOT_PROVIDED
from djangoApp.models import Author, Book
from djangoApp.serializers.author_serializer import AuthorSerializer
from djangoApp.serializers.book_serializer import BookSerializer
from djangoApp.services.author_service import AuthorService
from djangoApp.services.book_service import BookService


class CRUDViewSet(viewsets.ViewSet):
    permission_classes = []
    model = None
    service_class = None
    serializer_class = None

    def get(self, request) -> Response:
        model_instances = self.model.objects.all()
        serialized = self.serializer_class(model_instances, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    def get_object(self, request, id: int) -> Response:
        model_instance = self.model.objects.get(id=id)
        serializer = self.serializer_class(model_instance)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id: int) -> Response:
        model_instance = self.model.objects.get(id=id)
        serializer = self.serializer_class(model_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id: int) -> Response:
        self.model.objects.get(id=id).delete()
        return Response(status=status.HTTP_200_OK,
                        data=MESSAGE_OBJECT_DELETED_SUCCESSFULLY.format(self.model.__name__, id))


class AuthorApi(CRUDViewSet):
    permission_classes = []

    model = Author
    service_class = AuthorService
    serializer_class = AuthorSerializer

    def get_top_five_authors(self, request) -> Response:
        authors = self.service_class.get_top_five_authors()
        serializer = self.serializer_class(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookApi(CRUDViewSet):
    permission_classes = []

    model = Book
    service_class = BookService
    serializer_class = BookSerializer

    def get_books_by_author(self, request, id: int) -> Response:
        books = self.service_class.get_books_by_author(author_id=id)
        serializer = self.serializer_class(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_books_published_last_year(self, request) -> Response:
        books = self.service_class.get_books_published_last_year()
        serializer = self.serializer_class(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def search_books(self, request) -> Response:
        query = request.query_params.get('query', None)
        if query is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=ERROR_MESSAGE_QUERY_STRING_NOT_PROVIDED)
        books = self.service_class.search_books(text=query)
        serializer = self.serializer_class(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
