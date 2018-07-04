# 第二周作业

## 作业1. 创建并导出 blogdb 数据库
　　按要求创建 blogdb 数据库，并创建会员表 users 和博客文章表 blog，最后将其导出为 blogdb.sql 文件。

![image](https://gitee.com/luhuadong/Python_Learning/raw/master/2nd_week/homework/images/2nd_week_homework_1.png)


```
insert into blog(id,title,abstract,content,uid,cdate) values(201807001,'A',"AA","aa...aa",1001,curtime());
```

```
insert into blog(title,abstract,content,uid,cdate) values('B',"BB","bb...bb",1001,curtime());
```

导出数据库：
```
mysqldump -u root -p blogdb > blogdb.sql
```


## 作业2. 操作 blogdb 中的数据表

```
select * from users order by cdate limit 10;
```


## 作业3. 实现基于 MySQL 的学生信息管理系统


## 作业4. 飞机大战游戏


## 附加题. 连连看游戏
