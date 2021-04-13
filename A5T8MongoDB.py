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

def printWrap(myString):
    length = len(myString)
    min_width = 60
    max_width = 70
    i = 0
    j = 0
    c = ''
    for i in range(length):
        c = myString[i]
        print(c, end="")    
        if (j > min_width):
            if (c == ' '):
                print()
                j = 0
            elif (j > max_width):
                print("-")
                j = 0
        j += 1       
    print()

def handle_task():
    '''
    run the MongoDB query 20 times and 
    find the average running time in ms
    '''
    
    '''
    arguments for MongoDB query
    '''
    
    user_input = "x"
    
    while (not user_input.isdigit()):
        user_input = input("Please enter a listing ID: ")
    user_input = int(user_input)
    
    match = {"$match": {"id": user_input}}
    unwind = {"$unwind": "$reviews" } 
    project = {"$project": { "_id": 0, "host_name": 1, "price": 1, "comments": "$reviews.comments", "date": "$reviews.date" }}
    sort = {"$sort": { "date" : -1 }}
    group = {"$group": {"_id": "$_id", "reviews": {"$push": {"host_name": "$host_name", "price": "$price", "reviews": "$reviews", "comments": "$comments", "date": "$date"}}}}
    limit = {"$limit": 1 }
    
    start_time = time.time()

    for i in range (0,20):
        c = db.listings.aggregate([match,unwind,project,sort,group,limit])
    
    q = ((time.time() - start_time)*1000)/20
    q = "{:.3f}".format(q)

    '''
    output the task result
    '''
    dict_array = list(c)
    

    if (len(dict_array) > 0):
        dict1 = dict_array[0]["reviews"][0]
        print('*'*32)
        print('|  {:^9s}      | {:^9s}  |'.format('host_name','price'))
        print('-'*32)        
        print('|  {:>9s}      | {:>9d}  |'.format(dict1["host_name"],dict1["price"]))
    else:
        print("No listing_id = " + str(user_input) + " exists.")
        return            
            
    print('*'*32)
    print("Latest Review:")
    print()
    printWrap(dict1["comments"])
    print()    
    
    
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