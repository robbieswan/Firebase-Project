import pyrebase
import csv 
import json
import time
import getpass

firebaseConfig = {"apiKey": "Get your own ;)",
  "authDomain": "book-store-74d98.firebaseapp.com",
  "databaseURL": "https://book-store-74d98-default-rtdb.firebaseio.com",
  "projectId": "book-store-74d98",
  "storageBucket": "book-store-74d98.appspot.com",
  "messagingSenderId": "988293404072",
  "appId": "1:988293404072:web:0d68beb5ccc6403ad3b99d",
  "measurementId": "G-8G9L48CF50"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# Push Data
data = {"name":"Robbie", "age":23, "address":["New York", "Los Angeles"]}
# db.push(data)

# Create new class that turns csv data into JSON data we can import to database.

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'SalesRecords.csv'
jsonFilePath = r'data.json'

start = time.perf_counter()
csv_to_json(csvFilePath, jsonFilePath)
finish = time.perf_counter()

print(f"Conversion 100.000 rows completed successfully in {finish - start:0.4f} seconds")



# Set up authorization

auth = firebase.auth()

email = input("Please Enter Email: ")
password = getpass("Please Enter Your Password: ")

# CRUD statements.

# Locating Json File
jsonData = "data.json"

# Opening and reading in json file that we just created above.
with open(jsonData) as f:
    all_data = json.load(f)

# Removing Previous added table.
db.child("Books").remove()

# For all the items in my json file, create new relationships in database
# Make heading by country, then a child of Item Type, then push rest of data underneath that.
for item in range(100):
    # print(all_data[item]['Country'])
    db.child("Country").push(all_data[item]['Country'])
    db.child("Country").child("Item Type").push(all_data[item]['Item Type'])
    db.child("Country").child("Country Order Info").push(all_data[item])


#Delete item with unkown generated key
# BY first retrieving the child information
tasks = db.child("Country").child("Item Type").get()

for task in tasks.each():
    if task.val()[0]:
        key=task.key()

# Now delete where condition is met.
db.child("Country").child("Item Type").child(key).remove()


# Update names of data types (Item Types)
db.child("Country").child("Item Type").update({'Item Type':'Personal Care'})

