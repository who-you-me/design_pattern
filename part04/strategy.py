# coding: utf-8

import sys

from abc import ABCMeta, abstractmethod

import random

class Hand(object):
    HANDVALUE_GOO = 0
    HANDVALUE_CHO = 1
    HANDVALUE_PAA = 2

    class __Hand(object):
        name = ["グー", "チョキ", "パー"]

        def __init__(self, hand_value):
            self.__hand_value = hand_value

        def is_stronger_than(self, hand):
            return self.__fight(hand) == 1

        def is_weaker_than(self, hand):
            return self.__fight(hand) == -1

        def __fight(self, hand):
            if self == hand:
                return 0
            elif (self.__hand_value + 1) % 3 == hand.__hand_value:
                return 1
            else:
                return -1

        def __str__(self):
            return self.name[self.__hand_value]

    hand = [ __Hand(HANDVALUE_GOO),
        __Hand(HANDVALUE_CHO),
        __Hand(HANDVALUE_PAA),
    ]

    @classmethod
    def get_hand(cls, hand_value):
        return cls.hand[hand_value]

class Strategy(object, metaclass=ABCMeta):
    @abstractmethod
    def next_hand(self):
        pass

    @abstractmethod
    def study(self, win):
        pass

class WinningStrategy(Strategy):
    def __init__(self, seed):
        random.seed(seed)
        self.__won = False
        self.__prev_hand = None

    def next_hand(self):
        if not self.__won:
            self.__prev_hand = Hand.get_hand(random.randint(0, 2))
        return self.__prev_hand

    def study(self, win):
        self.__won = win

class ProbStrategy(Strategy):
    def __init__(self, seed):
        random.seed(seed)
        self.__prev_hand_value = 0
        self.__current_hand_value = 0
        self.__history = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]

    def next_hand(self):
        bet = random.randint(0, self.__get_sum(self.__current_hand_value))
        hand_value = 0
        if (bet < self.__history[self.__current_hand_value][0]):
            hand_value = 0
        elif (bet < self.__history[self.__current_hand_value][0] + self.__history[self.__current_hand_value][1]):
            hand_value = 1
        else:
            hand_value = 2
        self.__prev_hand_value = self.__current_hand_value
        self.__current_hand_value = hand_value
        return Hand.get_hand(hand_value)

    def __get_sum(self, hv):
        sum = 0
        for i in range(3):
            sum += self.__history[hv][i]
        return sum

    def study(self, win):
        if win:
            self.__history[self.__prev_hand_value][self.__current_hand_value] += 1
        else:
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 1) % 3] += 1
            self.__history[self.__prev_hand_value][(self.__current_hand_value + 2) % 3] += 1

class Player(object):
    def __init__(self, name, strategy):
        self.__name = name
        self.__strategy = strategy
        self.__win_count = 0
        self.__lose_count = 0
        self.__game_count = 0

    def next_hand(self):
        return self.__strategy.next_hand()

    def win(self):
        self.__strategy.study(True)
        self.__win_count += 1
        self.__game_count += 1

    def lose(self):
        self.__strategy.study(False)
        self.__lose_count += 1
        self.__game_count += 1

    def even(self):
        self.__game_count += 1

    def __str__(self):
        return "[{}:{} games, {} win, {} lose]".format(
            self.__name, self.__game_count,
            self.__win_count, self.__lose_count
        )

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python strategy.py randomseed1 randomseed2")
        print("Example: python strategy.py 314 15")
        sys.exit()

    seed1 = int(sys.argv[1])
    seed2 = int(sys.argv[2])
    player1 = Player("Taro", WinningStrategy(seed1))
    player2 = Player("Hana", ProbStrategy(seed2))
    for i in range(10000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()
        if next_hand1.is_stronger_than(next_hand2):
            print("Winner:", player1, sep="")
            player1.win()
            player2.lose()
        elif next_hand2.is_stronger_than(next_hand1):
            print("Winner:", player2, sep="")
            player1.lose()
            player2.win()
        else:
            print("Even...")
            player1.even()
            player2.even()
    print("Total result:")
    print(player1)
    print(player2)
