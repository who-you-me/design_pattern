# coding: utf-8

import unicodedata
from framework import Product, Manager

def string_width(string):
    width = 0
    for ch in string:
        char_width = unicodedata.east_asian_width(ch)
        if char_width in "WFA":
            width += 2
        else:
            width += 1

    return width

class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, string):
        length = string_width(string)
        for i in range(length + 4):
            print(self.decochar, end="")
        print()
        print(self.decochar + " " + string + " " + self.decochar)
        for i in range(length + 4):
            print(self.decochar, end="")
        print()


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, string):
        length = string_width(string)
        print('"' + string + '"')
        print(" ", end="")
        for i in range(length):
            print(self.ulchar, end="")
        print()

if __name__ == "__main__":
    manager = Manager()
    upen = UnderlinePen("~")
    mbox = MessageBox("*")
    sbox = MessageBox("/")
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    p1 = manager.create("strong message")
    p1.use("Hello, world.")
    p2 = manager.create("warning box")
    p2.use("Hello, world.")
    p3 = manager.create("slash box")
    p3.use("Hello, world.")

