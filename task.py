import csv
import database as db
database = db.Database()

# Function to scrape database from csv file
def csv_crawler():
	open_file = open('task_data.csv','r')
	csv_iter = csv.reader(open_file)
	csv_data = iter(csv_iter)
	next(csv_data)
	for row in csv_data:
		database.insert_db(row)
	database.connection.cursor().close()

if __name__ == "__main__":
	csv_crawler()