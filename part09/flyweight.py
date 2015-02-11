# coding: utf-8

import sys

class BigChar(object):
    def __init__(self, charname):
        self.__charname = charname
        try:
            with open("big{}.txt".format(charname)) as f:
                self.__fontdata = f.read()
        except IOError:
            self.__fontdata = charname + "?"

    def print(self):
        print(self.__fontdata)

class BigCharFactory(object):
    class __BigCharFactory(object):
        def __init__(self):
            self.__pool = {}

        def get_big_char(self, charname):
            charname = str(charname)
            bc = self.__pool.get(charname)
            if not bc:
                bc = BigChar(charname)
                self.__pool[charname] = bc
            return bc

    singleton = __BigCharFactory()

    @classmethod
    def get_instance(cls):
        return cls.singleton

class BigString(object):
    def __init__(self, string):
        self.__bigchars = []
        factory = BigCharFactory.get_instance()
        for c in string:
            self.__bigchars.append(factory.get_big_char(c))

    def print(self):
        for c in self.__bigchars:
            c.print()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python flyweight.py digits")
        print("Example: python flyweight.py 1212123")
        sys.exit()

    bs = BigString(sys.argv[1])
    bs.print()
