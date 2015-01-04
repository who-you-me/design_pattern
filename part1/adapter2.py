# coding: utf-8

from abc import ABCMeta, abstractmethod

class Banner(object):
    def __init__(self, string):
        self.__string = string

    def show_with_paren(self):
        print("(" + self.__string + ")")

    def show_with_aster(self):
        print("*" + self.__string + "*")

class Print(object, metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self):
        pass

    def print_strong(self):
        pass

class PrintBanner(Print):
    def __init__(self, string):
        self.__banner = Banner(string)

    def print_weak(self):
        self.__banner.show_with_paren()

    def print_strong(self):
        self.__banner.show_with_aster()

if __name__ == "__main__":
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()
