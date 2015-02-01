# coding: utf-8

from abc import ABCMeta, abstractmethod

class Trouble(object):
    def __init__(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def __str__(self):
        return "[Trouble {}]".format(self.__number)

class Support(object, metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name
        self.__next = None

    def set_next(self, next):
        self.__next = next
        return next

    def support(self, trouble):
        if self._resolve(trouble):
            self._done(trouble)
        elif self.__next:
            self.__next.support(trouble)
        else:
            self._fail(trouble)

    def __str__(self):
        return "[{}]".format(self.__name)

    @abstractmethod
    def _resolve(self, trouble):
        pass

    def _done(self, trouble):
        print("{} is resolved by {}.".format(trouble, self))

    def _fail(self, trouble):
        print("{} cannot be resolved.".format(trouble))

class NoSupport(Support):
    def _resolve(self, trouble):
        return False

class LimitSupport(Support):
    def __init__(self, name, limit):
        Support.__init__(self, name)
        self.__limit = limit

    def _resolve(self, trouble):
        if trouble.get_number() < self.__limit:
            return True
        else:
            return False

class OddSupport(Support):
    def _resolve(self, trouble):
        if trouble.get_number() % 2 == 1:
            return True
        else:
            return False

class SpecialSupport(Support):
    def __init__(self, name, number):
        Support.__init__(self, name)
        self.__number = number

    def _resolve(self, trouble):
        if trouble.get_number() == self.__number:
            return True
        else:
            return False

if __name__ == "__main__":
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 100)
    charlie = SpecialSupport("Charlie", 429)
    diana = LimitSupport("Diana", 200)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)
    alice.set_next(bob).set_next(charlie).set_next(diana).set_next(elmo).set_next(fred)
    for i in range(0, 500, 33):
        alice.support(Trouble(i))
