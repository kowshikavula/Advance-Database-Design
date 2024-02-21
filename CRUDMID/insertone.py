# Import necessary modules
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

# Define the MongoDB connection URI
uri = "mongodb+srv://kowshikavula14:Smileysmiley183@cluster0.prsfy7f.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'employee_management' database
    db = client.employee_management

    # Get reference to 'employees' collection
    employees_collection = db.employees

    # Define a document to be inserted into the 'employees' collection
    new_employee = {
        "employee_id": "EMP001",
        "first_name": "John",
        "last_name": "Doe",
        "department": "Engineering",
        "position": "Software Engineer",
        "hire_date": datetime.datetime.utcnow(),
        "salary": 75000
    }

    # Insert the 'new_employee' document into the 'employees' collection
    result = employees_collection.insert_one(new_employee)

    # Retrieve the ID of the inserted document
    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")

except Exception as e:
    # Print any exceptions that occur
    print(e)
finally:
    # Close the MongoClient to release resources
    client.close()
