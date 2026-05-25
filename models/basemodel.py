import os

from peewee import SqliteDatabase, Model
from dotenv import load_dotenv

load_dotenv()

DATABASE = os.getenv('DATABASE')

db = SqliteDatabase(DATABASE, pragmas={'foreign_keys':1})

class BaseModel(Model):
    
    class Meta:
        database = db
        
        