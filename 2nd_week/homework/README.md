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
insert into users(id,name,email,cdate)
values(1001,'Allen','allen@csdn.net',curtime());
```
　　插入下一条记录时，则不必再指定 id 的值，让它自增就好了：
```
insert into users(name,email,cdate)
values('Bob','bob@csdn.net',curtime());
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
insert into blog(id,title,abstract,content,uid,cdate)
values(201807001,'A',"AA","aa...aa",1001,curtime());
```
　　因为 pcount 和 flag 有默认值，所以我没有指定它们的值，后续再修改。接着添加下一条记录，也不需要指定 id 的值：
```
insert into blog(title,abstract,content,uid,cdate)
values('B',"BB","bb...bb",1001,curtime());
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

**（5）最后将 blogdb 数据库中的信息导出，并以 blogdb.sql 文件存储待上交作业。**

　　最后，我们在终端下执行如下命令导出数据库文件：

```
mysqldump -u root -p blogdb > blogdb.sql
```


------

## 作业2. 操作 blogdb 中的数据表

**（1）在 users 表中查询注册时间最早的十条会员信息。**

　　命令：
```
select * from users ORDER BY cdate LIMIT 10;
```

　　结果：

```
+------+--------+-----------------+---------------------+
| id   | name   | email           | cdate               |
+------+--------+-----------------+---------------------+
| 1002 | Bob    | bob@csdn.net    | 2018-07-03 00:00:00 |
| 1003 | Carrie | carrie@csdn.net | 2018-07-03 17:53:54 |
| 1004 | David  | david@csdn.net  | 2018-07-03 23:41:56 |
| 1005 | Elsa   | elsa@csdn.net   | 2018-07-04 00:03:16 |
| 1006 | Fifi   | fifi@csdn.net   | 2018-07-04 00:03:35 |
| 1007 | Gucci  | gucci@csdn.net  | 2018-07-04 00:05:01 |
| 1001 | Allen  | allen@csdn.net  | 2018-07-04 00:07:13 |
| 1008 | Herry  | herry@csdn.net  | 2018-07-04 01:00:23 |
| 1009 | Irving | irving@csdn.net | 2018-07-04 01:00:59 |
| 1010 | James  | james@csdn.net  | 2018-07-04 01:01:30 |
+------+--------+-----------------+---------------------+
10 rows in set (0.00 sec)

```

**（2）从两个表中查询点赞数最高的5条博客信息，要求显示字段：(博文id, 标题, 点赞数, 会员名)**

　　命令：
```
SELECT blog.id as article_id, title, pcount, users.name as author
FROM blog, users
WHERE blog.uid=users.id
ORDER BY pcount DESC LIMIT 5;
```
　　结果：
```
+------------+-------+--------+--------+
| article_id | title | pcount | author |
+------------+-------+--------+--------+
|  201807004 | D     |     12 | David  |
|  201807006 | F     |     10 | Elsa   |
|  201807001 | A     |     10 | Allen  |
|  201807002 | B     |      8 | Allen  |
|  201807012 | L     |      8 | Nike   |
+------------+-------+--------+--------+
5 rows in set (0.00 sec)

```

**（3）统计每个会员的发表博文数量（降序），要求显示字段：(会员id号, 姓名, 博文数量)**

　　命令：
```
SELECT users.id, users.name, COUNT(blog.uid) as count
FROM blog, users
WHERE blog.uid=users.id AND blog.flag=1
GROUP BY users.id
ORDER BY count DESC, uid;
```
　　结果：
```
+------+--------+-------+
| id   | name   | count |
+------+--------+-------+
| 1005 | Elsa   |     3 |
| 1001 | Allen  |     2 |
| 1002 | Bob    |     2 |
| 1003 | Carrie |     1 |
| 1004 | David  |     1 |
| 1007 | Gucci  |     1 |
| 1008 | Herry  |     1 |
| 1009 | Irving |     1 |
| 1014 | Nike   |     1 |
+------+--------+-------+
9 rows in set (0.00 sec)

```


**（4）获取会员的博文平均点赞数量最高的三位。显示字段：(会员id, 姓名, 平均点赞数)**

　　命令：
```
SELECT users.id, users.name, AVG(blog.pcount) as avg_like
FROM blog, users
WHERE blog.uid=users.id
GROUP BY users.id
ORDER BY avg_like DESC, uid
LIMIT 3;
```
　　结果：
```
+------+-------+----------+
| id   | name  | avg_like |
+------+-------+----------+
| 1004 | David |  12.0000 |
| 1014 | Nike  |   8.0000 |
| 1005 | Elsa  |   7.6667 |
+------+-------+----------+
3 rows in set (0.00 sec)

```

**（5）删除没有发表博文的所有会员信息。**

　　在删除之前，我们先来看看 users 表中哪些会员在 blog 表中没有记录，也就是说没有编辑过博文（这里不管是否已发布或者删除）。

　　命令：
```
SELECT users.id, users.name
FROM users
WHERE users.id NOT IN (SELECT uid FROM blog);
```
　　结果：
```
+------+--------+
| id   | name   |
+------+--------+
| 1006 | Fifi   |
| 1010 | James  |
| 1011 | Ken    |
| 1013 | Miruna |
+------+--------+
4 rows in set (0.00 sec)
```

　　对比前面完整的 blog 表数据，确实是这几个哥们没有编辑过博文。那么，我们就按题目要求把他们删除吧（虽然不太人道）。

　　命令：
```
delete FROM users
WHERE users.id NOT IN (SELECT uid FROM blog);
```
　　结果：
```
Query OK, 4 rows affected (0.01 sec)
```

　　检查一下：

```
mysql> SELECT id, name FROM users;
+------+--------+
| id   | name   |
+------+--------+
| 1001 | Allen  |
| 1002 | Bob    |
| 1003 | Carrie |
| 1004 | David  |
| 1005 | Elsa   |
| 1007 | Gucci  |
| 1008 | Herry  |
| 1009 | Irving |
| 1012 | Lucky  |
| 1014 | Nike   |
+------+--------+
10 rows in set (0.00 sec)

```

　　Fifi、James、Ken、Miruna 四个会员的信息确实被我们删除了。

　　如果想找回来，可以用作业1导出的 blogdb.sql 文件，重新导入到一个空的数据库。方法如下：

　　首先创建一个新的数据库 `create database newdb`，然后选择数据库 `use newdb`，设置数据库编码 `set names utf8`，最后导入数据 `source /home/root/blogdb.sql` 即可。

　　如果嫌麻烦，也可以简单粗暴地使用以下命令：
```
mysql -u root -p newdb < blogdb.sql
```


------


## 作业3. 实现基于 MySQL 的学生信息管理系统

------

## 作业4. 飞机大战游戏

------


## 附加题. 连连看游戏
