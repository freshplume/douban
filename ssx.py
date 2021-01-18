
import bs4
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = "https://www.b910.cn/tool/1.htm"

    #1、爬取网页
    datalist = getdata(baseurl)

    savepath = ".\\ssx.xls"


    #3、保存数据
    saveData(savepath)

    # askURL("https://movie.douban.com/top250?start=")

#1、
findLink = re.compile(r'<a href="(.*?)">')

def askURL(url):
    head = {    #模拟浏览器头部，向服务器发送消息
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"
    #用户代理表示告诉服务器我们是什么类型的机器，浏览器（本质上是告诉浏览器我们可以接收什么水平的信息）
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr((e,"reason")):
            print(e.reason)
    return html

def saveData():
    print()

if __name__ == "__main__":
    main()
    print("完成")
