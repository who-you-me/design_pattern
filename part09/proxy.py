# coding: utf-8

from abc import ABCMeta, abstractmethod
import time

class Printable(object, metaclass=ABCMeta):
    @abstractmethod
    def set_printer_name(self, name):
        pass

    @abstractmethod
    def get_printer_name(self):
        pass

    @abstractmethod
    def print(self, string):
        pass

class Printer(Printable):
    def __init__(self, name):
        if name:
            self.__name = name
            self.__heavy_job("Printerのインスタンス（{}）を生成中".format(name))
        else:
            self.__heavy_job("Printerのインスタンスを生成中")

    def set_printer_name(self, name):
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def print(self, string):
        print("=== {} ===".format(self.__name))
        print(string)

    def __heavy_job(self, msg):
        print(msg)
        for i in range(5):
            time.sleep(1)
            print(".", end="", flush=True)
        print("完了。")

class PrinterProxy(Printable):
    def __init__(self, name):
        self.__name = name
        self.__real = None

    def set_printer_name(self, name):
        if self.__real:
            self.__real.set_printer_name(name)
        self.__name = name

    def get_printer_name(self):
        return self.__name

    def print(self, string):
        self.__realize()
        self.__real.print(string)

    def __realize(self):
        if not self.__real:
            self.__real = Printer(self.__name)

if __name__ == "__main__":
    p = PrinterProxy("Alice")
    print("名前は現在{}です".format(p.get_printer_name()))
    p.set_printer_name("Bob")
    print("名前は現在{}です".format(p.get_printer_name()))
    p.print("Hello, world.")


