from flask import request, jsonify
from flask_restx import Resource, fields, abort

import configuration

class Data(Resource):

    def post(self):

        # Get body
        payload = request.json

        # Insert data
        dummy_collection = configuration.db.collection("dummy_collection")
        dummy_collection.add(payload)

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
        # Note: Use of CollectionRef stream() is preferred to get()
        docs = configuration.db.collection(u'dummy_collection').where(u'name', u'==', name).stream()
        data = [doc.to_dict() for doc in docs]

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
        docs = configuration.db.collection(u'dummy_collection').where(u'address', u'==', address).stream()
        for doc in docs:
            configuration.db.collection(u'dummy_collection').document(doc.id).delete()

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
        docs = configuration.db.collection(u'dummy_collection').where(u'address', u'==', address).limit(1).stream()
        for doc in docs:
            configuration.db.collection(u'dummy_collection').document(doc.id).update({
                u'address': new_address
            })

        return {
            "statusCode": 200,
            "message": "Data updated successfully!"
        }
