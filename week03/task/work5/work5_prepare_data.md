> 本实验使用了sysbench来产生随机数据作为测试数据，存放至`sbtest`库中。使用sysbench生成一个1000万的表`sbtest1`，并导出数据到`sbtest2`中，确保数据一致，然后删除`sbtest2`表中`k`字段的索引。来对比`sbtest1`和`sbtest2`执行时长的分析。

### 安装sysbench添加测试数据

```shell
sudo apt -y install make automake libtool pkg-config libaio-dev
sudo apt -y install libmysqlclient-dev libssl-dev
sudo apt -y install sysbench
```

### 使用sysbench准备测试数据

```shell
# 指定4线程、生成两个测试表，每个表有100万条数据
sysbench --threads=4 --time=20 --report-interval=5 --mysql-host=localhost --mysql-port=3308 --mysql-user=root --mysql-password=123 --mysql-socket=/tmp/mysql.sock /usr/share/sysbench/oltp_read_write.lua --tables=1 --table_size=10000000 --db-driver=mysql prepare
```

### 查看数据准确性

```shell
# 表sbtest1、sbtest2数据均为1000万条
mysql> select count(*) from sbtest1;
+----------+
| count(*) |
+----------+
| 10000000 |
+----------+
1 row in set (1.24 sec)

mysql> select count(*) from sbtest2;
+----------+
| count(*) |
+----------+
| 10000000 |
+----------+
1 row in set (1.23 sec)


# 查看表结构
mysql> show create table sbtest1;
CREATE TABLE `sbtest1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `k` int(11) NOT NULL DEFAULT '0',
  `c` char(120) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  `pad` char(60) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  KEY `k_1` (`k`)
) ENGINE=InnoDB AUTO_INCREMENT=1000001 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
```

### 删除sbtest2表的`k`字段索引, 查看两表索引

```shell
# 删除sbtest2表`k`字段的索引
mysql> DROP INDEX k_1 ON sbtest2;

# 查看索引
# 查看sbtest1表索引
mysql> show index from sbtest1\G;
*************************** 1. row ***************************
        Table: sbtest1
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: id
    Collation: A
  Cardinality: 9496224
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
*************************** 2. row ***************************
        Table: sbtest1
   Non_unique: 1
     Key_name: k_1
 Seq_in_index: 1
  Column_name: k
    Collation: A
  Cardinality: 1429420
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
2 rows in set (0.01 sec)

# 查看sbtest2表索引
mysql> show index from sbtest2\G;
*************************** 1. row ***************************
        Table: sbtest2
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: id
    Collation: A
  Cardinality: 9365616
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
1 row in set (0.00 sec)
```

### mysql临时开启profiling查看SQL执行时间

```shell
# 使用show profiles,查看执行时间,需要开启profiling功能
# 测试环境临时开启profiling
mysql> set profiling=1;
# 通过查看系统变量即可查询到是否开启
mysql> show variables like "profiling";
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| profiling     | ON    |
+---------------+-------+
1 row in set (0.01 sec)
```

### 执行查询SQL对比两表执行时间以及影响行数

```shell
# 查看SQL执行时间；
mysql> show profiles;
+----------+------------+-----------------------------------------+
| Query_ID | Duration   | Query                                   |
+----------+------------+-----------------------------------------+
|        1 | 0.00294750 | select * from sbtest1 where k='4986694' |
|        2 | 2.94150500 | select * from sbtest2 where k='4986694' |
+----------+------------+-----------------------------------------+
2 rows in set (0.00 sec)
```

```shell
# 操作了多少行
mysql> explain select * from sbtest1 where k='4986694';
+----+-------------+---------+------------+------+---------------+------+---------+-------+------+----------+-------+
| id | select_type | table   | partitions | type | possible_keys | key  | key_len | ref   | rows | filtered | Extra |
+----+-------------+---------+------------+------+---------------+------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | sbtest1 | NULL       | ref  | k_1           | k_1  | 4       | const |   98 |   100.00 | NULL  |
+----+-------------+---------+------------+------+---------------+------+---------+-------+------+----------+-------+
1 row in set, 1 warning (0.01 sec)

mysql> explain select * from sbtest2 where k='4986694';
+----+-------------+---------+------------+------+---------------+------+---------+------+---------+----------+-------------+
| id | select_type | table   | partitions | type | possible_keys | key  | key_len | ref  | rows    | filtered | Extra       |
+----+-------------+---------+------------+------+---------------+------+---------+------+---------+----------+-------------+
|  1 | SIMPLE      | sbtest2 | NULL       | ALL  | NULL          | NULL | NULL    | NULL | 9365680 |    10.00 | Using where |
+----+-------------+---------+------------+------+---------------+------+---------+------+---------+----------+-------------+
1 row in set, 1 warning (0.00 sec)
```

### 执行更新SQL对比两表执行时间以及影响行数

```shell
mysql> show profiles;
+----------+------------+----------------------------------------------------------------+
| Query_ID | Duration   | Query                                                          |
+----------+------------+----------------------------------------------------------------+
|        1 | 0.06265750 | update sbtest1 set pad='update_test' where k='4986694'         |
|        2 | 5.32284550 | update sbtest2 set pad='update_test' where k='4986694'         |
+----------+------------+----------------------------------------------------------------+
2 row in set (0.00 sec)
```

通过数据即可看出，对于数据行比较多的库表，使用索引查询速度、更新数据有明显增强