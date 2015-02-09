# coding: utf-8

from pagemaker.database import Database
from pagemaker.htmlwriter import HtmlWriter

class PageMaker(object):
    @classmethod
    def make_welcome_page(cls, mail_addr, filename):
        try:
            mail_prop = Database.get_properties("maildata")
            username = mail_prop.get(mail_addr)
            f = open(filename, "w")
            writer = HtmlWriter(f)
            writer.title("Welcome to {}'s page!".format(username))
            writer.paragraph("{}のページヘようこそ。".format(username))
            writer.paragraph("メールまっていますね。")
            writer.mailto(mail_addr, username)
            writer.close()
            print("{} is created for {} ({})".format(filename, mail_addr, username))
        except IOError as error:
            print(error)
        finally:
            f.close()

