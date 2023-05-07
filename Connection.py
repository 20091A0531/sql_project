import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Charan@2002')
cu=mydb.cursor()
cu.execute("create database INVENTORY_MANAGEMENT")
