import os
from flask import Flask
from routes import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# app factory
def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    # client.drop_database("HabitTracker")
    app.db = client.get_default_database()
    print(f"The default database is: {app.db.name}")
    # app.db = client.HabitTracker

    app.register_blueprint(pages)
    return app




