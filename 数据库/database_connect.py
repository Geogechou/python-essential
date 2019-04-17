# 首先在IDEA中安装python的插件，再配置Run Configuration
# “cryptography is required for sha256_password or caching_sha2_password”
# 这个异常需要安装一个包,pip install cryptography
# port需要一个整数，而不是字符串
import pymysql
try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='123456',
        db='university',
        port=3306,
        charset='utf8'
    )
    print("数据库连接对象为: "+str(conn))
    # 获取游标
    cur = conn.cursor()
    print("游标是:"+str(cur))
    # 查询语句
    sql = 'select * from student'
    cur.execute(sql)
    conn.commit()
    # 使用fetchall()获取数据对象
    data = cur.fetchall()
    # 使用fetchone()获取一条数据
    # data2 = cur.fetchone()
    for item in data:
        print(item)
    cur.close()
    conn.close()
except Exception as e:
    print(e)
