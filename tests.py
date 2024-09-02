from library.models import Book

book_name = Book.objects.first().title
print(book_name)