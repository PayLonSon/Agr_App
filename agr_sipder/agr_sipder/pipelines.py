# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from agr_sipder import items
from agr_sipder import settings
import pymysql

#class AgrSipderPipeline(object):
#    def process_item(self, item, spider):
#        return item


class AgrSipderPipeline(object):
    def __init__(self):

        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DATABASE,
            user=settings.MYSQL_USERNAME,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8'
        )
        
        
        self.cursor = self.connect.cursor()



    def gov_item(self,item):

    # 检查是否存在重复记录
        query = 'SELECT * FROM Agri_Prod WHERE CropCode = %s  \
        AND MarketCode = %s and TransDate = %s ; '
        
        self.cursor.execute(query, (item['CropCode'], item['MarketCode'], item['TransDate']))
        result = self.cursor.fetchone()

    # 如果没有重复记录，插入数据
        if result:
            print('存在了咧')
        else :
            print('不在咧')
            query = 'INSERT INTO Agri_Prod (    TransDate ,CropCode ,CropName ,MarketCode ,\
                                            MarketName ,Upper_Price ,Middle_Price ,Lower_Price ,\
                                            Avg_Price ,Trans_Quantity ,As_Of_Date) \
        VALUES ("{TransDate}" ,"{CropCode}" ,"{CropName}" ,"{MarketCode}" ,\
                "{MarketName}" ,"{Upper_Price}" ,"{Middle_Price}"  ,"{Lower_Price}" ,\
                "{Avg_Price}" ,"{Trans_Quantity}" ,"{As_Of_Date}" ); '.format(
                TransDate = item['TransDate'],CropCode = item['CropCode'], 
                CropName = item['CropName'], MarketCode = item['MarketCode'],
                MarketName = item['MarketName'], Upper_Price = item['Upper_Price'], 
                Middle_Price = item['Middle_Price'], Lower_Price = item['Lower_Price'],
                Avg_Price = item['Avg_Price'], Trans_Quantity = item['Trans_Quantity'], 
                As_Of_Date = item['As_Of_Date']
                )
            self.cursor.execute(query)

    def px_item(self,item):
    # 检查是否存在重复记录
        query = 'SELECT * FROM px_data WHERE CropName = %s  \
        AND Avg_Price = %s and As_Of_Date = %s ; '
        
        self.cursor.execute(query, (item['CropName'], item['Avg_Price'], item['As_Of_Date']))
        result = self.cursor.fetchone()

    # 如果没有重复记录，插入数据
        if result:
            print('存在了咧')
        else :
            print('不在咧')
            query = 'INSERT INTO px_data (    CropName, Avg_Price, Suggest_Price, As_Of_Date) \
        VALUES ("{CropName}" ,"{Avg_Price}" ,"{Suggest_Price}" ,"{As_Of_Date}" ); '.format(
                CropName = item['CropName'], Avg_Price = item['Avg_Price'], 
                Suggest_Price = item['Suggest_Price'], As_Of_Date = item['As_Of_Date']
                )
            self.cursor.execute(query)

    def process_item(self, item, spider):

        print(item['Pipline'])
        if item['Pipline'] == 'gov':
            self.gov_item(item)
        if item['Pipline'] == 'px':
            self.px_item(item)
        else:
            print('[INFO] NONE')


    def close_spider(self, spider):
        self.connect.commit()
        self.connect.close()