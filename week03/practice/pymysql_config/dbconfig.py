from configparser import ConfigParser
from pathlib import Path

p = Path(__file__)
cur_path = p.resolve().parent
dbconfig = cur_path.joinpath('dbconfig.ini')


def read_db_config(configpath=dbconfig, section='mysql'):
    """
    读数据库配置文件并返回为字典
    ：param configpath: 配置文件名字
    ：param section: 文件中的哪一部分
    ：return: 数据库参数字典
    """
    # 创建参数读取配置文件
    parser = ConfigParser()
    parser.read(configpath)

    # 获取section段
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception(f'{section} not found in the {configpath} file')
    # print(items)
    return dict(items)

if __name__ == "__main__":
    print(read_db_config())
