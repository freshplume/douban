
import bs4
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = "https://movie.douban.com/top250?start="

    #1、爬取网页
    datalist = getdata(baseurl)
    savepath = ".\\doubanmoivetop250.xls"
    # dbpath = "movie.db"

    #3、保存数据
    saveData(datalist,savepath)
    # saveData2DB(datalist, dbpath)
    # askURL("https://movie.douban.com/top250?start=")

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')             #创建正则表达式对象，表示规则（字符串模式）
#影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)        #re.S让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*?)</span>')
#影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片评价人数
findJudge = re.compile(r"<span>(\d*)人评价</span>")
#影片概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取网页
def getdata(baseurl):
    datalist = []
    for i in range(0,10):   #调用获取页面信息的函数10次
        url = baseurl + str(i*25)
        html = askURL(url)  #保存获取到的网页源码

        # 2、逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):    #查找符合要求的字符串，形成列表
            #print(item)  #测试查看电影信息
            data = []     #保存一部电影全部信息
            item = str(item)

            link = re.findall(findLink,item)[0] #re库用来通过正则表达式查找指定的字符串
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle,item)
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")  #去掉无关的符号
                data.append(otitle.strip())
            else:
                data.append(titles[0])
                data.append(' ')

            rating = re.findall(findRating,item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            # bd = re.sub('/'," ",bd)
            bd = bd.replace("\xa0/\xa0","")
            bd = bd.replace("\xa0\xa0\xa0","")
            data.append(bd.strip())

            # print(data)
            datalist.append(data)






    return datalist

#得到指定一个URL网页的内容
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


#保存数据
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="UTF-8",style_compression=0)  # 创建wookbook对象
    sheet = book.add_sheet('sheet1',cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        # print(i)
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #数据

    book.save(savepath)    #保存

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into movie250 (
                info_link,pic_link,cname,oname,score,rated,instroduction,info)
                values(%s)'''%",".join(data)
        # print(sql)
        c.execute(sql)
        conn.commit()
    c.close()
    conn.close()

def init_db(dbpath):
    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar ,
        oname varchar ,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    c = conn.cursor()
    c.execute(sql)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
    # init_db("movietest.db")
    print("抓取完毕")






