# coding: utf-8

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

