import requests
from lxml import etree

#我们邀抓取的页面链接
url='http://zhjw.scu.edu.cn/student/integratedQuery/scoreQuery/allPassingScores/index'

#用requests库的get方法下载网页
r=requests.get(url).text

#解析网页并且定位短评
s=etree.HTML(r)
#//*[@id="content"]/div/div[1]/ol/li[2]/div/div[2]/div[1]/a/span[1]
file=s.xpath('//*[@id="tab4"]/div/div/table/tbody/tr[1]/td[3]')

#打印抓取的信息

print(file)
