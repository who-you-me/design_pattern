# coding: utf-8

from bigchar import BigChar

class BigCharFactory(object):
    class __BigCharFactory(object):
        def __init__(self):
            self.__pool = {}

        def get_big_char(self, charname):
            charname = str(charname)
            bc = self.__pool.get(charname)
            if not bc:
                bc = BigChar(charname)
                self.__pool[charname] = bc
            return bc

    singleton = __BigCharFactory()

    @classmethod
    def get_instance(cls):
        return cls.singleton

