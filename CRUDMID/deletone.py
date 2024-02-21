from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

uri = "mongodb+srv://kowshikavula14:Smileysmiley183@cluster0.prsfy7f.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to the 'employee_management' database
    db = client.employee_management

    # Get reference to the 'employees' collection
    employees_collection = db.employees

    # Define the filter to identify the document to delete
    filter_criteria = {"employee_id": "EMP002"}  # Example filter criteria

    # Use delete_one() to delete the document
    result = employees_collection.delete_one(filter_criteria)

    # Print information about the delete operation
    print("Deleted %d document" % result.deleted_count)

except Exception as e:
    print(e)
finally:
    # Close the connection
    client.close()
