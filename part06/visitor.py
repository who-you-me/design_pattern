# coding: utf-8

from abc import ABCMeta, abstractmethod

class Visitor(object, metaclass=ABCMeta):
    def visit(self, obj):
        if isinstance(obj, File):
            self._visit_file(obj)
        elif isinstance(obj, Directory):
            self._visit_directory(obj)

    @abstractmethod
    def _visit_file(self, file):
        pass

    @abstractmethod
    def _visit_directory(self, directory):
        pass

class Element(object, metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Entry(Element, metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry):
        raise FileTreatmentException

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

    def accept(self, visitor):
        visitor.visit(self)

class Directory(Entry):
    def __init__(self, name):
        self.__name = name
        self.__dir = []

    def get_name(self):
        return self.__name

    def get_size(self):
        size = 0
        for entry in self.iterator():
            size += entry.get_size()
        return size

    def add(self, entry):
        self.__dir.append(entry)
        return self

    def iterator(self):
        return self.__dir

    def accept(self, visitor):
        visitor.visit(self)

class ListVisitor(Visitor):
    def __init__(self):
        self.__current_dir = ""

    def _visit_file(self, file):
        print("{}/{}".format(self.__current_dir, file))

    def _visit_directory(self, directory):
        print("{}/{}".format(self.__current_dir, directory))
        save_dir = self.__current_dir
        self.__current_dir = "{}/{}".format(self.__current_dir, directory.get_name())
        for entry in directory.iterator():
            entry.accept(self)
        self.__current_dir = save_dir

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
    root_dir.accept(ListVisitor())

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
    root_dir.accept(ListVisitor())
