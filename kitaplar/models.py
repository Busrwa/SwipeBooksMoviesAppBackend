from django.db import models

class Author(models.Model):
    # Yazar ismi
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    # Yazar ilişkisi (bir kitap bir yazara ait)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    description = models.TextField(blank=True)
    publish_date = models.DateField(null=True, blank=True)

    # Kapak resmi URL ya da dosya
    cover_image_url = models.URLField(blank=True)
    # Eğer medya dosyası kullanmak istersen:
    # cover_image = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
