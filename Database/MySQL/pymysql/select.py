import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost",user="root",password="",db="test",charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 定义查询 sql 语句
sql = "SELECT * FROM USER"

try:
    # 使用 execute() 方法执行 SQL 查询 
    cursor.execute(sql)
    print("本次查询条数：", cursor.rowcount)
    # 获取所有结果
    res = cursor.fetchall()
    for item in res:
        print(item)
except Exception as err:
    print("SQL执行错误，原因：",err)

# 关闭数据库连接
db.close()