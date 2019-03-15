from connexion import NoContent
from datetime import datetime, timedelta

from app.orm import Book
from main import db_session


def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return book.dump()
    return NoContent, 404


def delete_book(book_id):
    book = Book.query.get(book_id)
    if book:
        db_session.delete(book)
        db_session.commit()
        return NoContent, 204
    return 404


def update_book(book_id, book_obj):
    book_data = book_obj.get('data')
    if book_data:
        book_attrs = book_data.get('attributes')
        if book_attrs:
            book = Book.query.filter_by(id=book_id).update(dict(name=book_attrs['name'],
                                                                author=book_attrs['author'],
                                                                year=book_attrs['year'],
                                                                pages_count=book_attrs['pages_count'])
                                                           )
            if book is None:
                return 404
            db_session.commit
            return get_book(book_id)
        else:
            return {'errors': 'No attributes given'}, 400
    else:
        return {'errors': 'No data'}, 400


def get_books(name=None, author=None, after=0, before=0):
    books_query = db_session.query(Book)

    if name:
        books_query = books_query.filter(Book.author.contains(name))
    if author:
        books_query = books_query.filter(Book.author.contains(author))
    if after != 0:
        books_query = books_query.filter(Book.datetime_added > datetime.now() - timedelta(seconds=after))
    if before != 0:
        books_query = books_query.filter(Book.datetime_added < datetime.now() - timedelta(seconds=after))
    books_list = [book.dump() for book in books_query.all()]

    return {'books': books_list,
            'name': name,
            'author': author,
            'after': after,
            'before': before, }


def create_books(books_list):
    books_created_ids = []
    books_created = []
    for book in books_list:
        book_data = book.get('data')
        if book_data:
            book_data.pop('id', None)
            book_attrs = book_data.get('attributes')
            book_attrs.pop('datetime_added', None)
            if book_attrs:
                book_obj = Book(**book_attrs)
                db_session.add(book_obj)
                db_session.commit()
                books_created_ids.append(book_obj.id)
        else:
            return {'errors': 'No data'}, 400

    for book_id in books_created_ids:
        books_created.append(get_book(book_id))
    return books_created, 201
