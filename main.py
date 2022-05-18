#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Author: p1yang
#@File: main.py
#@Time: 2022/05/17 08:36:02
import os
from pydoc import Doc
from telnetlib import DO
from click import style
import requests
import re
import urllib
import time
from docx import Document

#
kuchuan_search_app = "https://android.kuchuan.com/searchappallmarket?kw={}&page=1&count=20&market=0&date={}"
kuchuan_search_appInfo = "https://android.kuchuan.com/totaldownload?packagename={}&date={}"
kuchuan_search_developer = "https://android.kuchuan.com/page/detail/download?package={}&infomarketid=10&site=0#!/sum/{}"
kuchuan_info = "https://android.kuchuan.com/page/detail/download?package={}&infomarketid=1&site=0#!/sum/{}"
app_name = "" #软件名
app_version = "" #版本
app_hash = "" #hash
package_name = "" #包名
totla_downloads = 0 #下载量
developer = "" #开发商名称
leak_type = "" #漏洞类型，需要自行填写
is_open = "" #发布情况
hazard_level = ""#危害等级
addr = "" #所属省份

def getDate():
    date = int( round(time.time() * 1000)) - int(int(time.time() - time.timezone) % 86400)*1000
    return date

# 获取总下载量
def getTotalDownloads():
    url = kuchuan_search_appInfo.format(package_name,getDate())
    head_data = {
        'Accept': 'application/json, text/plain, */*',
        'Cookie': '请自行填写，有问题联系QQ：397712823',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'android.kuchuan.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
        'Referer': 'https://android.kuchuan.com/page/detail/download?package={}&infomarketid=10&site=0'.format(package_name),
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = requests.get(url,headers=head_data).json()
    #data = {"status":200, "msg":"请求成功", "data":{"联想":4,"OPPO":195,"华为":10000,"应用宝":23,"魅族":20,"vivo":1908}}
    nums = data["data"]
    downloads = 0
    for num in nums:
        downloads += nums[num]
    return downloads


#获取软件包名
def getPackageName():
    app_name_hex = urllib.parse.quote(app_name)
    head_data = {
        "Accept": "application/json, text/plain, */*",
        "Cookie": "请自行填写，有问题联系QQ：397712823",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Host": "android.kuchuan.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "Referer": "https://android.kuchuan.com/page/detail/searchResult?kw={}&site=0&marketId=0".format(app_name_hex),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest"
    }
    url = kuchuan_search_app.format(app_name_hex,getDate())
    data = requests.get(url,headers=head_data).json()
    infos = data['data']['result']
    package_name = ""
    for info in infos:
        if app_name == info["title"]:
            package_name = info["packageName"]
            break
    return package_name

#获取开发商名称
def getDeveloper():
    url = kuchuan_search_developer.format(package_name,package_name)
    head_data = {
        'Cookie': '请自行填写，有问题联系QQ：397712823',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Host': 'android.kuchuan.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    data = requests.get(url,headers=head_data).text
    s = re.findall(r'"developer":"[\u4e00-\u9fa5]+"',data)
    return s[0].split('"')[-2]

#获取hash，使用的是md5
def getHash(fileName):
    res = os.popen("md5 "+fileName).read()
    return res[res.index("=")+2:-1]
    
def printInfo():
    print("[软件名]："+app_name)        
    print("[软件版本]："+app_version)
    print("[软件哈希]："+app_hash)
    print("[软件包名]："+package_name)
    print("[下载量]："+str(totla_downloads))
    print("[开发商]："+developer)

def createReport():
    newDoc = Document()
    newDoc.add_heading("{} {}APP {}版本存在{}问题".format(developer,app_name,app_version,leak_type),level=0)
    newDoc.add_paragraph("一、受影响产品名称：{}{}APP {} 安卓版".format(developer,app_name,app_version))
    newDoc.add_paragraph("二、网络产品提供者/影响企业的所属省份：{}".format(addr))
    newDoc.add_paragraph("三、APP包名：{}".format(package_name))
    newDoc.add_paragraph("四、APP哈希值：MD5:{}".format(app_hash))
    newDoc.add_paragraph("五、漏洞成因类型：{}问题".format(leak_type))
    newDoc.add_paragraph("六、发布情况：{}".format(is_open))
    newDoc.add_paragraph("七、危害等级：{}".format(hazard_level))
    newDoc.add_paragraph("八、总下载量：{}".format(str(totla_downloads)))
    newDoc.add_paragraph("这里放截图")
    newDoc.add_paragraph("九、漏洞简介\n")
    newDoc.save("{}/{}存在{}问题.docx".format(app_name,app_name,leak_type))

if __name__ == "__main__":
    print("[*]开始获取app信息")
    s = os.listdir()
    name = ""
    for i in s:
        if ".apk" in i:
            name = i
            app_name = i[:i.index("_")]
            app_version = i[i.index("_")+1:i.index("apk")-1]
            app_hash = getHash(i)
            break
    package_name = getPackageName()
    if package_name != "":
        totla_downloads = getTotalDownloads()
        developer = getDeveloper()
    else:
        print("未查到该软件，请手动查询")
    printInfo()
    print("下面请输入其他信息")
    addr = input("[所属省份]：")
    leak_type = input("[漏洞类型]：")
    is_open = input("[发布情况]：")
    hazard_level = input("[危害等级]：")
    print("[*]开始生成报告")
    os.mkdir(app_name)
    createReport()
    os.system("mv {} ./{}/".format(i,app_name))
    print("[*]报告生成完毕，手动补充漏洞截图和简介")
    print(kuchuan_info.format(package_name,package_name))