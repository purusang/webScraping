# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling differet item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class QuotetutorialPipeline:
    def __init__(self):
        self.make_connection()
        self.create_table()

    def make_connection(self):
        self.conn = mysql.connector.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'quotes')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS quotes_tb")
        self.curr.execute("""CREATE TABLE quotes_tb(
            title text,
            author text,
            tag text
        )""")


    def save_data(self, item):
        self.curr.execute("""insert into quotes_tb values (%s, %s, %s)""", (item['title'][0],
                                                                         item['author'][0],
                                                                         ','.join(item['tag'])))
        self.conn.commit()

    def process_item(self, item, spider):
        self.save_data(item)
        return item
