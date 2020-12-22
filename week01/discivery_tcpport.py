import os
import json
import time
from pathlib import Path

"""
由于普通用户对/var/log/目录没有写入权限，
可以使用管理员账户让普通用户对其有写入权限,
执行以下命令chmod o+w /var/log
"""


def getNowTime():
    nowtime = time.strftime("%F %T", time.localtime())
    return nowtime


def getTcpPort():
    """
    tcp端口自动发现
    可以通过管理员给netstat添加s权限,
    chmod +s /bin/netstat
    """
    cmd = os.popen(
        '''netstat -tnlp|egrep "java|nginx|redis|named|harpoxy|node|ftp"|
        awk '{print $4}'|awk -F':+|::1:' '{print $2}'|sort -nu''')
    ports = []
    for port in cmd.read().split('\n'):
        if len(port) != 0:
            ports.append({'{#PORT_NAME}': port})
    # print(json.dumps({'data': ports}, indent=4, separators=(',', ':')))
    res = json.dumps({'data': ports}, indent=4, separators=(',', ':'))
    return res


def writeFile(path):
    p = Path(path)
    if not p.parents[0].exists():
        p.parents[0].mkdir()
    with open(path, "a") as f:
        f.write(str(getNowTime()))
        f.write("\n")
        f.write(str(getTcpPort()))
        f.write("\n")


logfile = "/var/log/python-{}/test.log".format(time.strftime('%Y%m%d'))
writeFile(logfile)
