from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://kowshikavula14:Smileysmiley183@cluster0.prsfy7f.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to '.employee_management' database
    db = client.employee_management

    # Get reference to '.employee_management' collection
    employees_collection = db.employees

    # Define new documents to insert
    new_employees = [
        {
            "employee_id": "EMP002",
            "first_name": "tom",
            "last_name": "mallik",
            "department": "Engineering",
            "position": "Data Engineer",
            "hire_date": datetime.datetime.utcnow(),
            "salary": 85000,
        },
        {
            "employee_id": "EMP003",
            "first_name": "queen",
            "last_name": "wow",
            "department": "Engineering",
            "position": "Testing",
            "hire_date": datetime.datetime.utcnow(),
            "salary": 95000,
        },
    ]

    # Insert the new documents into the collection
    result = employees_collection.insert_many(new_employees)

    # Extract the inserted document IDs
    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")

except Exception as e:
    print(e)
finally:
    # Close the connection
    client.close()
