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

def strip_special(myString):
    newString = ""
    for c in myString:
        if (c in "abcdefghjijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ,.<>!@#$%^&*()_+-={}[];:'"):
            newString += c  
    return newString
        

def handle_task():
    '''
    run the MongoDB query 20 times and 
    find the average running time in ms
    '''
    
    '''
    arguments for MongoDB query
    '''
    
    user_input = input("Enter a search query (comma separated): ")
    
    #.sort([('score', {'$meta': 'textScore'})]).limit(limit_value)
    # db.listings.find( {$text: { $search: "bananas" } }, {"_id": 0,"id":1,"name":1,"price":1,"host_name":1, "score": {"$meta": "textScore"}},{ score: { $meta: "textScore" } } ).sort( { score: { $meta: "textScore" } } )
    
    text = {"$text": { "$search": user_input } }
    start_time = time.time()

    for i in range (0,20):
        c = db.listings.find(text, { "score": {"$meta": "textScore"}}) .sort([("score", {"$meta": "textScore"})]).limit(3)
    
    q = ((time.time() - start_time)*1000)/20
    q = "{:.3f}".format(q)

    '''
    output the task result
    '''
    dict_array = list(c)
    
    table_width = 92
    if (len(dict_array) > 0):
                   
        print('*'*table_width)
        print('| {:^10s} |  {:^12s} | {:^37s} | {:^5s} |  {:^10s} |'.format('id','host_name','description','price','relevance'))
        print('-'*table_width)        
        for each in dict_array:
            host = strip_special(each["host_name"])
            description = strip_special(each["name"])
            if len(description) > 37:
                description = description[0:35] + ".."            
            if len(host) > 12:
                host = host[0:10] + ".."
            print('| {:10d} |  {:>12s} | {:>37s} | {:>5d} | {:>10f}  |'.format(each["id"],host,description,each["price"],each["score"]))
        print('*'*table_width)
    else:
        print("No listing_id = " + str(user_input) + " exists.")
        return            
    
    
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