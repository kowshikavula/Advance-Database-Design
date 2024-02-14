from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://kowshikavula14:Smileysmiley183$@cluster0.6woaqse.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'bank' database
    db = client.bank

    # Get reference to 'accounts' collection
    accounts_collection = db.accounts

    # Define the query to find documents with balance less than or equal to $5000
    query = {"balance": {"$lte": 5000}}

    # Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
    cursor = accounts_collection.find(query)

    # Iterate over the cursor and print the documents
    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()

    print("# of documents found: " + str(num_docs))

except Exception as e:
    print(e)
finally:
    client.close()
