# coding: utf-8

import copy

class Memento(object):
    def __init__(self, money):
        self._money = money
        self._fruits = []

    def get_money(self):
        return self._money

    def _add_fruit(self, fruit):
        self._fruits.append(fruit)

    def _get_fruits(self):
        return copy.deepcopy(self._fruits)

