# -- encoding:utf-8 --
import requests,time,re
from lxml import etree
for i in range(1,41):
    startUrl='http://sh.baletu.com/zhaofang/p%do1a1/?seachId=0&is_rec_house=0&entrance=14&solr_house_cnt=28658'%i
    headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
     }
# #//tr[position()>1]
    r = requests.get(startUrl,headers=headers).text
    html = etree.HTML(r)
    trs = html.xpath("//li[@class = 'listUnit-date clearfix PBA_list_house']")
    num=1
    for i in trs:
        id = i.xpath("./@uniqid")[0]
        hid = i.xpath("./@num")[0]
        title = i.xpath("./div/div/h3/a/@title")[0]
        village = i.xpath("./@name")[0]
        pattern6 =re.compile("^\S*")
        village = re.findall(pattern6,village)
        area0 = i.xpath("./@category")[0]
        pattern5 = re.compile("..$")
        area = re.findall(pattern5,area0)
        type = i.xpath("./@variant")[0]
        price = i.xpath("./@price")[0]
        url = i.xpath("./div/a/@href")[0]
        pattern = re.compile("[0-9]+M²")
        square0 = i.xpath("./div/p/span[2]/text()")
        square = re.findall(pattern,square0[0])
        line_station_meter = i.xpath("./div/div/text()")[9]
        pattern1 = re.compile("距离[0-9]+号线")
        pattern2 = re.compile("距离.*公交站")
        pattern3 = re.compile("[0-9]+米")
        pattern4 = re.compile("公交站|号线|距离|米|M²")
        square = re.sub(pattern4,"",square[0])
        line0= re.findall(pattern1,line_station_meter)
        meter0 =re.findall(pattern3,line_station_meter)
        if meter0:
            meter = re.sub(pattern4,"",meter0[0])
        else:
            meter0 = "0"
        station0 = re.findall(pattern2,line_station_meter)
        if line0:
            line = re.sub(pattern4,"",line0[0])
        else:
            line = "-"
        if station0:
            station = re.sub(pattern4,"",station0[0])
        else:
            station = "-"
        score = i.xpath("./div/div/div/span/text()")[0]
        ratnum = i.xpath("./div/div/div/span/text()")[1]
        addtime=i.xpath("./span/text()") [0]
        time.sleep(0.1)
        with open("./rant_house2.txt","a") as file:
            file.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}{}".format(id,hid,title,village[0],area[0],url,price,type,square,line,station,meter,score,ratnum,addtime,"\n"))
        print(id+"--"+hid+"--"+title+"--"+village[0]+"--"+area[0]+"--"+url+"--"+price+"--"+type+"--"+square+"--"+line+"--"+station+"--"+meter+"--"+score+"--"+ratnum+"--"+addtime)

    
