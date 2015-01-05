# coding: utf-8

class Singleton(object):
    class __Singleton(object):
        def __init__(self):
            print("インスタンスを作成しました。")

    singleton = __Singleton()

    @classmethod
    def get_instance(cls):
        return cls.singleton

if __name__ == "__main__":
    print("Start.")
    obj1 = Singleton.get_instance()
    obj2 = Singleton.get_instance()
    if obj1 == obj2:
        print("obj1とobj2は同じインスタンスです")
    else:
        print("obj1とobj2は同じインスタンスではありません")
    print("End.")

