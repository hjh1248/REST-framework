from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'bid', 'tirle', 'author', 'category', 'pages', 'price', 'published_date', 'description'
            ]
        