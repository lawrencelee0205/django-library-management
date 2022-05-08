import random
from django.db import models
from django_countries.fields import CountryField

def generate_isbn():
    return "".join([str(random.randint(0,9)) for _ in range(10)])

BOOK_CATEGORY = (
    ('SC', 'SCIENCTIFIC'),
    ('AD', 'ADVENTURE'),
    ('FC', 'FICTION'),
    ('NFC', 'NON-FICTION'),
)

GENDER_CATEGORY = (
    ('M','MALE'),
    ('F','FEMALE'),
)

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10,unique=True,default=generate_isbn())
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10,choices=BOOK_CATEGORY)
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    library = models.ManyToManyField('Library',related_name='books')
    Publications = models.ForeignKey('Publication',on_delete=models.CASCADE,related_name='books')
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10,choices=GENDER_CATEGORY)
    nationality = CountryField(blank_label='(Select country)')
    born_date = models.DateField()
    publication = models.OneToOneField('Publication',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length=200)    
    
    def __str__(self):
        return self.name