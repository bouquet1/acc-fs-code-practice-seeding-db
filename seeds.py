from models import User, Meal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db')

Session = sessionmaker(bind=engine)
session = Session()

import random 
import json # https://www.w3schools.com/python/python_json.asp
import requests # https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content

print("🌱 Seeding DB...") 

# Reset DB
session.query(User).delete()

# Use faker to seed 30 Users
    # first_name
    # last_name
    # username - could do first_name_last_name
    # email - username@gmail.com

# Use the Meals DB to populate the meals
# Link: https://www.themealdb.com/api/json/v1/1/search.php?f=a
# Random element from list: https://docs.python.org/3/library/random.html?highlight=random#random.sample

print("✅ Done seeding!")

import ipdb; ipdb.set_trace()