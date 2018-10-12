# 部署 Django 项目





### 安装 uWSGI

```
$ sudo pip3 install uwsgi
```



前台运行

```
uwsgi --http :9090 --chdir /root/demo --module demo.wsgi
```

后台运行

```
uwsgi --http :9090 --chdir /root/demo --module demo.wsgi --daemonize /var/log/uwsgi.log
```

