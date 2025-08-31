from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'isbn', 'title', 'author', 'description', 'publish_date', 'cover_image_url']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, _ = Author.objects.get_or_create(name=author_data['name'])
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author', None)
        if author_data:
            author, _ = Author.objects.get_or_create(name=author_data['name'])
            instance.author = author

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
