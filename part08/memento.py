# coding: utf-8

from game.memento import Memento
from game.gamer import Gamer
import time

if __name__ == "__main__":
    gamer = Gamer(100)
    memento = gamer.create_memento()
    for i in range(100):
        print ("==== {}".format(i))
        print("現状:{}".format(gamer))

        gamer.bet()

        print("所持金は{}円になりました。".format(gamer.get_money()))

        if gamer.get_money() > memento.get_money():
            print("    （だいぶ増えたので、現在の状態を保存しておこう）")
            memento = gamer.create_memento()
        elif gamer.get_money() < memento.get_money() / 2:
            print("    （だいぶ減ったので、以前の状態に復帰しよう）")
            gamer.restore_memento(memento)

        time.sleep(1)
        print()
