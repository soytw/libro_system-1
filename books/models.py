from django.db import models

from urllib.request import urlopen
import datetime
import json
import operator
import re

from books import utils

#class Category(models.Model):
#    category_name = models.CharField(max_length=453)

class Author(models.Model):
    name = models.CharField(max_length=453)

    def __str__(self):
        return self.name

class Bookdetails(models.Model):
    title = models.CharField(max_length=453)
    subtitle = models.CharField(max_length=453, blank=True)
    authors = models.ManyToManyField(Author) # [TODO] translator
    publisher = models.CharField(max_length=453, blank=True)
    #published_date = models.DateField(blank=True, null=True)
    published_date = models.CharField(max_length=53, blank=True)
    #identifiers = models.ManyToManyField(BookIdentifier)
    #identifiers changed to foreignkey
    description = models.TextField(max_length=9453, blank=True)
    
    def __str__(self):
        return self.title

class BookIdentifier(models.Model):
    itype = models.CharField(max_length=7, choices=(
        ('ISBN_10', 'International Standard Book Number (10 digits)'),
        ('ISBN_13', 'International Standard Book Number (13 digits)'),
        ('ISSN', 'International Standard Serial Number (8 digits)')))

    identifier = models.CharField(max_length=13)
    belongbook = models.ForeignKey(Bookdetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier

#    categories = models.ManyToManyField(Category)

    # books_owned = models.ForeignKey('Book', models.CASCADE, one_to_many=True)
    # [TODO] https://docs.djangoproject.com/en/dev/topics/db/queries/#following-relationships-backward

#    @staticmethod
#    def add_books(books):
#        # add new books if not exist
#        for book_info in books.get('items'):
#            present_books = BookDetails.objects.filter(
#                identifiers__identifier = book_info.get('industryIdentifiers')[0]
#                                                   .get('identifier'))
#            if present_books:
#                return present_books[0]
#            else:
#                new_book = BookDetails(
#                    title = book_info.get('title'),
#                    subtitle = book_info.get('subtitle'),
#                    published_date = utils.parse_date(book_info.get('publishedDate')),
#                    publisher = book_info.get('publisher'),
#                    description = book_info.get('description'))
#                new_book.save()
#                for d in book_info.get('industryIdentifiers'):
#                    new_book.identifiers.add(
#                        BookIdentifier.objects.get_or_create(type=d['type'],
#                                                             identifier=d['identifier'])[0])
#                for name in book_info.get('authors'):
#                    new_book.authors.add(
#                        Author.objects.get_or_create(name=name)[0])
#                # [TODO] categories
#                return new_book

class Location(models.Model):
    floor = models.CharField(max_length=53, blank=True)
    room = models.CharField(max_length=53, blank=True)

class Possessor(models.Model):
    name = models.CharField(max_length=453, blank=True)

class Book(models.Model):
    detail = models.ForeignKey(Bookdetails, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    possessor = models.ForeignKey(Possessor, on_delete=models.PROTECT)
    notas = models.TextField(max_length=9453, blank=True)

