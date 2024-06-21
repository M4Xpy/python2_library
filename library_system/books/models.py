from datetime import timedelta

from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    loan_date = models.DateField(default=timezone.now)
    return_date = models.DateField(
        default=lambda: timezone.now().date() + timedelta(weeks=1)
    )

    def is_overdue(self):
        return self.return_date < timezone.now().date()

    def days_until_due(self):
        return (self.return_date - timezone.now().date()).days

    def __str__(self):
        return "{} - {} - {}".format(self.book, self.client, self.return_date)
