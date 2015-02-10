# coding: utf-8

from bigchar_factory import BigCharFactory

class BigString(object):
    def __init__(self, string):
        self.__bigchars = []
        factory = BigCharFactory.get_instance()
        for c in string:
            self.__bigchars.append(factory.get_big_char(c))

    def print(self):
        for c in self.__bigchars:
            c.print()

