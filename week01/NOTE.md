本周主要学习一下知识点：

## github的使用包括其基本命令
    - git config
    - git clone
    - git add filename
    - git commit -m "xxxx"
    - git push

## Python虚拟环境
    - 创建虚拟环境: python3 -m venv prod
    - 进入虚拟环境: source prod/bin/activate
    - 退出虚拟环境: deactivate
    - pip更换镜像源
    - pip install 
    - pip uninstall
    - pip freeze > requirements.txt
    - pip install -r requirements.txt


## Python基本数据类型

### 空类型
None：不是0，也不是空字符串，而是一个空对象，可以把None赋值给一个变量。eg: n = None,使用 n is None 判断输出True。

### 数值型
数值型包括整型、浮点型以及复数。整形和浮点型支持加、减、乘、除等数学运算。eg: 1+1=2,1.0+1=2.0
整型和浮点型也可以相互转换。eg: int(3.14)为3,float(2)为2.0

### 序列
序列包括字符串、列表、元组
#### 字符串
字符串可以用"",'',"""""",''''''来表示,其中三引号中的字符串可以跨越多行，直至匹配到下一个未转义三引号为之。eg: str1 = 'abc123',str2="Let's go!"
##### 字符串的常用方法
str = 'abc123CBA321'

    - capitalize()将字符串首位大写，其余小写。str.capitalize()为'Abc123cba321'
    - count()返回子串在字符串中出现的次数。str.count('a')为1
    - find()返回自左至右被找到的最小索引。str.find('3')为5
    - rfind()返回自右至左被找到的最小索引。str.rfind('3')为9
    - format()格式化字符串。"1+2={}".format(1+2)为'1+2=3'
    - upper()将所有字母转化为大写。str.upper()为'ABC123CBA321'
    - lower()将所有字母转化为小写。str.lower()为'abc123cba321'
    - 

#### 列表
列表属于可变序列，可以使用一对方括号标识列表，其中以逗号分隔。lis1 = [a,b,1,2,3]， lis2 = [ x for x in range(1,11) ]
##### 列表常用方法
以下方法都没有初始化列表。都是在上一步执行后直接执行。list = [ x for x in range(11,1,-1) if x % 2 == 0]

    - append()追加一个新元素到列表中。list.append(12)为[10, 8, 6, 4, 2, 12]
    - count()返回元素在列表中出现的次数。list.count(10)为1
    - insert()在列表的某个位置插入数据。list.insert(0,8)为[8, 10, 8, 6, 4, 2, 12]
    - reverse()转置列表。list.reverse()为[12, 2, 4, 6, 8, 10, 8]
    - pop()往后删除列表元素。list.pop()为[12, 2, 4, 6, 8, 10]
    - sort()排序列表。list.sort()为[2, 4, 6, 8, 10, 12]
    - remove()从列表移除指定元素。list.remove(6)为[2, 4, 8, 10, 12]
    - extend()把指定可迭代的序列追加到列表中。list.extend('123')为[2, 4, 8, 10, 12, '1', '2', '3']
    - clear()清空列表。list.clear()为[]

#### 元组
元组属于不可变续序列，可以使用一对小括号标识列表，其中以逗号分隔。tup = (a,b,1,2,3)
##### 元组常用方法
tup = (1,2,3,2,1)
    - count()返回指定元素在元组中的个数。tup.count(2)为2
    - index()返回自左至右被找到的最小索引。tup.index(1)为0

### 字典
字典可以通过逗号分隔的key:value来创建dic = {'name': 'tom', 'age': 18}
#### 字典常用方法
    - dic.get()指定key获取value。不存在则返回None
    - dic.items()获取所有键值对。
    - dic.keys()获取所有键
    - dic.values()获取所有值
    - 通过dic['key']='value'增加新键值。
    - 通过del dic['key']删除键值对。
    - dic.update()用一个字典更新另一个字典，如果被更新的字典中没有无对应的键值对，则新增到该字典中。
    - dic.fromkeys()创建新字典，参数1为可迭代对象，参数2为新字典的value值。该方法将参数1打散作为key，参数2作为value值
    - dic.pop()删除指定的键值对。返回值为被删除的键值对的值
    - dic.popitem()从末尾删除一个键值对，返回值为被删除的键值对的值

### 布尔型
布尔值是两个常量对象 False 和 True。 被用来表示逻辑上的真假。

### 函数
函数是通过函数定义创建的，通过func(argv-list)调用。
## Python常用标准库

### os.path模块
主要用于对路径做操作，通过import os导入
#### os.path常用方法
    - os.path.abspath(path)返回路径path的绝对路径
    - os.path.basename(path)返回path的文件名称
    - os.path.dirname(path)返回path的目录名称
    - os.path.getatime(path)返回path的最后访问时间
    - os.path.getmtime(path)返回path的最后修改时间
    - os.path.getctime(path)返回path的元数据最后修改时间
    - os.path.getsize(path)返回path的大小
    - os.path.isabs(path)如果path是绝对路径，返回True
    - os.path.isdir(path)如果path是一个目录，返回True
    - os.path.isfile(path)如果path是一个普通文件，返回Ture
    - os.path.split(path)将path拆分为目录和文件名的形式

### pathlib模块
采用面向对象的方式，主要用于对路径做操作,通过from pathlib import Path导入
#### pathlib常见用法
path = '/var/log/auth.log'
p = Path(path)

    - p.root 返回根路径
    - p.parent 返回父目录
    - p.name 返回文件名
    - p.suffix 返回文件扩展名
    - p.suffixes 返回文件扩展名列表
    - p.stem 返回文件名，并去除扩展名
    - p.uri() 将路径表示为file:/// 的形式
    - p.is_absolute() 路径是否为绝对路径
    - p.cwd() 返回当前路径
    - p.home() 返回当前用户家目录
    - p.stat() 返回路径的相关信息
    - p.chmod(mode) 设置路径的权限为mode
    - p.exists() 路径是否存在
    - p.group() 返回路径的用户组
    - p.is_dir() 是否是目录
    - p.is_file() 是否是文件
    - p.mkdir() 创建目录
    - p.owner() 返回文件的属主
    - p.rename() 重命名
    - p.touch() 创建文件


### time模块
用于时间的访问和转换,通过import time导入使用
#### time常见用法
    - time.asctime() 返回'Sat Dec 26 16:08:00 2020'格式的时间
    - time.localtime() 返回当地时间
    - time.sleep() 暂停指定时间，单位为秒
    - time.strftime() 把时间转换为一个元组
    - time.strptime() 根据格式解释表示时间的字符串
    - time.time() 返回从1970-01-01 00:00:00到现在的秒数

### datetime模块
基本日期和时间类型支持时间日期的数学运算,通过 import datetime或from datetime import datetime导入使用


### logging模块
Pyyhon的日志记录工具，logging模块CRITICAL，ERROR，WARNING,INFO,DEUG,NOTSET几个日志级别
使用import logging导入
#### 打印日志信息
logging.error("error message") 输出 ERROR:root:error message
#### 修改logging配置
logging.basicConfig(**kwargs)该函数有一下参数
    - filename 使用文件名创建
    - level 设置默认的日志级别
    - format 定义日志的格式
    - datefmt 指定日志中的日期、时间格式。格式与time.strftime()相同


### json模块
用于json编码和解码，使用 import json导入使用

#### json常用方法
    - json.dump() 将obj序列化为json格式
    - json.load() 将一个含json文档的文本或二进制文本反序列化为Python对象

### re模块
用于正则表达式匹配、替换、查找子串

#### 常用元字符
    - . 匹配除了换行的任意字符
    - ^ 匹配字符开头
    - $ 匹配字符结尾
    - * 匹配前面的正则式0-任意次
    - + 匹配前面的正则式1次
    - ? 匹配前面的正则式0-1次
    - {m} 匹配之前的正则式m次
    - {m,n} 匹配之前的正则式m-n次

#### re模块常用方法
    - re.search(pattern, string) 扫描整个串，找到匹配样式的第一个位置
    - re.match(pattern,string) 如过string开0或多个字符匹配到，则返回想应的匹配对象
    - re.splist(pattern,string) 用pattern分割string
    - re.findall(pattern,string) 对string返回一个不重复的pattern列表
    - re.sub(pattern,epel,string,count=0) 返回通过repl替换string最左边出现的pattern字符串 