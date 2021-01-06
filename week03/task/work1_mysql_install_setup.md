### 环境介绍

| 操作系统  | Ubuntu20.04 desktop                 |
| :-------: | ----------------------------------- |
| 内核版本  | 5.4.0-58-generic                    |
| MySQL版本 | mysql-5.7.31-linux-glibc2.12-x86_64 |

### 下载安装初始化MySQL

```shell
wget -c https://cdn.mysql.com/archives/mysql-5.7/mysql-5.7.31-linux-glibc2.12-x86_64.tar.gz
# 解压二进制安装包
sudo tar -xf mysql-5.7.31-linux-glibc2.12-x86_64.tar.gz -C  /usr/local/
sudo ln -sv /usr/local/mysql-5.7.31-linux-glibc2.12-x86_64/ /usr/local/mysql
# 配置环境变量
sudo echo "export PATH=$PATH:/usr/local/mysql/bin" >> /etc/profile
source /etc/profile
# 开机启动
sudo cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysql
sed -i -e '/basedir=$/s/basedir=/basedir=\/usr\/local\/mysql\//' -e '/datadir=$/s/datadir=/datadir=\/data\/mysql\/data\//' /tmp/mysql-test.txt
sudo update-rc.d mysql defaults
sudo update-rc.d mysql enable
# 新建mysql用户以及数据目录
sudo useradd -s /sbin/nologin -M mysql
sudo mkdir -pv /data/mysql/data
sudo chown -R mysql. /data/mysql/data
```

### 初始化MySQL数据库

```shell
# --defaults-file指定配置文件，--user指定mysql启动用户，--datadir指定数据存放目录，--basedir指定mysql软件目录， --initialize初始化选项
sudo /usr/local/mysql/bin/mysqld --defaults-file=/etc/mysql/my.cnf --initialize --user=mysql --datadir=/data/mysql/data/ --basedir=/usr/local/mysql
```

### 编辑MySQL配置文件,设置字符集

```shell
cat /etc/mysql/my.cnf
[mysql]
# 设置mysql客户端连接使用的字符集
default_character_set = utf8mb4

[cilent]
# 设置其他客户端连接使用的字符集
default_character_set = utf8mb4

[mysqld]
# 配置mysql监听端口
port=3308

# 设置mysql
# 设置mysql数据库默认字符集
character-set-server=utf8mb4
# 初始化连接字符集设置
init_connect = "SET NAMES utf8mb4"
character_set_client_handshake = False
collation_server = utf8mb4_unicode_ci
```

### 启动MySQL数据库

```shell
sudo systemctl restart mysql
sudo systemctl enable mysql
```

### 登录MySQL，修改管理员密码

```shell
# 使用初始化之后的密码登录数据库
mysql -uroot -p
# 修改mysql管理员密码，由于是开发环境，设置一个弱密码，生产环境需要增加密码强度
mysql> alter root@'localhost' identified by '1234';
```

### 查看数据库当前字符集

```shell
mysql> show variables like '%character%';
+--------------------------+----------------------------------------------------------------+
| Variable_name            | Value                                                          |
+--------------------------+----------------------------------------------------------------+
| character_set_client     | utf8mb4                                                        |
| character_set_connection | utf8mb4                                                        |
| character_set_database   | utf8mb4                                                        |
| character_set_filesystem | binary                                                         |
| character_set_results    | utf8mb4                                                        |
| character_set_server     | utf8mb4                                                        |
| character_set_system     | utf8                                                           |
| character_sets_dir       | /usr/local/mysql-5.7.31-linux-glibc2.12-x86_64/share/charsets/ |
+--------------------------+----------------------------------------------------------------+
8 rows in set (0.00 sec)
```

### 查看当前校对规则

```shell
mysql> show variables like '%collation%';
+----------------------+--------------------+
| Variable_name        | Value              |
+----------------------+--------------------+
| collation_connection | utf8mb4_unicode_ci |
| collation_database   | utf8mb4_unicode_ci |
| collation_server     | utf8mb4_unicode_ci |
+----------------------+--------------------+
3 rows in set (0.00 sec)
```

### 创建数据库并授权新用户远程访问

```shell
# 创建数据库
mysql> create database testdb;
# 授权新用户
mysql> grant all on testdb.* to 'python'@'%' identified by 'python123';
```

