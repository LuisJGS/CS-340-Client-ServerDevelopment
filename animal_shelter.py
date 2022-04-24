from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username = 'aacuser1', password = 'animals'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:54914' % (username, password))
        self.database = self.client['AAC']
        print('login success')

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data != None:
            self.database.animals.insert(data)  # data should be dictionary
            print('Sucessfull') 
            return True           
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

# Create method to implement the R in CRUD.
    def read(self, criteria):
        # criteria is not None then this find will return all rows which matches the criteria
        if criteria != None:       
            data = self.database.animals.find(criteria,{"_id":False})
            print('read success')
        else:
        #if there is no search criteria then all the rows will be return  
            data = self.database.animals.find( {} , {"_id":False})

        print(data) 
        return data

# Create method to implement the U in CRUD
    def update(self, keyVal, updateVal):
        if updateVal != None:
            self.database.animals.update(keyVal, updateVal) #data should be dictionary
            return True
        else:
            raise Exception("Nothing to update, data parameter empty")
            return False

# Create method to implement the D in CRUD
    def delete(self, keyVal):
        if keyVal != None:
            self.database.animals.remove(keyVal) #data should be dictionary
            return True
        else:
            raise Exception("Nothing to remove, data parameter empty")
            return False