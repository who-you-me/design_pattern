# coding: utf-8

import unicodedata
from abc import ABCMeta, abstractmethod

class Display(object, metaclass=ABCMeta):
    def __init__(self, impl):
        self.__impl = impl

    def open(self):
        self.__impl.raw_open()

    def print(self):
        self.__impl.raw_print()

    def close(self):
        self.__impl.raw_close()

    def display(self):
        self.open()
        self.print()
        self.close()

class CountDisplay(Display):
    def multi_display(self, times):
        self.open()
        for i in range(times):
            self.print()
        self.close()

class DisplayImpl(object, metaclass=ABCMeta):
    @abstractmethod
    def raw_open(self):
        pass

    @abstractmethod
    def raw_print(self):
        pass

    @abstractmethod
    def raw_close(self):
        pass

class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.__string = string
        self.__width = self.string_width(string)

    def raw_open(self):
        self.__print_line()

    def raw_print(self):
        print("|" + self.__string + "|")

    def raw_close(self):
        self.__print_line()

    def __print_line(self):
        print("+", end="")
        for i in range(self.__width):
            print("-", end="")
        print("+")

    def string_width(self, string):
        width = 0
        for ch in string:
            char_width = unicodedata.east_asian_width(ch)
            if char_width in "WFA":
                width += 2
            else:
                width += 1

        return width

if __name__ == "__main__":
    d1 = CountDisplay(StringDisplayImpl("Hello, Japan."))
    d1.display()
    d1.multi_display(5)
