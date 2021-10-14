# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from guaiben_redis.items import GuaibenItem, GuaibenItem2
from itemadapter import ItemAdapter
import pymysql
import scrapy
from scrapy import item
from .items import GuaibenItem, GuaibenItem2





# class data_search_id():
#     def __init__(self):

class MysqlPipeline1(object):
    """
    同步操作
    """

    def __init__(self):
        self.conn = pymysql.connect(
            host='47.113.205.237', port=3306, user='root', password='820197450zhao', db='xiaoshuo', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, GuaibenItem):
            sql = 'INSERT INTO books (name,title,type) VALUE (%s, %s, %s )'
            value = (item['name_data'], item['title_data'], item['type_data'])  # 字段的值
            self.cursor.execute(sql, value)
            self.conn.commit()
        else:
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class MysqlPipeline2(object):
    """
    同步操作
    """

    def __init__(self):
        self.conn = pymysql.connect(
            host='47.113.205.237', port=3306, user='root', password='820197450zhao', db='xiaoshuo', charset='utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, GuaibenItem2):
            insert_sql = 'INSERT INTO chapters (book_id,rules,content,rules_info) VALUE (%s, %s, %s, %s)'
            value = (item['book_id'], item['rules'], item['content'], item['zhang_name'])
            self.cursor.execute(insert_sql, value)
            self.conn.commit()
        else:
            return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class MysqlPipeline3(object):
    """
    同步操作
    """

    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect(
            host='47.113.205.237', port=3306, user='root', password='820197450zhao', db='xiaoshuo', charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        if isinstance(item, GuaibenItem):
            # print('这是item1的管道')
            sql = 'INSERT INTO books (name,title,type) VALUE (%s, %s, %s )'
            value = (item['name_data'], item['title_data'], item['type_data'])  # 字段的值

            self.cursor.execute(sql, value)
            self.conn.commit()
        else:
            insert_sql = 'INSERT INTO chapters (book_id,rules,content,rules_info) VALUE (%s, %s, %s, %s)'
            value = (item['book_id'], item['rules'], item['content'], item['zhang_name'])

            self.cursor.execute(insert_sql, value)
            self.conn.commit()

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
        return item
