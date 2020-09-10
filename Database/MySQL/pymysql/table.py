import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="",db="test",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表
cursor.execute("DROP TABLE IF EXISTS USER")

# 创建数据表SQL语句
sql = """CREATE TABLE IF NOT EXISTS USER (
         id    int         unsigned not null auto_increment PRIMARY KEY,
         name  varchar(32) not null unique,
         email varchar(100),
         cdate datetime );"""

cursor.execute(sql)

# 关闭数据库连接
db.close()