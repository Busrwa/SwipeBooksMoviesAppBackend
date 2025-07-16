from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nested serializer ile yazar detayını göster

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'publish_date', 'cover_image_url']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(name=author_data['name'])
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        author_data = validated_data.pop('author')
        author, created = Author.objects.get_or_create(name=author_data['name'])

        instance.title = validated_data.get('title', instance.title)
        instance.author = author
        instance.description = validated_data.get('description', instance.description)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)
        instance.cover_image_url = validated_data.get('cover_image_url', instance.cover_image_url)
        instance.save()
        return instance
