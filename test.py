import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/labDB")
dataBase = client["MyLabDB"]
collection = dataBase['MyProducts']
d = {'Name': 'Aamir',
     'Age': '25',
     'Experience': '1.5'}

#rec = collection.insert_one(d)
all_record = collection.find()
for idx, record in enumerate(all_record):
     print(f"{idx}: {record}")

