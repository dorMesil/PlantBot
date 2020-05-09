
import json
# import pymongo
# from pymongo import MongoClient

from plantbot import client
# client = MongoClient("mongodb+srv://admin:admin1234@cluster0-rsh71.mongodb.net/test?retryWrites=true&w=majority")

db = client['plantbot']
data = db['plants']

def get_plant(plant_index):
    
    plant = data.find({"_id" : plant_index})
    for x in plant:
        return x
    
    
def get_plants():
    
    plants = data.find()
    
    return plants
    

def insert():
    
    with open('data.txt') as json_file:
        file = json.load(json_file)
    
    for plant in file['plants']:
        data.insert_one(plant)

    