import mysql.connector as mysql

mydb=mysql.connect(
	host='127.0.0.1',
	username='root',
	password='root',
	database='mydb'
	)

mycursor=mydb.cursor() # cursor object make use mysqlconnection obj to connect with mysql server

print("Create table Country")

sql="CREATE TABLE IF NOT EXISTS Country (Name VARCHAR(50),Capital VARCHAR(50),Continent VARCHAR(50),PRIMARY KEY(Name))"
mycursor.execute(sql)


print("Insert record in Person Table")

sql="INSERT INTO Country(Name,Capital,Continent) VALUES (%s,%s,%s)"
val=("India","New Delhi","Asia")

mycursor.execute(sql,val)


print("Select countries from table Country")
sql="Select * from Country"
mycursor.execute(sql)

result=mycursor.fetchall()

print(result)
mydb.commit()




