# coding: utf-8

from framework import Product, Factory

class IDCard(Product):
    def __init__(self, owner):
        print("{}のカードを作ります。".format(owner))
        self.owner = owner

    def use(self):
        print("{}のカードを使います。".format(self.owner))

class IDCardFactory(Factory):
    def __init__(self):
        self.owners = []

    def create_product(self, owner):
        return IDCard(owner)

    def register_product(self, product):
        self.owners.append(product.owner)

