from django.db import models

import uuid


# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    publisher = models.CharField(max_length=100)
    publishdate = models.DateTimeField(auto_now_add=True)
    book_category = models.ForeignKey(BookCategory, related_name='books', on_delete=models.CASCADE,
                                      blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)
    notelp = models.CharField(max_length=16, unique=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Order(models.Model):
    code_borrow = models.CharField(max_length=8,null=True, blank=True, unique=True, default=uuid.uuid4().hex[:6].upper())
    book = models.ForeignKey(Book, related_name='books', on_delete=models.CASCADE, blank=True, null=True)
    member = models.ForeignKey(Member, related_name='members', on_delete=models.CASCADE, default=None, blank=True,
                               null=True)
    date_borrow = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
