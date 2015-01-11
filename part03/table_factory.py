# coding: utf-8

from factory import Factory, Link, Tray, Page

class TableFactory(Factory):
    def create_link(caption, url):
        return TableLink(caption, url)

    def create_tray(caption):
        return TableTray(caption)

    def create_page(title, author):
        return TablePage(title, author)

class TableLink(Link):
    def make_html(self):
        return '  <td><a href="' + self._url + '">' + self._caption + '</a></td>\n'

class TableTray(Tray):
    def make_html(self):
        buffer = ""
        buffer += "<td>"
        buffer += '<table width="100" border="1"><tr>'
        buffer += '<td bgcolor="#cccccc" align="center" colspan="' + str(len(self._tray)) + '"><b>' + self._caption + '</b></td>'
        buffer += "</tr>\n"
        buffer += "<tr>\n"
        for item in self._tray:
            buffer += item.make_html()
        buffer += "</tr></table>\n"
        buffer += "</td>\n"
        return buffer

class TablePage(Page):
    def make_html(self):
        buffer = ""
        buffer += "<html><head><title>" + self._title + "</title></head>\n"
        buffer += "<body>\n"
        buffer += "<h1>" + self._title + "</h1>\n"
        buffer += '<table width="80" border="3">\n'
        for item in self._content:
            buffer += "<tr>" + item.make_html() + "</tr>"
        buffer += "</table>\n"
        buffer += "<hr><address>" + self._author + "</address>\n"
        buffer += "</body></html>\n"
        return buffer

