from .models import db_session, Book
from cachetools import TTLCache, cached

# Initialize cache with TTL
cache = TTLCache(maxsize=100, ttl=60)

# Book caching by ID
@cached(cache)
def get_book_from_db(book_id):
    return db_session.query(Book).filter(Book.id == book_id).first()

# Adding a book to the database
def add_book_to_db(title, author):
    new_book = Book(title=title, author=author)
    db_session.add(new_book)
    db_session.commit()


