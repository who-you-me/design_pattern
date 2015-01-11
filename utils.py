# coding: utf-8

import unicodedata

def string_width(string):
    width = 0
    for ch in string:
        char_width = unicodedata.east_asian_width(ch)
        if char_width in "WFA":
            width += 2
        else:
            width += 1

    return width
