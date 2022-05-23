from flask import request, jsonify
from flask_restx import Resource, fields, abort

import configuration

# http methods mapping
class Data(Resource):

    def post(self):

        # Get body
        payload = request.json

        # Insert data
        dummy_collection = configuration.db['dummy_collection']
        dummy_collection.insert_one(payload)

        return {
            "statusCode": 200,
            "message": "Data added successfully!"
        }

    def get(self):

        # Get query parameters
        name = request.args.get('name', default=None, type=str)

        # name is required
        if not name:
            abort(400, f"Name is missing.", statusCode=400)

        # Query data
        dummy_collection = configuration.db['dummy_collection']
        data = [x for x in dummy_collection.find({"name": name},{"_id": 0})]

        return {
            "statusCode": 200,
            "data": data
        }

    def delete(self):

        # Get query parameters
        address = request.args.get('address', default=None, type=str)

        # address is required
        if not address:
            abort(400, f"Address is missing.", statusCode=400)

        # Delete data
        dummy_collection = configuration.db['dummy_collection']
        dummy_collection.delete_many({"address": address})

        return {
            "statusCode": 200,
            "message": "Data deleted successfully!"
        }

    def put(self):

        # Get query parameters
        address = request.args.get('address', default=None, type=str)
        new_address = request.args.get('new_address', default=None, type=str)

        # address is required
        if not address or not new_address:
            abort(400, f"Missing parameters.", statusCode=400)

        # Update data
        myquery = {"address": address}
        new_values = {"$set": {"address": new_address}}
        dummy_collection = configuration.db['dummy_collection']
        dummy_collection.update_one(myquery, new_values)

        return {
            "statusCode": 200,
            "message": "Data updated successfully!"
        }
