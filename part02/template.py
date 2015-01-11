# coding: utf-8

from abc import ABCMeta, abstractmethod

import unicodedata
import utils

class AbstractDisplay(object, metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def close(self):
        pass

    def display(self):
        self.open()
        for i in range(5):
            self.print()
        self.close()

class CharDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print("<<", end="")

    def print(self):
        print(self.ch, end="")

    def close(self):
        print(">>")

class StringDisplay(AbstractDisplay):
    def __init__(self, string):
        self.string = string
        self.width = utils.string_width(self.string)

    def open(self):
        self.print_line()

    def print(self):
        print("|" + self.string + "|")

    def close(self):
        self.print_line()

    def print_line(self):
        print("+", end="")
        print("-" * self.width, end="")
        print("+")

if __name__ == "__main__":
    d1 = CharDisplay("H")
    d2 = StringDisplay(u"Hello, world!")
    d3 = StringDisplay(u"こんにちは。")
    d1.display()
    d2.display()
    d3.display()
