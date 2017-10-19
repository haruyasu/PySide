import urllib2
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import time

time_flag = True

# while True:
#     if datetime.now().minute != 59:
#         time.sleep(58)
#         continue

f = open('nikkei_heikin.csv', 'a')
writer = csv.writer(f, lineterminator='\n')

# while datetime.now().second != 59:
#     time.sleep(1)
#
# time.sleep(1)

csv_list = []

time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
csv_list.append(time)

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

print time, nikkei_heikin
csv_list.append(nikkei_heikin)
writer.writerow(csv_list)
f.close()



