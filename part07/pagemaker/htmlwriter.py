# coding: utf-8

class HtmlWriter(object):
    def __init__(self, writer):
        self.__writer = writer

    def title(self, title):
        self.__writer.write("<html>")
        self.__writer.write("<head>")
        self.__writer.write("<title>{}</title>".format(title))
        self.__writer.write("</head>")
        self.__writer.write("<body>\n")
        self.__writer.write("<h1>{}</h1>\n".format(title))

    def paragraph(self, msg):
        self.__writer.write("<p>{}</p>\n".format(msg))

    def link(self, href, caption):
        self.paragraph('<a href="{}">{}</a>'.format(href, caption))

    def mailto(self, mail_addr, username):
        self.link("mailto:{}".format(mail_addr), username)

    def close(self):
        self.__writer.write("</body>")
        self.__writer.write("</html>\n")
        self.__writer.close()
