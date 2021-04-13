from pymongo import MongoClient
import time

''' 
    A5T3MongoDB.py
    Created by Brad Conklin, Mashiad Hasan and Klyde Pausang
    For CMPUT 291 - Assignment 5
    University of Alberta
    Winter 2021
'''

def connect_mongoDB():

    global client, db, listings
        
    # Connect to the default port on localhost for the mongodb server.
    client = MongoClient('mongodb://localhost:27012')
    
    # Open the A5db database on server.
    db = client["A5db"]
    
    listings = db["listings"]
    
    return

def handle_task():
    '''
    run the MongoDB query 20 times and 
    find the average running time in ms
    '''
    

    start_time = time.time()
    
    for i in range (0,20):
        
        c = db.listings.aggregate([
            {"$group": {'_id':"$host_id", 'count': {"$sum":1}}},
            {"$sort":{"_id":1}},
            {"$limit":10}
            ])
        
    q = ((time.time() - start_time)*1000)/20 
    q = "{:.3f}".format(q)
    
    print('*'*30)
    
    '''
    output the task result
    '''
    dict_array = list(c)
    
    print('|  {:^9s}  | {:^10s} '.format("host_id",'count'))
    print('-'*30)
    
    for dict1 in dict_array:
        
        print('| {:>9d}   | {:<10d} '.format(dict1["_id"],dict1["count"]))
        
    print('*'*30)
    
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
