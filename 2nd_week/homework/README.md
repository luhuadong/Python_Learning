# 第二周作业

------


## 作业1. 创建并导出 blogdb 数据库

　　在命令行模式下登录 MySQL 数据库，使用 SQL 语句完成如下要求：

　　**（1）创建留言数据库 blogdb**

```
create database if not exists blogdb;

use blogdb;
```

　　**（2）在 blogdb 数据库中创建会员表 users 和博客文章表 blog，结构如下：**

![image](https://gitee.com/luhuadong/Python_Learning/raw/master/2nd_week/homework/images/2nd_week_homework_1.png)

　　创建 users 表：

```
create table users(
    id    int         unsigned not null auto_increment PRIMARY KEY,
    name  varchar(32) not null unique,
    email varchar(100),
    cdate datetime
);
```
　　创建 blog 表：
```
create table blog(
    id       int          unsigned not null auto_increment PRIMARY KEY,
    title    varchar(100) not null,
    abstract varchar(200) not null,
    content  text         not null,
    uid      int          unsigned,
    pcount   int          unsigned default 0,
    flag     tinyint      unsigned default 0,
    cdate    datetime
);
```

　　也许 blog.flag 字段还可以这样定义：

```
    flag     enum(0,1,2)  not null default 0,
```

　　创建好之后，我们来查看 users 表结构：

```
mysql> desc users;
+-------+------------------+------+-----+---------+----------------+
| Field | Type             | Null | Key | Default | Extra          |
+-------+------------------+------+-----+---------+----------------+
| id    | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(32)      | NO   | UNI | NULL    |                |
| email | varchar(100)     | YES  |     | NULL    |                |
| cdate | datetime         | YES  |     | NULL    |                |
+-------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

```

　　还有查看 blog 表结构：

```
mysql> desc blog;
+----------+---------------------+------+-----+---------+----------------+
| Field    | Type                | Null | Key | Default | Extra          |
+----------+---------------------+------+-----+---------+----------------+
| id       | int(10) unsigned    | NO   | PRI | NULL    | auto_increment |
| title    | varchar(100)        | NO   |     | NULL    |                |
| abstract | varchar(200)        | NO   |     | NULL    |                |
| content  | text                | NO   |     | NULL    |                |
| uid      | int(10) unsigned    | YES  |     | NULL    |                |
| pcount   | int(10) unsigned    | YES  |     | 0       |                |
| flag     | tinyint(3) unsigned | YES  |     | 0       |                |
| cdate    | datetime            | YES  |     | NULL    |                |
+----------+---------------------+------+-----+---------+----------------+
8 rows in set (0.00 sec)

```

　　**（3）在会员表 users 中添加 >=5 条的测试数据。**

　　这里 id 的数据类型是 int，而且是 unsigned 和 auto_increment 的，如果我们不指定 id，它就会从 1 开始算起。
　　我这里并不想让 id 从 1 开始自增，所以我在插入的第一条语句中指定 id 的值：

```
insert into users(id,name,email,cdate) values(1001,'Allen','allen@csdn.net',curtime());
```
　　插入下一条记录时，则不必再指定 id 的值，让它自增就好了：
```
insert into users(name,email,cdate) values('Bob','bob@csdn.net',curtime());
```

　　最后，users 表的数据如下：

```
mysql> select * from users;
+------+--------+-----------------+---------------------+
| id   | name   | email           | cdate               |
+------+--------+-----------------+---------------------+
| 1001 | Allen  | allen@csdn.net  | 2018-07-04 00:07:13 |
| 1002 | Bob    | bob@csdn.net    | 2018-07-03 00:00:00 |
| 1003 | Carrie | carrie@csdn.net | 2018-07-03 17:53:54 |
| 1004 | David  | david@csdn.net  | 2018-07-03 23:41:56 |
| 1005 | Elsa   | elsa@csdn.net   | 2018-07-04 00:03:16 |
| 1006 | Fifi   | fifi@csdn.net   | 2018-07-04 00:03:35 |
| 1007 | Gucci  | gucci@csdn.net  | 2018-07-04 00:05:01 |
| 1008 | Herry  | herry@csdn.net  | 2018-07-04 01:00:23 |
| 1009 | Irving | irving@csdn.net | 2018-07-04 01:00:59 |
| 1010 | James  | james@csdn.net  | 2018-07-04 01:01:30 |
| 1011 | Ken    | ken@csdn.net    | 2018-07-04 01:01:46 |
| 1012 | Lucky  | lucky@csdn.net  | 2018-07-04 01:02:16 |
| 1013 | Miruna | miruna@csdn.net | 2018-07-04 01:02:36 |
| 1014 | Nike   | nike@csdn.net   | 2018-07-04 01:03:22 |
+------+--------+-----------------+---------------------+
14 rows in set (0.00 sec)

```

　　**（4）在 blog 博文信息表中添加 >=10 条的测试数据。**

　　同样，在 blog 表添加第一条记录时指定 id 的值：

```
insert into blog(id,title,abstract,content,uid,cdate) values(201807001,'A',"AA","aa...aa",1001,curtime());
```
　　因为 pcount 和 flag 有默认值，所以我没有指定它们的值，后续再修改。接着添加下一条记录，也不需要指定 id 的值：
```
insert into blog(title,abstract,content,uid,cdate) values('B',"BB","bb...bb",1001,curtime());
```

　　此时 pcount 和 flag 的值都是 0，所以我使用 `update blog set pcount=10 where title='A';` 之类的操作进行调整。最后 blog 表的数据如下：

```
mysql> select * from blog;
+-----------+-------+----------+---------+------+--------+------+---------------------+
| id        | title | abstract | content | uid  | pcount | flag | cdate               |
+-----------+-------+----------+---------+------+--------+------+---------------------+
| 201807001 | A     | AA       | aa...aa | 1001 |     10 |    1 | 2018-07-04 11:56:17 |
| 201807002 | B     | BB       | bb...bb | 1001 |      8 |    1 | 2018-07-04 11:57:28 |
| 201807003 | C     | CC       | cc...cc | 1002 |      5 |    1 | 2018-07-04 11:58:01 |
| 201807004 | D     | DD       | dd...dd | 1004 |     12 |    1 | 2018-07-04 11:58:21 |
| 201807005 | E     | EE       | ee...ee | 1005 |      7 |    1 | 2018-07-04 11:58:39 |
| 201807006 | F     | FF       | ff...ff | 1005 |     10 |    1 | 2018-07-04 11:58:51 |
| 201807007 | G     | GG       | gg...gg | 1008 |      2 |    1 | 2018-07-04 11:59:16 |
| 201807008 | H     | HH       | hh...hh | 1008 |      0 |    0 | 2018-07-04 11:59:35 |
| 201807009 | I     | II       | ii...ii | 1007 |      3 |    1 | 2018-07-04 12:00:06 |
| 201807010 | J     | JJ       | jj...jj | 1005 |      6 |    1 | 2018-07-04 12:00:23 |
| 201807011 | K     | KK       | kk...kk | 1009 |      1 |    1 | 2018-07-04 12:00:46 |
| 201807012 | L     | LL       | ll...ll | 1014 |      8 |    1 | 2018-07-04 12:00:59 |
| 201807013 | M     | MM       | mm...mm | 1012 |      0 |    0 | 2018-07-04 12:01:17 |
| 201807014 | N     | NN       | nn...nn | 1002 |      4 |    1 | 2018-07-04 12:01:37 |
| 201807015 | O     | OO       | oo...oo | 1003 |      1 |    1 | 2018-07-04 12:02:00 |
| 201807016 | P     | PP       | pp...pp | 1008 |      0 |    0 | 2018-07-04 12:02:19 |
| 201807017 | Q     | QQ       | qq...qq | 1001 |      0 |    2 | 2018-07-04 12:02:44 |
+-----------+-------+----------+---------+------+--------+------+---------------------+
17 rows in set (0.00 sec)

```

　　**（5）最后将blogdb数据库中的信息导出，并以blogdb.sql文件存储待上交作业。**

　　最后，我们在终端下执行如下命令导出数据库文件：

```
mysqldump -u root -p blogdb > blogdb.sql
```

------

## 作业2. 操作 blogdb 中的数据表

```
select * from users order by cdate limit 10;
```

------


## 作业3. 实现基于 MySQL 的学生信息管理系统

------

## 作业4. 飞机大战游戏

------


## 附加题. 连连看游戏
