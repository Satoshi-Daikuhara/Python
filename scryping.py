import requests
from bs4 import BeautifulSoup

# r = requests.get('https://news.yahoo.co.jp')
#
# print(r.headers)
# print("---------")
# print(r.encoding)
# print(r.content)

# html = "<h1>sayhello</h1>,<h1>saysay</h1>,<h2>say</h2>"

# 第一引数に実際に解析したいもの
# 第二引数にパーサを指定
# パーサとは何をもとに解析するかという事で、この場合はhtmlなのでhtml.parserとする
# soup = BeautifulSoup(html, "html.parser")

# CSSセクレタを指定
# print(soup.select("h1"))

# soup = BeautifulSoup(r.content, "html.parser")

# 主要ニュースを取ってくる
# print(soup.find("div", id="tpc_maj"))

# 主要ニュースのタイトルを取ってくる（テキストだけを取ってくる）
# print(soup.find("div", id="tpc_maj").text)


url = "http://www.nikkei.com/markets/kabu/"

r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, "html.parser")

span = soup.find_all("span")

nikkei_heikin = ""

for tag in span:
    try:
        string_ = tag.get("class").pop(0)

        if string_ in "mkc-stock_prices":
            nikkei_heikin = tag.string
            break

    except:
        pass

print(nikkei_heikin)
