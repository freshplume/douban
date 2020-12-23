
import bs4
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="

    #1、爬取网页
    datalist = getdata(baseurl)
    savepath = ".\\doubanmoivetop250.xls"
    #2、解析数据

    #3、保存数据
    saveData(savepath)

#爬取网页
def getdata(baseurl):
    datalist = []
    return datalist

#得到指定一个URL网页的内容
def askURL(url)
    head = {}
    head["User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0"]

#保存数据
def saveData(savepath):
    print()



if __name__ == "__main__":
    main()







