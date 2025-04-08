class Book:
    def __init__(self, title, genre, author):
        self.title = title
        self.genre = genre
        self.author = author

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre:{self.genre}")
        print(f"Author:{self.author}")

    def change_genre(self, biography):
        self.genre = biography
        print(f"Genre updated to: {self.genre}")

my_book = Book("My Story", "Autobiography", "Alicia Keys")

my_book.display_details()

my_book.change_genre("Biography")

my_book.display_details()





