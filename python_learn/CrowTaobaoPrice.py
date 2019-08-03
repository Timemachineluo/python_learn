import requests
import re
 
def getHTMLText(url):
    # 防止淘宝反爬虫，需要更改headers和cookies
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    cookies={}
    coo = 'thw=cn; t=ea4b85c1a1f5fad176783e0e03047589; enc=Y%2FAwCrwT%2BZ%2FJt%2BWdYzh3MFpzddjjF7mjIJs%2B%2FJE2SBmV5vrfoeEe9lOhY5wexDirNE0cUnPZSrY85sAAipwcEA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=1fe0a9c0c79e07cf8b3d8402565556de; _tb_token_=f8378f34603f7; alitrackid=www.taobao.com; swfstore=200842; cna=J4+DFWifwV4CASQ8q5KSe9z8; v=0; unb=2950533116; uc3=id2=UUGnyhBTfjqagg%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=EE47%2F61KDFPgRnjr&vt3=F8dBy32m0NOpP02itmU%3D; csg=f9759db1; lgc=spongebob%5Cu4E36k; cookie17=UUGnyhBTfjqagg%3D%3D; dnk=spongebob%5Cu4E36k; skt=3a9682d5f8c6c10e; existShop=MTU2NDQ5ODgxMg%3D%3D; uc4=nk4=0%40Epd97FTUXaKmKmpaIq%2BSFzGVNpLq3Yk%3D&id4=0%40U2OQ3b3TofkLuf34cI6sjDmmbxOV; tracknick=spongebob%5Cu4E36k; _cc_=UIHiLt3xSw%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=k6b; _nk_=spongebob%5Cu4E36k; cookie1=UNQ%2FhDkzb04M4iLKC2gQwxhxEZfIgDEDzIrACLWVI%2FM%3D; JSESSIONID=EA17DB299CC4898B88665FD74C2B81FA; lastalitrackid=login.taobao.com; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UIHiLt3xTIkz&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTaHPwJ8DW7OA%3D%3D&tag=8&lng=zh_CN; mt=ci=1_1; whl=-1%260%260%261564498828404; isg=BG5usUWgvxkvLss7r98AFBkZv8TwxzMIuCIxopg1tHEsew_VAv4keWU5M6cyoyqB; l=cBEAHeJVqj3LBpWoBOfw5uI8LRbOfQAbzsPzw4OG0ICP9_C65M4hWZFxIjLBCnGVp6pe-35fHFhYBeYBqsXtHxoD2j-la'
    for line in coo.split(';'):
        name,value = line.strip().split('=',1)
        cookies[name] = value
    try:
        r = requests.get(url, headers=headers, cookies=cookies, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
     
def parsePage(ilt, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price , title])
    except:
        print("")
 
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
         
def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    printGoodsList(infoList)
     
main()