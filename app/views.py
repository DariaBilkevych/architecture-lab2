from flask import Blueprint, request, jsonify
from .models import db_session, Book
from .services import get_book_from_db, add_book_to_db

book_bp = Blueprint('books', __name__, url_prefix='/books')

# Adding a new book
@book_bp.route('/', methods=['POST'])
def add_book():
    data = request.get_json()
    add_book_to_db(data['title'], data['author'])
    return jsonify({"message": "Book added"}), 201

# Getting a book
@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book_from_db(book_id)
    if book:
        return jsonify({"id": book.id, "title": book.title, "author": book.author})
    return jsonify({"message": "Book not found"}), 404

# Updating an existing book
@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = db_session.query(Book).filter(Book.id == book_id).first()
    if book:
        book.title = data['title']
        book.author = data['author']
        db_session.commit()
        return jsonify({"message": "Book updated"}), 200
    return jsonify({"message": "Book not found"}), 404

# Deleting a book
@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = db_session.query(Book).filter(Book.id == book_id).first()
    if book:
        db_session.delete(book)
        db_session.commit()
        return jsonify({"message": "Book deleted"}), 200
    return jsonify({"message": "Book not found"}), 404