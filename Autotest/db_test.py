import pymysql
import pandas as pd

class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', passwd='root', charset='utf8'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset=charset)
        # 创建游标，操作设置为字典类型
        self.cur = self.conn.cursor(cursor = pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()


if __name__ == '__main__':
    sql = 'select parent_sid from user_account where phone = 13905843198'
    db_name = 'zs_user_system'
    host = 'rm-uf60275574n809i7r90210.mysql.rds.aliyuncs.com'
    with DB(host=host, user='testuser', passwd='testuser2020', db=db_name) as db:
        db.execute(sql)
    # 查询结果
    result = db.fetchall()
    # df_result = pd.DataFrame(list(result), columns=[])
    print(result)
    # 从返回的字典列表中获取字典的值
    for dic in result:
        for key in dic:
            print(dic[key])
