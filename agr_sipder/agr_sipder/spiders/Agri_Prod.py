# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urlparse, urlencode, parse_qs
from datetime import date, timedelta
from agr_sipder.items import AgrProdSipderItem

def tw_year(dt):
    return str(dt.year - 1911)+dt.strftime('.%m.%d')

class AgriProdSpider(scrapy.Spider):
    name = 'Agri_Prod'
    allowed_domains = ['data.coa.gov.tw']
    start_urls = ['https://data.coa.gov.tw/api/v1/AgriProductsTransType/?api_key=KVU0MO51X4AIMBP8RNTSG4465TE7FD']
#https://data.coa.gov.tw/api/v1/AgriProductsTransType/?Start_time=111.04.01&End_time=111.04.13



    def parse(self, response):
        parsed_url = urlparse(response.url)
        query_params = parse_qs(parsed_url.query)
        today = date.today()
        for i in range(7):
            # 使用 timedelta 函數減去天數
            day = today - timedelta(days=i)
            day_format = tw_year(day)
            query_params["Start_time"] = day_format
            query_params["End_time"] = day_format
            query_params["page"] = "1"
            new_url = parsed_url.scheme + "://" \
            + parsed_url.netloc + parsed_url.path \
            + "?" + urlencode(query_params, doseq=True)
            print(new_url)
            yield scrapy.Request(new_url, callback=self.GetOneDateProd)


    def GetOneDateProd(self, response):
        
        data = json.loads(response.text)
        today = date.today()
        day_format = tw_year(today)

        for item in data['Data']:
            yield {
                'TransDate': item['TransDate'],
                'CropCode': item['CropCode'],
                'CropName': item['CropName'],
                'MarketCode': item['MarketCode'],
                'MarketName': item['MarketName'],
                'Upper_Price': item['Upper_Price'],
                'Middle_Price': item['Middle_Price'],
                'Lower_Price': item['Lower_Price'],
                'Avg_Price': item['Avg_Price'],
                'Trans_Quantity': item['Trans_Quantity'],
                'As_Of_Date':day_format,
                'Pipline':'gov'
            }

        next_exist = data.get('Next')
        parsed_url = urlparse(response.url)
        query_params = parse_qs(parsed_url.query)
        if next_exist :
            next_page_num = int(query_params["page"][0])+1
            query_params["page"] = [str(next_page_num)] 
            next_page = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path + "?" + urlencode(query_params, doseq=True)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.GetOneDateProd)

