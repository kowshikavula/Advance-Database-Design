from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

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

    # Define the filter to identify the document to update
    filter_criteria = {"employee_id": "EMP002"}

    # Define the update operation
    update_operation = {
        "$set": {
            "salary": 90000,  # New salary value
            "position": "Senior Data Engineer"  # New position value
        }
    }

    # Use update_one() to update the document
    result = employees_collection.update_one(filter_criteria, update_operation)

    # Print information about the update operation
    print("Matched %d documents" % result.matched_count)
    print("Modified %d documents" % result.modified_count)

except Exception as e:
    print(e)
finally:
    # Close the connection
    client.close()
