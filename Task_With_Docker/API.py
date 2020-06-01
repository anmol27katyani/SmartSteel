from flask import Flask, render_template 
import datetime
import mysql.connector
from mysql.connector import Error
import csv

file1 = open("deb.txt", "r+")
for i in range(11):
    line = file1.readline() 
    if i==4:
        print (line)
        break

password=line[len(line)-17:len(line)-1]
username = "debian-sys-maint"
hostname = "localhost"

cache = {}
Data=[]
app = Flask(__name__)
connection = None
@app.route("/",methods=['GET'])
def fetch_request():
    #Establishing database connection
    connection = mysql.connector.connect(host = hostname,user = username,passwd = password, autocommit=True)
    mycursor = connection.cursor()
    mycursor.execute("USE csv_db")
    #Log current time against each GET-request
    mycursor.execute("INSERT INTO time_log (type,timestamp_of_query) VALUES(%s,%s)",("GET",datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")))
    mycursor.close()
    if len(cache)==0:
        open_file = open('task_data.csv','r')
        csv_iter = csv.reader(open_file)
        csv_data = iter(csv_iter)
        next(csv_data)
        for row in csv_data:
            Data.append(row)
    return render_template("index.html", len = len(Data), data = Data) 

if __name__=='__main__':
    app.run(host="0.0.0.0",port="4567",debug=True)
