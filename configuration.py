from flask import Flask
from flask_restx import Api
from flask_cors import CORS
import pymongo
import firebase_admin
from firebase_admin import firestore, initialize_app, credentials
import os

global db, api, app, message_queue, col

def init():

    global db

    # ---- MongoDB ----
    # Initialize mongo client and connect to the mongo server

    # Local mongo server
    # client = pymongo.MongoClient(host=["mongodb://localhost:27017/"])

    # Container mongo server
    # client = pymongo.MongoClient(host=[os.environ.get("ME_CONFIG_MONGODB_URL")])

    # Get the database reference
    # db = client[f"test_db"]

    # ---- Firestore ----

    # Initialize firestore when using Google Cloud Products (Cloud Run, Cloud Functions, etc).
    initialize_app()
    db = firestore.client()

    # Initialize firestore for non-Google products.
    # cred = credentials.Certificate("ntua-project-firebase-adminsdk-ew0dg-f6077fc3c5.json")
    # firebase_admin.initialize_app(cred)
    # db = firestore.client()

    # Initialize Flask application
    global api, app
    app = Flask(__name__)
    CORS(app)
    api = Api(app=app, version="1.0", title="SaaS project")

    return app
