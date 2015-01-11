# coding: utf-8

import sys

from abc import ABCMeta, abstractmethod

class Builder(object, metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title):
        pass

    @abstractmethod
    def make_string(self, string):
        pass

    @abstractmethod
    def make_items(self, items):
        pass

    @abstractmethod
    def close(self):
        pass

class Director(object):
    def __init__(self, builder):
        self.__builder = builder

    def construct(self):
        self.__builder.make_title("Greeting")
        self.__builder.make_string("朝から昼にかけて")
        self.__builder.make_items([
            "おはようございます。",
            "こんにちは。"
        ])
        self.__builder.make_string("夜に")
        self.__builder.make_items([
            "こんばんは。",
            "おやすみなさい。",
            "さようなら。"
        ])
        self.__builder.close()

class TextBuilder(Builder):
    def __init__(self):
        self.__buffer = ""

    def make_title(self, title):
        self.__buffer += "==============================\n"
        self.__buffer += ("『" + title + "』\n")
        self.__buffer += "\n"

    def make_string(self, string):
        self.__buffer += ("■" + string + "\n")
        self.__buffer += "\n"

    def make_items(self, items):
        for item in items:
            self.__buffer += ("　・" + item + "\n")
        self.__buffer += "\n"

    def close(self):
        self.__buffer += "==============================\n"

    def get_result(self):
        return self.__buffer

class HtmlBuilder(Builder):
    def __init__(self):
        self.__filename = None
        self.__writer = None

    def make_title(self, title):
        self.__filename = title + ".html"
        self.__writer = open(self.__filename, "w")
        self.__writer.write("<html><head><title>" + title + "</title></head><body>")
        self.__writer.write("\n")
        self.__writer.write("<h1>" + title + "</h1>")
        self.__writer.write("\n")

    def make_string(self, string):
        self.__writer.write("<p>" + string + "</p>")
        self.__writer.write("\n")

    def make_items(self, items):
        self.__writer.write("<ul>")
        self.__writer.write("\n")
        for item in items:
            self.__writer.write("<li>" + item + "</li>")
            self.__writer.write("\n")
        self.__writer.write("</ul>")
        self.__writer.write("\n")

    def close(self):
        self.__writer.write("</body></html>")
        self.__writer.write("\n")
        self.__writer.close()

    def get_result(self):
        return self.__filename

if __name__ == "__main__":
    if sys.argv[1] == "plain":
        text_builder = TextBuilder()
        director = Director(text_builder)
        director.construct()
        result = text_builder.get_result()
        print(result)
    elif sys.argv[1] == "html":
        html_builder = HtmlBuilder()
        director = Director(html_builder)
        director.construct()
        filename = html_builder.get_result()
        print(filename + "が作成されました。")

