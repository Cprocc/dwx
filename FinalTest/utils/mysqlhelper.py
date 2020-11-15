"""
本模块的功能 。。。。。。
本模块的使用。。。。。。
适用版本。。。。。。。
"""
# -----引入模块 -----
import pymysql

# ---- 定义数据库连接 ----
DB_CONN = {'HOST': '192.168.17.8', 'USER': 'root', 'PASSWORD': '1234.Com', 'DB': 'mobile'}


def conn_mysql():
    """
    连接到mysql,并返回连接对象
    :return: conn的对象
    """
    # 实例化连接对象
    conn = pymysql.connect(DB_CONN['HOST'], DB_CONN['USER'], DB_CONN['PASSWORD'], DB_CONN['DB'])
    # 返回
    return conn


def get_db_data(sql: str):
    """
    根据SQL语句获取数据库中的数据
    :param sql: 提供的sql语句
    :return: 数据集
    """
    # 获取一个数据库连接
    conn = conn_mysql()
    # 获取一个操作指针
    cursor = conn.cursor()
    # 定义一个返回值的字典
    res = {}
    # 异常处理
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取数据库的返回值
        data = cursor.fetchall()
        # 添加返回值状态
        res['status'] = True
        # 添加要返回的数据
        res['data'] = data
    except Exception as e:
        # 添加返回值的状态
        res['status'] = False
        # 添加错误信息
        res['error'] = "获取数据库数据出现异常，具体原因：" + str(e)
    finally:
        # 无论代码有没有出现异常，都要执行的代码
        # 关闭数据库连接
        conn.close()
    # 返回
    return res


def update_db(sql: str):
    """
    更新数据库（添加、修改、删除）
    :param sql: 更新数据库提供的SQL语句
    :return: 返回更新的结果状态
    """
    # 获取一个数据库连接
    conn = conn_mysql()
    # 获取一个操作指针
    cursor = conn.cursor()
    # 定义一个返回值的字典
    res = {}
    # 异常处理
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库
        conn.commit()
        # 添加状态
        res['status'] = True
    except Exception as e:
        # 回滚操作
        conn.rollback()
        # 添加操作状态
        res['status'] = False
        # 添加错误提示
        res['error'] = "更新数据库数据出现异常，具体原因：" + str(e)
    finally:
        # 关闭数据库连接
        conn.close()

    # 返回
    return res


def bulk_insert(sql:str, data):
    """
    批量插入数据到数据库
    :param sql: sql语句模板
    :param data: 提供的数据库 -- List / Tuple
    :return: 状态
    """
    # 获取一个数据库连接
    conn = conn_mysql()
    # 获取一个操作指针
    cursor = conn.cursor()
    # 定义一个返回值字典
    res = {}
    # 开始异常处理
    try:
        # 执行SQL语句
        cursor.executemany(sql, data)
        # 提交到数据库
        conn.commit()
        # 添加运行状态
        res['status'] = True
    except Exception as e:
        # 回滚
        conn.rollback()
        # 添加运行状态
        res['status'] = False
        # 添加错误提示
        res['error'] = "批量插入数据出现异常，具体原因：" + str(e)
    finally:
        # 关闭数据连接
        conn.close()
    # 返回
    return res