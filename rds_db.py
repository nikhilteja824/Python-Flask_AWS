import pymysql

conn = pymysql.connect(
        host= 'mydb1.c18junhzcyjw.us-east-2.rds.amazonaws.com', #endpoint link
        port = 3306, # 3306
        user = 'nikhilteja85', # admin
        password = 'Nikhil123', #pass
        db = 'mydb', #DB created in Workbench
        
        )

#Table Creation
cursor=conn.cursor()
Drop_table="""
DROP TABLE Details
"""
cursor.execute(Drop_table)
create_table="""
create table Details (ID varchar(200),name varchar(200),phone varchar(20),email varchar(200),gender varchar(20),feedback varchar(200) )

"""
cursor.execute(create_table)


def insert_details(ID,name,phone,email,gender,feedback):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (ID,name,phone,email,gender,feedback) VALUES (%s,%s,%s,%s,%s,%s)", (ID,name,phone,email,gender,feedback))
    conn.commit()

def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")

    details = cur.fetchall()
    return details