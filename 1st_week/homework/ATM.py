'''
 Name: 模拟自动取款机
 Athor: 卢华东
 Date: 2018-06-18
 Description: 数据临时存放在变量列表中，实现一个取款机上的存取款
              模拟效果，包括登录、退出、查询余额、取款和存款功能
'''

# 账号信息列表
accoutList = [
        {'accout':'442018001','name':'Allen','passwd':'123456','balance':100.00},
        {'accout':'442018002','name':'Bonus','passwd':'abcdef','balance':100.00},
        {'accout':'442018003','name':'Carrie','passwd':'hello','balance':200.00}]

# 显示账户信息列表
def showAccout(accoutList):
    '''
    '''
    if len(accoutList) == 0:
        print("(I) No Data from Accout")
        return
    print("|{0:<10} | {1:<10} | {2:<10} | {3:<10}".format("accout",
        "name","passwd","balance"))
    print("-"*40)
    for i in range(len(stulist)):
        print("|{0:<5} | {1:<10} | {2:<5} | {3:<10}".format(i+1,
            stulist[i]['name'],stulist[i]['age'],stulist[i]['classid']))
    print("")

# 登录界面
def showLoginPage():
    print("+-----------------------+")
    print("+                       +")
    print("+          ATM          +")
    print("+                       +")
    print("+-----------------------+")
    print("        （请插卡）       ")
    
# 验证账号及密码
def checkAccout(accout, passwd):
    for item in accoutList:
        if accout == item['accout'] and passwd == item['passwd']:
            return True
        else:
            return False



# 初始化界面
def showMainPage():

    print("="*12, "学员信息在线管理", "="*12)
    print("{0:1} {1:13} {2:15}".format(" ", "1.查看学员信息", 
        "2.添加学员信息"))
    print("{0:1} {1:13} {2:15}".format(" ", "3.删除学员信息", 
        "4.退出系统"))
    print("="*42)


# 开始啦
showLoginPage()
accout = input("请输入账号：")
passwd = input("请输入密码：")
if checkAccout(accout, passwd):
    print("(I) 登录成功")
else:
    print("(I) 登录失败，请检查账号和密码")

while True:
    showMainPage()
    key = input("请输入对应的选择：")
    if key == "1":
        print("="*14, "学员信息浏览", "="*14)
        showStu(stulist)
        input("按回车键继续：")
    elif key == "2":
        print("="*14, "学员信息添加", "="*14)
        stu = {}
        stu['name'] = input("请输入要添加的姓名：")
        stu['age'] = input("请输入要添加的年龄：")
        stu['classid'] = input("请输入要添加的班级号：")
        stulist.append(stu)
        print("(I) 添加成功")
        input("按回车键继续：")
    elif key == "3":
        print("="*14, "学员信息删除", "="*14)
        sid = input("请输入你要删除的信息id号：")
        if int(sid) > 0 and int(sid) <= len(stulist):
            del stulist[int(sid)-1]
            print("(I) 删除成功")
        else:
            print("(E) 删除失败")
        input("按回车键继续：")
    elif key == "4":
        print("="*18, "再见", "="*18)
        break
    else:
        print("Try again!")

