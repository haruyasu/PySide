import urllib2
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/markets/kabu/"

html = urllib2.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

span = soup.find_all("span")
nikkei_heikin = ""

for tag in span:
    try:
        string = tag.get("class").pop(0)

        if string in "mkc-stock_prices":
            nikkei_heikin = tag.string
            break
    except:
        pass

print nikkei_heikin