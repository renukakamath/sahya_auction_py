import mysql.connector

database="sahya_auction"
def select(q):
    cnx=mysql.connector.connect(user='root',password='',host='localhost',database=database)
    cur=cnx.cursor(dictionary=True)
    cur.execute(q)
    result=cur.fetchall()
    cnx.close()
    cur.close()
    return result 
def insert(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database=database)
    cur = cnx.cursor(dictionary=True)
    cur.execute(q)
    result=cur.lastrowid
    cnx.commit()
    cnx.close()
    cur.close()
    return result
def update(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database=database)
    cur = cnx.cursor(dictionary=True)
    cur.execute(q)
    result=cur.rowcount
    cnx.commit()
    cnx.close()
    cur.close()
    return result
def delete(q):
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database=database)
    cur = cnx.cursor(dictionary=True)
    cur.execute(q)
    result = cur.rowcount
    cnx.commit()
    cnx.close()
    cur.close()
    return result
