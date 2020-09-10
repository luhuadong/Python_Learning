import pymysql
import datetime

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="",db="test",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 定义添加 sql 语句
data = (20190001, "Allen", 'allen@gmail.com', \
        '{0}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
sql = "INSERT INTO USER(id, name, email, cdate) value('%d','%s','%s','%s')"%(data)

try:
    # 使用 execute() 方法执行 SQL 
    m = cursor.execute(sql)
    # 事务提交
    db.commit()
    print("成功操作条数：",m)
    #print("成功操作条数：",cursor.rowcount)
except Exception as err:
    # 事务回滚
    db.rollback()
    print("SQL执行错误，原因：",err)

# 关闭数据库连接
db.close()