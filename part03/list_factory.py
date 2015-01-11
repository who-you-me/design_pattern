# coding: utf-8

from factory import Factory, Link, Tray, Page

class ListFactory(Factory):
    def create_link(caption, url):
        return ListLink(caption, url)

    def create_tray(caption):
        return ListTray(caption)

    def create_page(title, author):
        return ListPage(title, author)

class ListLink(Link):
    def make_html(self):
        return '  <li><a href="' + self._url + '">' + self._caption + '</a></li>\n'

class ListTray(Tray):
    def make_html(self):
        buffer = ""
        buffer += "<li>\n"
        buffer += self._caption + "\n"
        buffer += "<ul>\n"
        for item in self._tray:
            buffer += item.make_html()
        buffer += "</ul>\n"
        buffer += "</li>\n"
        return buffer

class ListPage(Page):
    def make_html(self):
        buffer = ""
        buffer += "<html><head><title>" + self._title + "</title></head>\n"
        buffer += "<body>\n"
        buffer += "<h1>" + self._title + "</h1>\n"
        buffer += "<ul>\n"
        for item in self._content:
            buffer += item.make_html()
        buffer += "</ul>\n"
        buffer += "<hr><address>" + self._author + "</address>\n"
        buffer += "</body></html>\n"
        return buffer

