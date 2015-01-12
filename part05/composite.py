# coding: utf-8

from abc import ABCMeta, abstractmethod

class Entry(object, metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry):
        raise FileTreatmentException

    def print_list(self):
        self._print_list("")

    @abstractmethod
    def _print_list(self, prefix):
        pass

    def __str__(self):
        return "{} ({})".format(self.get_name(), self.get_size())

class File(Entry):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def _print_list(self, prefix):
        print("{}/{}".format(prefix, self))

class Directory(Entry):
    def __init__(self, name):
        self.__name = name
        self.__directory = []

    def get_name(self):
        return self.__name

    def get_size(self):
        return sum([entry.get_size() for entry in self.__directory])

    def add(self, entry):
        self.__directory.append(entry)
        return self

    def _print_list(self, prefix):
        print("{}/{}".format(prefix, self))
        for entry in self.__directory:
            entry._print_list("{}/{}".format(prefix, self.__name))

class FileTreatmentException(Exception):
    pass

if __name__ == "__main__":
    print("Making root entries...")
    root_dir = Directory("root")
    bin_dir = Directory("bin")
    tmp_dir = Directory("tmp")
    usr_dir = Directory("usr")
    root_dir.add(bin_dir)
    root_dir.add(tmp_dir)
    root_dir.add(usr_dir)
    bin_dir.add(File("vi", 10000))
    bin_dir.add(File("latex", 20000))
    root_dir.print_list()

    print()
    print("Making user entries")
    yuki = Directory("yuki")
    hanako = Directory("hanako")
    tomura = Directory("tomura")
    usr_dir.add(yuki)
    usr_dir.add(hanako)
    usr_dir.add(tomura)
    yuki.add(File("diary.html", 100))
    yuki.add(File("Composite.java", 200))
    hanako.add(File("memo.txt", 300))
    tomura.add(File("game.doc", 400))
    tomura.add(File("junk.mail", 500))
    root_dir.print_list()
