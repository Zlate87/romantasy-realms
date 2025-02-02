from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    books = [
        {"title": "Book 1", "url": "#", "image": "static/images/book1.jpg"},
        {"title": "Book 2", "url": "#", "image": "static/images/book2.jpg"},
        {"title": "Book 3", "url": "#", "image": "static/images/book3.jpg"},
        {"title": "Book 4", "url": "#", "image": "static/images/book4.jpg"},
        {"title": "Book 5", "url": "#", "image": "static/images/book5.jpg"},
        {"title": "Book 6", "url": "#", "image": "static/images/book6.jpg"},
        {"title": "Book 7", "url": "#", "image": "static/images/book7.jpg"},
        {"title": "Book 8", "url": "#", "image": "static/images/book8.jpg"},
        {"title": "Book 9", "url": "#", "image": "static/images/book9.jpg"},
        {"title": "Book 10", "url": "#", "image": "static/images/book10.jpg"},
    ]
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=False, port=5055, host="0.0.0.0")
