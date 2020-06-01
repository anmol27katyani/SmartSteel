import os
import mysql.connector
from mysql.connector import Error

username = "root"
passwd = "" #You password may be different for root please check and update as string 
class Database:
    def __init__(self):
        self.cursor = None
        os.system("mysql.server start")
        self.connection = None
        self.create_connection("localhost", username, passwd)  
        query1 = "CREATE DATABASE csv_db"
        self.create_database(query1)
        mycursor = self.connection.cursor()
        mycursor.execute("USE csv_db")
        # table creation for csv db for data        
        query3 = "CREATE TABLE csvdb (id VARCHAR(255), timesstamp VARCHAR(255) , temperature VARCHAR(200), duration VARCHAR(200))"
        self.create_table(query3)
        # Table creation for timestamp
        query4 = "CREATE TABLE time_log (type VARCHAR(255), timestamp_of_query VARCHAR(255))"
        self.create_table(query4)        

    def create_connection(self,host_name, user_name, user_password):
        self.connection = None
        self.connection = mysql.connector.connect(host = host_name,user=user_name,passwd=user_password)
        print("Connection to MySQL DB successful")
        

    def create_database(self, query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            print("Database created successfully")
        except Error as e:
            print("The error HAS occurred")

    def create_table(self,query):
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(query)
            print("Table created successfully")
        except Error as e:
            print("The error occurred")

    def insert_db(self , row ):
        mycursor = self.connection.cursor()
        mycursor.execute("INSERT INTO csvdb (id,timesstamp,temperature,duration) VALUES(%s,%s,%s,%s)", row)
        mycursor.close()
        self.connection.commit()
