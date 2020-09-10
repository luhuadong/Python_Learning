import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="",db="test",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 定义删除 sql 语句
sql = "DELETE FROM USER WHERE id = %d"%(20190002)

try:
    cursor.execute(sql)
    print("成功删除条数：", cursor.rowcount)
    db.commit()
except Exception as err:
    db.rollback()
    print("SQL执行错误，原因：",err)

# 关闭数据库连接
db.close()