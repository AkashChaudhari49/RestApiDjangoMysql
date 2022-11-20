from rest_framework import serializers
from .models import Book

#create serializers here
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"