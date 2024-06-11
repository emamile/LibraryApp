from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(db_index=True)
    published_date = models.DateField(db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="authors_books")

    def __str__(self):
        return self.title
