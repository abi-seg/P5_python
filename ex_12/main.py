
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
     

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []


    def add_book(self,book):
        self.books.append(book)
        #print(f"Le livre '{book.title}' a été ajouté à la bibliothèque.")

    def remove_book(self,book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                print(f" Le livre '{book_title}' a été supprimé de la bibliothèque.")
                return
        print(f"Le livre '{book_title}' n'est pas disponible dans la bibliothèque.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                print(f"Vous avez emprunté '{book_title}'.")
                return
        print(f"Le livre '{book_title}' n'est pas disponible pour l'emprunt.")

    def return_book(self,book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                print(f"Vous avez rendu '{book_title}'.")
                return
        print(f"Le Livre '{book_title}' n'a pas été emprunté ici.")

    def available_books(self):
        if not self.books:
            print("Aucun livre disponible.")
        else:
            print("Livres disponibles :")
            for book in self.books:
                print(f"-{book.title} ({book.author}, {book.year})")
    
    def borrowed_books_list(self):
        if not self.borrowed_books:
            print("Aucun livre emprunté.")
        else:
            print("Livres empruntés : ")
            for book in self.borrowed_books:
                print(f"-{book.title} ({book.author},{book.year})")
    
library =  Library()

books_list = [
    Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943),
    Book("L'Étranger", "Albert Camus", 1942),
    Book("1984", "George Orwell", 1949),
    Book("Les Misérables", "Victor Hugo", 1862),
    Book("Le Rouge et le Noir", "Stendhal", 1830),
    Book("Madame Bovary", "Gustave Flaubert", 1857),
    Book("La Peste", "Albert Camus", 1947),
    Book("Le Comte de Monte-Cristo", "Alexandre Dumas", 1844),
    Book("Germinal", "Émile Zola", 1885),
    Book("Bel-Ami", "Guy de Maupassant", 1885)
]  
for book in books_list:
    library.add_book(book)


while True:
    print("\n--- Menu Bibliothèque ---")
    print("1. Afficher les livres disponibles")
    print("2. Afficher les livres empruntés")
    print("3. Emprunter un livre")
    print("4. Rendre un livre")
    print("5. Quitter")
    choice = input("Votre choix : ")

    if choice == "1":
        library.available_books()
    elif choice == "2":
        library.borrowed_books_list()
    elif choice == "3":
        title = input("Entrez le titre du livre à emprunter : ")
        library.borrow_book(title)
    elif choice == "4":
        title = input("Entrez le titre du livre à rendre : ")
        library.return_book(title)
    elif choice == "5":
        print("Au revoir !")
        break
    else:
        print("Choix invalide, veuillez réessayer.")

