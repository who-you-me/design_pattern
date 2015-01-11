# coding: utf-8

from abc import ABCMeta, abstractmethod

class Item(object, metaclass=ABCMeta):
    def __init__(self, caption):
        self._caption = caption

    @abstractmethod
    def make_html(self):
        pass

class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption, url):
        Item.__init__(self, caption)
        self._url = url

class Tray(Item, metaclass=ABCMeta):
    def __init__(self, caption):
        Item.__init__(self, caption)
        self._tray = []

    def add(self, item):
        self._tray.append(item)

class Page(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._content = []

    def add(self, item):
        self._content.append(item)

    def output(self):
        filename = self._title + ".html"
        writer = open(filename, "w")
        writer.write(self.make_html())
        writer.close()
        print(filename + "を作成しました。")

    @abstractmethod
    def make_html(self):
        pass

class Factory(object, metaclass=ABCMeta):
    @classmethod
    def get_factory(cls, class_name):
        parts = class_name.split(".")
        module = __import__(".".join(parts[:-1]))
        for comp in parts[1:]:
            factory = getattr(module, comp)
        return factory

    def __init__(self):
        pass

    @abstractmethod
    def create_link(self, caption, url):
        pass

    @abstractmethod
    def create_tray(self, caption):
        pass

    @abstractmethod
    def create_page(self, title, author):
        pass
