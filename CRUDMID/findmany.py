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

    # Define a query to find multiple documents
    query = {"department": "Engineering"}  # Example query

    # Find documents matching the query
    results = employees_collection.find(query)

    # Print each document found
    for result in results:
        pprint(result)

except Exception as e:
    print(e)
finally:
    # Close the connection
    client.close()
