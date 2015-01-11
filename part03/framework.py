# coding: utf-8

from abc import ABCMeta, abstractmethod

import copy

class Product(object, metaclass=ABCMeta):
    @abstractmethod
    def use(self, string):
        pass

class Manager(object):
    def __init__(self):
        self.__showcase = {}

    def register(self, name, proto):
        self.__showcase[name] = proto

    def create(self, proto_name):
        product = self.__showcase.get(proto_name)
        return copy.deepcopy(product)

