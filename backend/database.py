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

def add_note(text):
    val = []
    val.append((text))
    cur = conn.cursor()
    sql = "insert into notes (note, created_at) values (%s, now())"
    cur.executemany(sql, val)
    conn.commit()

def edit_note(id_note, text):
    val = []
    val.append((text, id_note))
    cur = conn.cursor()
    sql = "update notes set note = %s where id_note = %s;"
    cur.executemany(sql, val)
    conn.commit()

def delete_note(id_note):
    val = []
    val.append((id_note))
    cur = conn.cursor()
    sql = "delete from notes where id_note = %s"
    cur.executemany(sql, val)
    conn.commit()
