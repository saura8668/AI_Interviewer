from config.db import client

def get_all_notes():
    return client.db.notes.find()
