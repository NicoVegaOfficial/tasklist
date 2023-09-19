import pymysql

conn = pymysql.connect(
        host='localhost',
        user='nico', 
        password = "tobyX?890",
        db='tasklist'
    )

def get_task():
    sql = "select * from notes;"
    cur = conn.cursor()
    cur.execute(sql)
    output = cur.fetchall()
    return output
