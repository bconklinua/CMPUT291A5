from pymongo import MongoClient
import time

''' 
    A5T4MongoDB.py
    Created by Brad Conklin, Mashiad Hasan and Klyde Pausang
    For CMPUT 291 - Assignment 5
    University of Alberta
    Winter 2021
'''

def connect_mongoDB():

    global client, db, listings

    # Connect to the default port on localhost for the mongodb server.
    client = MongoClient()

    # Open the A5db database on server.
    db = client["A5db"]

    listings = db["listings"]

    return

def handle_task():
    '''
    run the MongoDB query 20 times and 
    find the average running time in ms
    '''
    
    '''
    arguments for MongoDB query
    '''
    query = {"$or": [{"reviews":[]}, {"reviews":{"$exists":False}}, {"reviews":None}]}
    projection = {"id":1, "name":1, "_id":0 }

    start_time = time.time()

    for i in range (0,20):

        c = db.listings.find(query,projection).sort("id",1).limit(10)
    
    q = ((time.time() - start_time)*1000)/20
    q = "{:.3f}".format(q)

    print('*'*70)

    '''
    output the task result
    '''
    dict_array = list(c)

    print('|  {:^9s}  | {:^50s}     '.format('id','name'))
    print('-'*70)

    for dict1 in dict_array:

        print('| {:>9d}   | {:<50s}     '.format(dict1["id"],dict1["name"]))

    print('*'*70)
    
    '''
    display the running time
    '''
    print('Average running time for the MongoDB Query:',q,'ms')

    return 
    

def main():
    
    connect_mongoDB()

    handle_task()

    return

if __name__ == "__main__":
    main()