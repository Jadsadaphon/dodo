import mysql.connector
'''
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="longteset",
)

mycursor = mydb.cursor(dictionary=True)

#sql = "SELECT name,hw_name,status,value,id FROM hard_ware"
sql = "SELECT * FROM hard_ware"


mycursor.execute(sql)

data = mycursor.fetchall()

for i in data:
    print(i)
'''
def conDB():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="longteset",
        ) 
    return mydb

class Con:
    def gethw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "SELECT * FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data

    def getname():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "SELECT name FROM hard_ware"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data
    
    def inserthw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "INSERT INTO hard_ware(name,hw_name,status,value)VALUES('ball','Light','OFF',0)"
        mycursor.execute(sql)
        mydb.commit()
        ID = mycursor.lastrowid
        mycursor.close()
        mydb.close()
        return ID

    def updatehw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "UPDATE hard_ware SET status = 'ON' WHERE id = 7"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def deleteehw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "DELETE FROM hard_ware WHERE id = 113"
        mycursor.execute(sql)
        mydb.commit()
        mycursor.close()
        mydb.close()
        return True

    def selectminhw():
        mydb = conDB()
        mycursor = mydb.cursor(dictionary=True) 
        sql = "SELECT * FROM hard_ware WHERE id = (SELECT MIN(id) FROM hard_ware)"
        mycursor.execute(sql)
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data


data = Con.gethw()
print(data)