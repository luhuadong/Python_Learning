import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="",db="test",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 定义更新 sql 语句
sql = "UPDATE USER SET email = 'allen@163.com' WHERE id = %d"%(20190001)

try:
    cursor.execute(sql)
    print("本次更新条数：", cursor.rowcount)
    db.commit()
except Exception as err:
    db.rollback()
    print("SQL执行错误，原因：",err)

# 关闭数据库连接
db.close()