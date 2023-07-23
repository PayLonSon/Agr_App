# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from datetime import date, timedelta
from agr_sipder.items import PxApiSipderItem
from agr_sipder.px_data import query


def tw_year(dt):
    return str(dt.year - 1911)+dt.strftime('.%m.%d')

class PxAgriSpider(scrapy.Spider):
    name = 'px_agri'
    # 設置請求體
    allowed_domains = ['data.coa.gov.tw']
    start_urls = ['https://data.coa.gov.tw/api/v1/AgriProductsTransType/?Start_time=107.07.01&End_time=107.07.10']


    def parse(self, response):
        yield scrapy.Request(response.url, callback=self.GetOneDateProd)


    def GetOneDateProd(self, response):
        # 向 API 發送 GET 請求
        print('[INFO] 2')

        # 設置請求頭
        headers = {'Content-Type': 'application/json'}
        response = requests.get(query, headers=headers)
        today = date.today()
        day_format = tw_year(today)
        # 處理響應
        if response.status_code == 200:
            data = response.json()
            # 處理返回的數據

            for item in data['data']['shopCategory']['salePageList']['salePageList']:
                yield {
                    'CropName': item['title'],
                    'Avg_Price': item['price'],
                    'Suggest_Price': item['suggestPrice'],
                    'As_Of_Date':day_format,
                    'Pipline':'px'
                }

        else:
            print('請求失敗')

        # 向 API 發送 POST 請求
#        response = requests.post('https://apigw.px.91app.tw/pythia-cdn/graphql', json=data, headers=headers)

        # 處理響應
#        if response.status_code == 200:
#            data = response.json()
            # 處理返回的數據
#        else:
#           print('請求失敗')
 #       yield scrapy.Request(new_url, callback=self.GetOneDateProd)