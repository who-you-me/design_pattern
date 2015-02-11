# coding: utf-8

from abc import ABCMeta, abstractmethod
import re

class Node(object, metaclass=ABCMeta):
    @abstractmethod
    def parse(self, context):
        pass

# <program> ::= program <command list>
class ProgramNode(Node):
    def __init__(self):
        self.__command_list_node = None

    def parse(self, context):
        context.skip_token("program")
        self.__command_list_node = CommandListNode()
        self.__command_list_node.parse(context)

    def __str__(self):
        return "[program {}]".format(self.__command_list_node)

# <command list> ::= <command>* end
class CommandListNode(Node):
    def __init__(self):
        self.__list = []

    def parse(self, context):
        while True:
            if not context.current_token():
                raise ParseException("Missing 'end'")
            elif context.current_token() == "end":
                context.skip_token("end")
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self.__list.append(command_node)

    def __str__(self):
        return "[{}]".format(", ".join([str(l) for l in self.__list]))

# <command> ::= <repeat command> | <primitive command>
class CommandNode(Node):
    def __init__(self):
        self.__node = None

    def parse(self, context):
        if context.current_token() == "repeat":
            self.__node = RepeatCommandNode()
            self.__node.parse(context)
        else:
            self.__node = PrimitiveCommandNode()
            self.__node.parse(context)

    def __str__(self):
        return str(self.__node)

# <repeat command> :== repeat <number> <command list>
class RepeatCommandNode(Node):
    def __init__(self):
        self.__number = None
        self.__command_list_node = []

    def parse(self, context):
        context.skip_token("repeat")
        self.__number = context.current_number()
        context.next_token()
        self.__command_list_node = CommandListNode()
        self.__command_list_node.parse(context)

    def __str__(self):
        return "[repeat {} {}]".format(self.__number, self.__command_list_node)

# <primitive command> ::= go | right | left
class PrimitiveCommandNode(Node):
    def __init__(self):
        self.__name = ""

    def parse(self, context):
        self.__name = context.current_token()
        context.skip_token(self.__name)
        if self.__name not in ("go", "right", "left"):
            raise ParseException("{} is undefined".format(self.__name))

    def __str__(self):
        return self.__name

class Context(object):
    def __init__(self, text):
        self.__current_token = None
        self.__tokenizer = StringTokenizer(text)
        self.next_token()

    def next_token(self):
        if self.__tokenizer.has_more_token():
            self.__current_token = self.__tokenizer.next_token()
        else:
            self.__current_token = None
        return self.__current_token

    def current_token(self):
        return self.__current_token

    def skip_token(self, token):
        if token != self.__current_token:
            raise ParseException("Warning: {} is expected, but {} is found".format(token, self.__current_token))
        self.next_token()

    def current_number(self):
        try:
            number = int(self.__current_token)
        except ValueError as error:
            raise ParseException(error)
        return number

class StringTokenizer(object):
    def __init__(self, text):
        self.__tokens = re.split(r"[ \t\n\r\f]", text)

    def next_token(self):
        token = self.__tokens[0]
        self.__tokens = self.__tokens[1:]
        return token

    def has_more_token(self):
        return len(self.__tokens) > 0

class ParseException(Exception):
    pass

if __name__ == "__main__":
    with open("program.txt") as f:
        for text in f:
            text = text.strip()
            print('text = "{}"'.format(text))
            node = ProgramNode()
            node.parse(Context(text))
            print("node = {}".format(node))
