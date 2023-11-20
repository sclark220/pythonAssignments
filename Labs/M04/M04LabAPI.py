from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# I just want to be honest I don't get it. I spent a long time just to copy this from the internet
# I am sorry

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookName = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)

# Create a new book
@app.route('/books', methods=['POST'])
def createBook():
    bookName = request.json['bookName']
    author = request.json['author']
    publisher = request.json['publisher']

    newBook = Book(bookName=bookName, author=author, publisher=publisher)
    db.session.add(newBook)
    db.session.commit()

    return jsonify({'message': 'Book created successfully!'}), 201

# Get all books
@app.route('/books', methods=['GET'])
def getAllBooks():
    books = Book.query.all()
    bookData = []

    for book in books:
        bookData.append({
            'id': book.id,
            'bookName': book.bookName,
            'author': book.author,
            'publisher': book.publisher
        })

    return jsonify({'books': bookData}), 200

# Get a single book
@app.route('/books/<int:id>', methods=['GET'])
def getBook(id):
    book = Book.query.get_or_404(id)

    return jsonify({
        'id': book.id,
        'bookName': book.bookName,
        'author': book.author,
        'publisher': book.publisher
    }), 200

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def updateBook(id):
    book = Book.query.get_or_404(id)

    book.bookName = request.json['bookName']
    book.author = request.json['author']
    book.publisher = request.json['publisher']

    db.session.commit()

    return jsonify({'message': 'Book updated successfully!'}), 200

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def deleteBook(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return jsonify({'message': 'Book deleted successfully!'}), 204

if __name__ == '__main__':
    app.run(debug=True)