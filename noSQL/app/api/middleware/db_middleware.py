import os

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('mongo_url', 'localhost'), os.getenv('mongo_port', 27017))
db = client.test_database


def get_db():
    try:
        yield db
    finally:
        client.close()
