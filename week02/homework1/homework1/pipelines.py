# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'wsc',
    'password' : 'welcome1',
    'db' : 'db1'
}
result = []

class ConnDB(object):
    def __init__(self, dbInfo, sqls):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.sqls = sqls

        # self.run()

    def run(self):
        conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事物
        cur = conn.cursor()
        try:
            for command in self.sqls:
                print(command)
                cur.execute(command)
                result.append(cur.fetchall())
            # 关闭游标
            cur.close()
            conn.commit()
        except:
            conn.rollback()
        # 关闭数据库连接
        conn.close()

class Homework1Pipeline:
    def process_item(self, item, spider):
        title = item['title']
        type = item['type']
        date = item['date']
        # output = f'|{title}|\t|{type}|\t|{date}|\n'
        # with open('./movies.csv', 'a+', encoding='utf-8') as article:
        #     article.write(output)

        values = "'" + ''.join([_ for _ in title]) + "'" + ", " + "'" + ''.join(
            [_ for _ in type]) + "'" + ", " + "'" + ''.join([_ for _ in date]) + "'"

        with open('./movies.csv', 'a+', encoding='utf-8') as article:
            article.write(values + '\n')

        sql = "INSERT INTO maoyan_tbl (movie_title, movie_type, plan_date) VALUES (" + values + ");"
        print(sql)
        sqls = [sql]
        db = ConnDB(dbInfo, sqls)
        db.run()

        return item
