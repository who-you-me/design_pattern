# coding: utf-8

class Book(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class BookShelf(object):
    def __init__(self):
        self.__books = []
        self.__index = 0

    def get_book_at(self, index):
        return self.__books[index]

    def append_book(self,book):
        self.__books.append(book)

    def get_length(self):
        return len(self.__books)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index < self.get_length():
            book = self.get_book_at(self.__index)
            self.__index += 1
            return book
        else:
            raise StopIteration

if __name__ == "__main__":
    book_shelf = BookShelf()
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))
    for book in book_shelf:
        print(book.get_name())
