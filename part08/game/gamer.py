# coding: utf-8

from game.memento import Memento
import random

class Gamer(object):
    fruits_name = ["リンゴ", "ぶどう", "バナナ", "みかん"]

    def __init__(self, money):
        self.__money = money
        self.__fruits = []

    def get_money(self):
        return self.__money

    def bet(self):
        dice = random.randint(1, 6)
        if dice == 1:
            self.__money += 100
            print("所持金が増えました")
        elif dice == 2:
            self.__money /= 2
            print("所持金が半分になりました")
        elif dice == 6:
            f = self.__get_fruit()
            print("フルーツ（{}）をもらいました".format(f))
            self.__fruits.append(f)
        else:
            print("何も起こりませんでした。")

    def create_memento(self):
        memento = Memento(self.__money)
        for fruit in self.__fruits:
            if fruit.startswith("おいしい"):
                memento._add_fruit(fruit)
        return memento

    def restore_memento(self, memento):
        self.__money = memento.get_money()
        self.__fruits = memento._get_fruits()

    def __str__(self):
        return "[money = {}, fruits = {}]".format(self.__money, self.__fruits)

    def __get_fruit(self):
        prefix = ""
        if bool(random.getrandbits(1)):
            prefix = "おいしい"
        return prefix + random.choice(Gamer.fruits_name)
