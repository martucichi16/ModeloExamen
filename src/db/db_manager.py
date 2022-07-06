import csv
from src.models.book_class import Book


def load_books():
    books = []

    with open("src/db/books.csv", "r") as books_file:
        rows = csv.DictReader(books_file)  # Devuelve un objeto

        for row in rows:
            ISBN = row["ISBN"]
            title = row["title"]
            author = row["author"]
            price = row["price"]
            published = row["published"]
            language = row["language"]
            number_pages = row["number_pages"]
            press = row["press"]
            ranking = row["ranking"]

            object_book = Book(ISBN, title, author, price, published, language, number_pages, press, ranking)

            # Rodri directamente guardo el mapeo en los atributos, osea Book(row["ISBN"], row["title"], ...)

            books.append(object_book)

    return books


# Definimos una funcion que sirva para persistir
def save_purchase_order(purchase):
    with open("src/db/purchase_orders.csv", "a") as purchase_file:
        header = ["date", "ISBN", "user_id", "full_address"]
        writer = csv.DictWriter(purchase_file, fieldnames=header)

        if purchase_file.tell() == 0:  # Te dice cuantas lineas tiene el archivo indicado
            writer.writeheader()

        writer.writerow(purchase)
