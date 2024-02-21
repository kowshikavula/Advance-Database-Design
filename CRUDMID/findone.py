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

    # Define a query to find a single document
    query = {"employee_id": "EMP002"}

    # Find one document matching the query
    result = employees_collection.find_one(query)

    if result:
        pprint(result)  # Print the document if found
    else:
        print("Document not found")

except Exception as e:
    print(e)
finally:
    # Close the connection
    client.close()
