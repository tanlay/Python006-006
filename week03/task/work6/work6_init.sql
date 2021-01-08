-- 创建数据库
CREATE DATABASE geek;
-- 建表通过ORM

-- 初始化数据表
INSERT INTO `geek`.`userinfo`(`uid`, `uname`) VALUES (1000001, '张三');
INSERT INTO `geek`.`userinfo`(`uid`, `uname`) VALUES (1000002, '李四');
INSERT INTO `geek`.`assets`(`uid`, `total_amount`) VALUES (1000001, 100.00);
INSERT INTO `geek`.`assets`(`uid`, `total_amount`) VALUES (1000002, 0.95);