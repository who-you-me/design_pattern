import sys
from factory import Factory

factory = Factory.get_factory(sys.argv[1])

asahi = factory.create_link("朝日新聞", "http://www.asahi.com/")
yomiuri = factory.create_link("読売新聞", "http://www.yomiuri.co.jp/")

us_yahoo = factory.create_link("Yahoo!", "http://www.yahoo.com/")
jp_yahoo = factory.create_link("Yahoo!Japan", "http://www.yahoo.co.jp/")
excite = factory.create_link("Excite", "http://www.excite.com/")
google = factory.create_link("Google", "http://www.google.com/")

tray_news = factory.create_tray("新聞")
tray_news.add(asahi)
tray_news.add(yomiuri)

tray_yahoo = factory.create_tray("Yahoo!")
tray_yahoo.add(us_yahoo)
tray_yahoo.add(jp_yahoo)

tray_search = factory.create_tray("サーチエンジン")
tray_search.add(tray_yahoo)
tray_search.add(excite)
tray_search.add(google)

page = factory.create_page("LinkPage", "結城 浩")
page.add(tray_news)
page.add(tray_search)
page.output()
