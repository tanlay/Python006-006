以下两张基于 id,name的列，分别使用 INNER JOIN、LEFT JOIN、 RIGHT JOIN 的结果是什么?

```shell
table1
+----+---------------+
| id | name          |
+----+---------------+
|  1 | table1_table2 |
|  2 | table1        |
+----+---------------+

table2
+----+---------------+
| id | name          |
+----+---------------+
|  1 | table1_table2 |
|  3 | table2        |
+----+---------------+
```

### inner join SQL及执行结果如下

```shell
mysql> SELECT
    -> t1.id as t1_id,
    -> t1.NAME as t1_name,
    -> t2.id as t2_id,
    -> t2.NAME as t2_name
    -> FROM
    -> table1 as t1
    -> INNER JOIN table2 as t2 ON t1.id = t2.id;
+-------+---------------+-------+---------------+
| t1_id | t1_name       | t2_id | t2_name       |
+-------+---------------+-------+---------------+
|     1 | table1_table2 |     1 | table1_table2 |
+-------+---------------+-------+---------------+
```

### left join SQL及执行结果如下：

```shell
mysql> SELECT
    -> t1.id as t1_id,
    -> t1.NAME as t1_name,
    -> t2.id as t2_id,
    -> t2.NAME as t2_name
    -> FROM
    -> table1 as t1
    -> LEFT JOIN table2 as t2 ON t1.id = t2.id;
+-------+---------------+-------+---------------+
| t1_id | t1_name       | t2_id | t2_name       |
+-------+---------------+-------+---------------+
|     1 | table1_table2 |     1 | table1_table2 |
|     2 | table1        |  NULL | NULL          |
+-------+---------------+-------+---------------+
```

### right join SQL及执行结果如下：

```shell
mysql> SELECT
    -> t1.id as t1_id,
    -> t1.NAME as t1_name,
    -> t2.id as t2_id,
    -> t2.NAME as t2_name
    -> FROM
    -> table1 as t1
    -> RIGHT JOIN table2 as t2 ON t1.id = t2.id;
+-------+---------------+-------+---------------+
| t1_id | t1_name       | t2_id | t2_name       |
+-------+---------------+-------+---------------+
|     1 | table1_table2 |     1 | table1_table2 |
|  NULL | NULL          |     3 | table2        |
+-------+---------------+-------+---------------+
```

### full join如下及其执行结果如下：

> mysql 不能直接查询全连接，需要使用union连接左右连接

```shell
mysql> SELECT
    -> t1.id AS t1_id,
    -> t1.NAME AS t1_name,
    -> t2.id AS t2_id,
    -> t2.NAME AS t2_name 
    -> FROM
    -> table1 AS t1
    -> LEFT JOIN table2 AS t2 ON t1.id = t2.id UNION
    -> SELECT
    -> t1.id AS t1_id,
    -> t1.NAME AS t1_name,
    -> t2.id AS t2_id,
    -> t2.NAME AS t2_name 
    -> FROM
    -> table1 AS t1
    -> RIGHT JOIN table2 AS t2 ON t1.id = t2.id;
+-------+---------------+-------+---------------+
| t1_id | t1_name       | t2_id | t2_name       |
+-------+---------------+-------+---------------+
|     1 | table1_table2 |     1 | table1_table2 |
|     2 | table1        |  NULL | NULL          |
|  NULL | NULL          |     3 | table2        |
+-------+---------------+-------+---------------+
```

