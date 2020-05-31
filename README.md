# SmartSteel

***PREREQUISITE: mysql, python3, Linux preffered***

If Python3 is not installed using https://www.python.org/downloads/ as per your distribution
If mysql is not installed, please install, Please change your username and password for login to mysql if they are different from "root" and "" respectively. If change is needed, change username and password in line 5,6 of database.py and line 7,8 of API.py

**To create Database using CSV file**

To produce similar results run ```pip3 install requirements.txt``` then make sure you have some version of task_data.csv.
Now use  ```python3 task.py``` , This creates a Database with name **csv_db** and 2 tables **csvdb** and **time_log**, 

**To login to database**

run ```mysql -u root```, To verify that all csv rows are inserted in database login to your mysql and switch to database **csv_db** using ```USE csv_db;```and then run ```SELECT * FROM csvdb;``` to see all enteries of the csv_file.

**To run a webserver using flask**

run ```python3 API.py```

**To verify api working**, Open browser, Go to https://localhost/4567 or http://127.0.0.1/4567 and please note the time of using GET request.

**To verify the GET timistamp insetion**, login to your mysql then run  ```USE csv_db;``` then ```SELECT * FROM time_log;```


**Tested on OSX and Ubuntu with mysql credentials root and empty password**
