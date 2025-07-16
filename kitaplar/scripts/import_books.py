import csv
import os
from datetime import datetime
from django.conf import settings
from kitaplar.models import Book, Author

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        try:
            return datetime.strptime(date_str, "%d.%m.%Y").date()
        except ValueError:
            return None

def run():
    csv_path = os.path.join(settings.BASE_DIR, 'kitaplar.csv')

    with open(csv_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            # Kontrol amaçlı her satırı yazdırmak istersen açabilirsin
            # print(f"Importing book: {row['title']} by {row['author_name']}")

            author, _ = Author.objects.get_or_create(name=row['author_name'])

            publish_date = parse_date(row.get('publish_date', ''))

            Book.objects.get_or_create(
                title=row['title'],
                author=author,
                description=row.get('description', ''),
                publish_date=publish_date,
                cover_image_url=row.get('cover_image_url', '')
            )

    print("Kitaplar başarıyla eklendi.")
