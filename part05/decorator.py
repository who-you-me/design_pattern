# coding: utf-8

from abc import ABCMeta, abstractmethod

import utils

class Display(object, metaclass=ABCMeta):
    @abstractmethod
    def get_columns(self):
        pass

    @abstractmethod
    def get_rows(self):
        pass

    @abstractmethod
    def get_row_text(self, row):
        pass

    def show(self):
        for i in range(self.get_rows()):
            print(self.get_row_text(i))

class StringDisplay(Display):
    def __init__(self, string):
        self.__string = string

    def get_columns(self):
        return utils.string_width(self.__string)

    def get_rows(self):
        return 1

    def get_row_text(self, row):
        if row == 0:
            return self.__string
        else:
            return None

class Border(Display):
    def __init__(self, display):
        self.display = display

class SideBorder(Border):
    def __init__(self, display, ch):
        Border.__init__(self, display)
        self.__border_char = ch

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return self.display.get_rows()

    def get_row_text(self, row):
        return self.__border_char + self.display.get_row_text(row) + self.__border_char

class FullBorder(Border):
    def __init__(self, display):
        Border.__init__(self, display)

    def get_columns(self):
        return 1 + self.display.get_columns() + 1

    def get_rows(self):
        return 1 + self.display.get_rows() + 1

    def get_row_text(self, row):
        if row == 0:
            return "+" + self.__make_line("-", self.display.get_columns()) + "+"
        elif row == self.display.get_rows() + 1:
            return "+" + self.__make_line("-", self.display.get_columns()) + "+"
        else:
            return "|" + self.display.get_row_text(row - 1) + "|"

    def __make_line(self, ch, count):
        buf = ""
        for i in range(count):
            buf += ch
        return buf

if __name__ == "__main__":
    b1 = StringDisplay("Hello, world.")
    b2 = SideBorder(b1, "#")
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()
    b4 = SideBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay("こんにちは。"),
                    ),
                    "*"
                )
            ),
            "/"
        )
    b4.show()
