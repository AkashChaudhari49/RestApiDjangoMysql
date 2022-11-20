from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name= models.CharField(max_length=50)
    quantity = models.IntegerField()
    book_genre = models.CharField(max_length=50)
    is_best_seller = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating  =  models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])

    def __str__(self):
        return f'{self.book_id}--{self.book_name}'