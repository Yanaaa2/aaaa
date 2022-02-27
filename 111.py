import requests
from lxml import  etree
from urllib.parse import urljoin
def qishiye(url):#解析拿到的起始html url
    res=requests.get(url)
    res.encoding=res.apparent_encoding
    html=res.text
    return html
def neirong_xinwen(html):#找出作者内容来源发布时间
    s=etree.HTML(html)
    new={}
    a=s.xpath("//h2/text()")[0]
    b=s.xpath("//div[@class='zz']/text()")[0].split()[0].lstrip("作者：")
    c=s.xpath("//div[@class='zz']/text()")[0].split()[1].lstrip("来源：")
    d=s.xpath("//div[@class='zz']/text()")[1].split()[0]
    d1=str(d).lstrip("发布时间：")
    e=s.xpath("//*[@id='vsb_content']//text()")
    e1="".join(x.strip() for x in e)
    new['a']=a
    new['b']=b
    new['c']=c
    new['d']=d1
    new['e']=e1
    return new
def urls_spider(url):
    urls=[]
    n= int(input("请输入起始页："))
    t= int(input("请输入起始页："))
    for i in range(n,t+1):
        fullname=str(i)+".html"
        fullname_quan=url+str(fullname)
        html=qishiye(fullname_quan)
        s=etree.HTML(html)
    result=s.xpath("//div[@class='right-1']//li/a/@href")
    for u in result:
        urls.append(urljoin(base_url,u))
    return urls
if __name__=="__main__":
    base_url="https://www.zjitc.net/"
    url="https://www.zjitc.net/xwzx/tztg/"
    uls=urls_spider(url)
    news=[]
    for u in uls:
        news.append(neirong_xinwen(qishiye(u)))
        print(news)