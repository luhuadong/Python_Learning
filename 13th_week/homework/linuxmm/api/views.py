from django.shortcuts import render
from django.http import HttpResponse

import paramiko
import psutil


CMD = {
    'cpu_cnt_phy': 'cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l',
    'cpu_cnt_log': 'cat /proc/cpuinfo | grep "processor" | wc -l',
    'cpu_info'   : 'cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c | sed "s/^[ \t]*//g"',
    'mem_stat'   : 'free -m',
    'disk_stat'  : 'df -h'
}



# Create your views here.


def get_host_stat(request):

    ssh = paramiko.SSHClient()
    # 避免连接未知主机时出错
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    cmd_file = open("./static/run.py", "r")
    cmd = cmd_file.read()
    print(cmd)
    print('-' * 64)

    # 连接远程主机
    ssh.connect(hostname="120.78.197.79", username="root", password="")

    data = exec_remote_cmd(ssh, cmd)

    # 关闭连接
    ssh.close()

    return HttpResponse(data)


def exec_remote_cmd(ssh, cmd):
    """ 执行远程命令 """

    stdin, stdout, stderr = ssh.exec_command(cmd)
    res = stdout.read().decode()
    return res

