# coding: utf-8

from abc import ABCMeta, abstractmethod

class Aggregate(object, metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass

class Iterator(object, metaclass=ABCMeta):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class Book(object):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class BookShelf(Aggregate):
    def __init__(self):
        self.__books = []

    def get_book_at(self, index):
        return self.__books[index]

    def append_book(self,book):
        self.__books.append(book)

    def get_length(self):
        return len(self.__books)

    def iterator(self):
        return BookShelfIterator(self)

class BookShelfIterator(Iterator):
    def __init__(self, book_shelf):
        self.__book_shelf = book_shelf
        self.__index = 0

    def has_next(self):
        if self.__index < self.__book_shelf.get_length():
            return True
        else:
            return False

    def next(self):
        book = self.__book_shelf.get_book_at(self.__index)
        self.__index += 1
        return book

if __name__ == "__main__":
    book_shelf = BookShelf()
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))
    it = book_shelf.iterator()
    while it.has_next():
        book = it.next()
        print(book.get_name())
