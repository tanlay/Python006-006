索引有主键索引、唯一索引、普通索引等

- 普通索引：允许在索引列插入重复值并且可以为空值
- 唯一索引：不允许在索引列插入重复值但可以为空值（普通索引+不重复值）
- 主键索引：不允许在索引列插入重复值也不可以为空值 （唯一索引+不为空）

### table1表id字段添加主键索引，name字段添加普通索引

```shell
# 创建表时直接指定索引
mysql> CREATE TABLE `table1` (
	`id` INT ( 11 ) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR ( 255 ) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY pk_id ( `id` ),
INDEX idx_name ( `name` ) 
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

# 通过alter修改table1表结构，指定id主键索引
mysql> ALTER TABLE table_test ADD PRIMARY KEY pk_id ( `id` );
# 通过alter修改table1表结构，指定name普通索引
mysql> ALTER TABLE table1 ADD INDEX idx_name ( `name` );
```

### table2表id字段添加主键索引，name字段添加唯一索引

```shell
# 创建表时直接指定索引
CREATE TABLE `table2` (
	`id` INT ( 11 ) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR ( 255 ) COLLATE utf8mb4_unicode_ci NOT NULL,
	PRIMARY KEY pk_id ( `id` ),
UNIQUE uk_name ( `name` ) 
) ENGINE = INNODB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

# 通过alter修改table2表结构，指定id主键索引
mysql> ALTER TABLE table_test ADD PRIMARY KEY pk_id ( `id` );
# 通过alter修改table2表结构，指定name唯一索引
mysql> ALTER TABLE table1 ADD UNIQUE uk_name ( `name` );
```

### 查看table1索引

```shell
mysql> show index from db1.table1\G;
*************************** 1. row ***************************
        Table: table1
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: id
    Collation: A
  Cardinality: 2
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
*************************** 2. row ***************************
        Table: table1
   Non_unique: 1
     Key_name: idx_name
 Seq_in_index: 1
  Column_name: name
    Collation: A
  Cardinality: 2
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
2 rows in set (0.00 sec)
```

### 查看table2索引

```shell
mysql> show index from db1.table2\G;
*************************** 1. row ***************************
        Table: table2
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: id
    Collation: A
  Cardinality: 2
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
*************************** 2. row ***************************
        Table: table2
   Non_unique: 0
     Key_name: uk_name
 Seq_in_index: 1
  Column_name: name
    Collation: A
  Cardinality: 2
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
2 rows in set (0.06 sec)
```
