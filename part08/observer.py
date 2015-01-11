# coding: utf-8

from abc import ABCMeta, abstractmethod

import random
import time

class Observer(object, metaclass=ABCMeta):
    @abstractmethod
    def update(self, generator):
        pass

class NumberGenerator(object, metaclass=ABCMeta):
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self)

    @abstractmethod
    def get_number(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        NumberGenerator.__init__(self)
        self.__number = None

    def get_number(self):
        return self.__number

    def execute(self):
        for i in range(20):
            self.__number = random.randint(0, 49)
            self.notify_observers()

class DigitObserver(Observer):
    def update(self, generator):
        print("DigitObserver:{}".format(generator.get_number()))
        time.sleep(0.1)

class GraphObserver(Observer):
    def update(self, generator):
        print("GraphObserver:", end="")
        count = generator.get_number()
        for i in range(count):
            print("*", end="")
        print("")
        time.sleep(0.1)

if __name__ == "__main__":
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()
