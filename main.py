#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Author: p1yang
#@File: main.py
#@Time: 2022/05/17 08:36:02
import os
import requests
import re
import urllib
import time
#
kuchuan_search_app = "https://android.kuchuan.com/searchappallmarket?kw={}&page=1&count=20&market=0&date={}"
kuchuan_search_appInfo = "https://android.kuchuan.com/totaldownload?packagename={}&date={}"
kuchaun_search_developer = "https://android.kuchuan.com/page/detail/download?package={}&infomarketid=10&site=0#!/sum/{}"
app_name = "" #软件名
package_name = "" #包名
app_version = "" #版本
totla_downloads = 0 #下载量
developer = "" #开发商名称

def getDate():
    date = int( round(time.time() * 1000)) - int(int(time.time() - time.timezone) % 86400)*1000
    return date

# 获取总下载量
def getTotalDownloads():
    url = kuchuan_search_appInfo.format(package_name,getDate())
    head_data = {
        'Accept': 'application/json, text/plain, */*',
        'Cookie': 'JSESSIONID=czmd4fxnl5057gt5du2xbg53; sign=FQ1lTeQ1fvPR5bbXOBo%2FSC2ImoHs5cgIOwP%2FE0H1GV9TZ6GH27yPxmhqCenid9SBSaMzn4IdEDMllFjWI5KDZ2WmokCm4%2BEQ7d8OYkbfVLcgw3V0xeyxsWdv5wFUJoaFquHZ9T7%2FGCUVY2OL4mkrPzoZ93zoYr1FsvwCekGG6tM%3D; token=5e651bc936be208f3d064df3cb70daff; _ga=GA1.2.1848213340.1652690100; _gid=GA1.2.1156197270.1652690100; Hm_lpvt_ef5592497ef84b441c6f40f98ada9c4f=1652698279; Hm_lvt_ef5592497ef84b441c6f40f98ada9c4f=1652690097; Hm_lpvt_84ee2face82d86b7584b5bbee44dfbe7=1652698279; Hm_lvt_84ee2face82d86b7584b5bbee44dfbe7=1652689992; CNZZDATA1257619731=708008061-1652680487-https%253A%252F%252Fios.kuchuan.com%252F%7C1652691308; CNZZDATA1260525360=2013768316-1652680496-https%253A%252F%252Fios.kuchuan.com%252F%7C1652691384; CNZZDATA5103679=cnzz_eid%3D77776780-1652681561-https%253A%252F%252Fios.kuchuan.com%252F%26ntime%3D1652692362; accessId=a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900; pageViewNum=26; qimo_seokeywords_a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900=; qimo_seosource_a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900=%E7%AB%99%E5%86%85; qimo_xstKeywords_a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900=; href=https%3A%2F%2Fandroid.kuchuan.com%2Fpage%2Fdetail%2FsearchResult%3Fkw%3D%25E8%25B1%25AB%25E4%25B8%258A%25E8%25A3%2585%26site%3D0%26marketId%3D0; UM_distinctid=180cbfff87121d-0f40ca97baa516-3a62684b-13c680-180cbfff8724ed; uniqueId=daa491ba33f54d68b40d1390b9d57cef',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Host': 'android.kuchuan.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
        'Referer': 'https://android.kuchuan.com/page/detail/download?package={}&infomarketid=10&site=0'.format(package_name),
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest'
    }
    #data = requests.get(url,headers=head_data).json
    data = {"status":200, "msg":"请求成功", "data":{"联想":4,"OPPO":195,"华为":10000,"应用宝":23,"魅族":20,"vivo":1908}}
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
        "Cookie": "sign=B%2BUrf3c7Rsuv%2B8WooKRvagI5flXNeCgXyGlpISdfz78XPGpR1cEjXNl3I5THa8z0bhPFrWHC1BSfcHhtXNah%2FRIkmTNr4wgElTLdVMpNA05S%2FCv21G0LF18INd8g9TPyvberAadcnK03nHzvWMBrjW0zb9EfHwXvuQYCpHYPjGA%3D; token=1156208a52c308ac47822f96aab49b7d; _ga=GA1.2.1848213340.1652690100; _gid=GA1.2.1156197270.1652690100; Hm_lpvt_ef5592497ef84b441c6f40f98ada9c4f=1652695220; Hm_lvt_ef5592497ef84b441c6f40f98ada9c4f=1652690097; Hm_lpvt_84ee2face82d86b7584b5bbee44dfbe7=1652695220; Hm_lvt_84ee2face82d86b7584b5bbee44dfbe7=1652689992; CNZZDATA1257619731=708008061-1652680487-https%253A%252F%252Fios.kuchuan.com%252F%7C1652691308; CNZZDATA1260525360=2013768316-1652680496-https%253A%252F%252Fios.kuchuan.com%252F%7C1652691384; CNZZDATA5103679=cnzz_eid%3D77776780-1652681561-https%253A%252F%252Fios.kuchuan.com%252F%26ntime%3D1652692362; JSESSIONID=dvif117fdomc1u3p6osmozrmk; accessId=a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900; pageViewNum=22; qimo_seokeywords_a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900=; qimo_seosource_a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900=%E7%AB%99%E5%86%85; qimo_xstKeywords_a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900=; href=https%3A%2F%2Fandroid.kuchuan.com%2Fpage%2Fdetail%2FsearchResult%3Fkw%3D%25E8%25B1%25AB%25E4%25B8%258A%25E8%25A3%2585%26site%3D0%26marketId%3D0; UM_distinctid=180cbfff87121d-0f40ca97baa516-3a62684b-13c680-180cbfff8724ed; uniqueId=daa491ba33f54d68b40d1390b9d57cef",
        "Accept-Language": "zh-CN,zh-Hans;q=0.9",
        "Host": "android.kuchuan.com",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
        "Referer": "https://android.kuchuan.com/page/detail/searchResult?kw={}&site=0&marketId=0".format(app_name_hex),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "X-Requested-With": "XMLHttpRequest"
    }
    url = kuchuan_search_app.format(app_name_hex,getDate())
    #data = requests.get(url,headers=head_data).json()
    data = {'status': 200, 'msg': '请求成功', 'data': {'result': [{'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttp%3A%2F%2Fpp.myapp.com%2Fma_icon%2F0%2Ficon_54127626_1631521246%2F96', 'market_id': '10', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttp%3A%2F%2Fpp.myapp.com%2Fma_icon%2F0%2Ficon_54127626_1631521246%2F96', 'market_id': '10', 'packageName': 'com.benben.zhuangxiugong', 'title': '豫上装'}, 'packageName': 'com.benben.zhuangxiugong', 'title': '豫上装'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F675a7b320a9946248d298b1dfacceddf.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F675a7b320a9946248d298b1dfacceddf.png', 'market_id': '18', 'packageName': 'cn.org.camib.www2.WeBrowser.zszx', 'title': '掌上装修'}, 'packageName': 'cn.org.camib.www2.WeBrowser.zszx', 'title': '掌上装修'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F7281789391134bbaa3a785e0aea27286.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F7281789391134bbaa3a785e0aea27286.png', 'market_id': '18', 'packageName': 'com.cxzg.m.zhuangxzs', 'title': '掌上装修装饰'}, 'packageName': 'com.cxzg.m.zhuangxzs', 'title': '掌上装修装饰'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F6f436ded19bd465ab70130f47b771f1f.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F6f436ded19bd465ab70130f47b771f1f.png', 'market_id': '18', 'packageName': 'com.eggpain.zhangshangzhuangxiushangcheng690', 'title': '掌上装修商城'}, 'packageName': 'com.eggpain.zhangshangzhuangxiushangcheng690', 'title': '掌上装修商城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd0a162e7caf5409eb5bf4f60d235eb7d.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd0a162e7caf5409eb5bf4f60d235eb7d.png', 'market_id': '18', 'packageName': 'cn.org.camib.www2.WeBrowser.zszssc', 'title': '掌上装饰商城'}, 'packageName': 'cn.org.camib.www2.WeBrowser.zszssc', 'title': '掌上装饰商城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd85271348e034d89919d36764470b07e_1.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd85271348e034d89919d36764470b07e_1.png', 'market_id': '18', 'packageName': 'com.ddm.shoppingmall', 'title': '掌上装饰城'}, 'packageName': 'com.ddm.shoppingmall', 'title': '掌上装饰城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F7e403bf864314815a62bd50be4aa10de.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F7e403bf864314815a62bd50be4aa10de.png', 'market_id': '18', 'packageName': 'cn.org.camib.www2.WeBrowser.zszxwfns', 'title': '掌上装修网'}, 'packageName': 'cn.org.camib.www2.WeBrowser.zszxwfns', 'title': '掌上装修网'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttp%3A%2F%2Fimg.wdjimg.com%2Fmms%2Ficon%2Fv1%2Ff%2Fcb%2F77f1191ff7b74553597ceacd435aacbf_256_256.png', 'market_id': '17', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttp%3A%2F%2Fimg.wdjimg.com%2Fmms%2Ficon%2Fv1%2Ff%2Fcb%2F77f1191ff7b74553597ceacd435aacbf_256_256.png', 'market_id': '17', 'packageName': 'com.sino.app.advancedB31317', 'title': '掌上装饰城'}, 'packageName': 'com.sino.app.advancedB31317', 'title': '掌上装饰城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd75fde337e2541e5b02a29402ab9fd67.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd75fde337e2541e5b02a29402ab9fd67.png', 'market_id': '18', 'packageName': 'cn.org.camib.WeBrowser.zszsc', 'title': '掌上装饰城'}, 'packageName': 'cn.org.camib.WeBrowser.zszsc', 'title': '掌上装饰城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F686b52b6d73d40ce86393ef91a255c06.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F686b52b6d73d40ce86393ef91a255c06.png', 'market_id': '18', 'packageName': 'cn.org.camib.www2.WeBrowser.zszsw8', 'title': '掌上装饰网'}, 'packageName': 'cn.org.camib.www2.WeBrowser.zszsw8', 'title': '掌上装饰网'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F2ac08f23a57c453f9a052e6ee202a6b5.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F2ac08f23a57c453f9a052e6ee202a6b5.png', 'market_id': '18', 'packageName': 'com.zdweilai.WeBrowser.zszslm', 'title': '掌上装饰联盟'}, 'packageName': 'com.zdweilai.WeBrowser.zszslm', 'title': '掌上装饰联盟'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F5603d6cc7a3e4e4e81e824c486fd64d3.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F5603d6cc7a3e4e4e81e824c486fd64d3.png', 'market_id': '18', 'packageName': 'com.eggpain.zhangshangzhuangxiumenhu3911', 'title': '掌上装修门户'}, 'packageName': 'com.eggpain.zhangshangzhuangxiumenhu3911', 'title': '掌上装修门户'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fecee3ec62ec6442d9038b9fb7cbe1fda.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fecee3ec62ec6442d9038b9fb7cbe1fda.png', 'market_id': '18', 'packageName': 'com.eggpain.zhangshangzhuangshigongcheng2508', 'title': '掌上装饰工程'}, 'packageName': 'com.eggpain.zhangshangzhuangshigongcheng2508', 'title': '掌上装饰工程'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fc34f769e8be64097b002f5bc76ac0317.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fc34f769e8be64097b002f5bc76ac0317.png', 'market_id': '18', 'packageName': 'com.yes.bokai', 'title': '博凯掌上装饰'}, 'packageName': 'com.yes.bokai', 'title': '博凯掌上装饰'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd3f85eda9f344d119c78f116de95b7e2.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fd3f85eda9f344d119c78f116de95b7e2.png', 'market_id': '18', 'packageName': 'com.eggpain.zhangshangzhuangxiudaquan1510', 'title': '掌上装修大全'}, 'packageName': 'com.eggpain.zhangshangzhuangxiudaquan1510', 'title': '掌上装修大全'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F556f81a1bfcd48a28422d11dc3053bbe.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F556f81a1bfcd48a28422d11dc3053bbe.png', 'market_id': '18', 'packageName': 'com.eggpain.zhangshangzhuangshicailiaocheng3065', 'title': '掌上装饰材料城'}, 'packageName': 'com.eggpain.zhangshangzhuangshicailiaocheng3065', 'title': '掌上装饰材料城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F51630f263a0546ca9156b053ec506aaa.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2F51630f263a0546ca9156b053ec506aaa.png', 'market_id': '18', 'packageName': 'com.eggpain.zhangshangzhuangshicailiaowang570', 'title': '掌上装饰材料网'}, 'packageName': 'com.eggpain.zhangshangzhuangshicailiaowang570', 'title': '掌上装饰材料网'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fc144aebbaece4e31908a15d19860e4e9.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fc144aebbaece4e31908a15d19860e4e9.png', 'market_id': '18', 'packageName': 'com.wise.zhshzhuangshgchwang', 'title': '掌上装饰工程网'}, 'packageName': 'com.wise.zhshzhuangshgchwang', 'title': '掌上装饰工程网'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fb96919e0c9b144ffbb3d514005ec60d7.png', 'market_id': '18', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttps%3A%2F%2Fappimg.dbankcdn.com%2Fapplication%2Ficon144%2Fb96919e0c9b144ffbb3d514005ec60d7.png', 'market_id': '18', 'packageName': 'com.zhongsou.zmall.zszsclscmall', 'title': '掌上装饰材料商城'}, 'packageName': 'com.zhongsou.zmall.zszsclscmall', 'title': '掌上装饰材料商城'}, {'baikeActive': 0, 'baikeUrl': '', 'IsAuth': 0, 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttp%3A%2F%2Fp2.qhimg.com%2Ft0112fc94203ebfc670.png', 'market_id': '1', 'appinfo': {'baikeActive': '0', 'baikeUrl': '', 'IsAuth': '0', 'icon': 'https://cdn-image.kuchuan.com/transferPicUrl?picUrl=http%3A%2F%2Fcdn-image.kuchuan.com%2FtransferPicUrl%3FpicUrl%3Dhttp%3A%2F%2Fp2.qhimg.com%2Ft0112fc94203ebfc670.png', 'market_id': '1', 'packageName': 'com.rd.huatest', 'title': '掌上装裱工-摩奈特装裱'}, 'packageName': 'com.rd.huatest', 'title': '掌上装裱工-摩奈特装裱'}], 'maxCount': 41787, 'isEnd': False}}
    infos = data['data']['result']
    package_name = ""
    for info in infos:
        if app_name == info["title"]:
            package_name = info["packageName"]
            break
    return package_name

#获取开发商名称
def getDeveloper():
    url = kuchaun_search_developer.format(package_name,package_name)
    head_data = {
        'Cookie': '_ga=GA1.2.1848213340.1652690100; _gid=GA1.2.1156197270.1652690100; Hm_lpvt_ef5592497ef84b441c6f40f98ada9c4f=1652698492; Hm_lvt_ef5592497ef84b441c6f40f98ada9c4f=1652690097; Hm_lpvt_84ee2face82d86b7584b5bbee44dfbe7=1652698492; Hm_lvt_84ee2face82d86b7584b5bbee44dfbe7=1652689992; CNZZDATA1257619731=708008061-1652680487-https%253A%252F%252Fios.kuchuan.com%252F%7C1652691308; CNZZDATA1260525360=2013768316-1652680496-https%253A%252F%252Fios.kuchuan.com%252F%7C1652691384; CNZZDATA5103679=cnzz_eid%3D77776780-1652681561-https%253A%252F%252Fios.kuchuan.com%252F%26ntime%3D1652692362; accessId=a1cb1fb0-0f1e-11e9-9e27-913eb5b7d900; pageViewNum=27; JSESSIONID=c4twua3jo60bo4mvib39u90w; token=5e651bc936be208f3d064df3cb70daff; href=https%3A%2F%2Fandroid.kuchuan.com%2Fpage%2Fdetail%2FsearchResult%3Fkw%3D%25E8%25B1%25AB%25E4%25B8%258A%25E8%25A3%2585%26site%3D0%26marketId%3D0; UM_distinctid=180cbfff87121d-0f40ca97baa516-3a62684b-13c680-180cbfff8724ed; uniqueId=daa491ba33f54d68b40d1390b9d57cef',
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

if __name__ == "__main__":
    s = os.listdir()
    for i in s:
        if ".apk" in i:
            app_name = i[:i.index("_")]
            app_version = i[i.index("_")+1:i.index("apk")-1]
    print(app_version)
    package_name = getPackageName()
    if package_name != "":
        totla_downloads = getTotalDownloads()
        #developer = getDeveloper()

    else:
        print("未查到该软件，请手动查询")