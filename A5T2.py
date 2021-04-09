import sqlite3
from pymongo import MongoClient

''' 
    A5T2.py
    Created by Brad Conklin, Mashiad Hasan and Klyde Pausang
    For CMPUT 291 - Assignment 5
    University of Alberta
    Winter 2021
'''

connection = None
cursor = None

def connect_sqlite(path):
    '''
    Connect to the sqlite3 database located at path
    '''

    global connection, cursor

    connection = sqlite3.connect(path)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    return

def setup_mongoDB():

    global client, db, listings

    # Connect to a specific port
    client = MongoClient('mongodb://localhost:27012')
    # Create the A5db database on server.
    db = client["A5db"]


    collist = db.list_collection_names()
    if "listings" in collist:
        print("The collection listings exists.")

    # Create or open the collection in the db
    listings = db["listings"]

    # delete all previous entries in the listings
    # specify no condition.
    listings.delete_many({})


def create_collection():
    '''
    use a MongoDB database called A5db and create within the database 
       a single collection where all the reviews associated to one given 
       listing are to be embedded within that one listing
    '''

    '''
    get all listing ids
    '''
    cursor.execute('''Select id From Listings''')
    rows = cursor.fetchall()
    listing_ids = []
    for each in rows:
        listing_ids.append(int(each["id"]))

    '''
    all the reviews associated to a given listing are to be embedded 
    within that one listing
    '''
    for i in range (0, len(listing_ids)):

        cursor.execute('''Select *
                        From Listings L
                        Where L.id = :id''',{"id":listing_ids[i]})

        listing_info = [dict(row) for row in cursor.fetchall()]
        for dict1 in listing_info:
            listing_info = dict1
        
        cursor.execute('''Select *
                        From Reviews R
                        Where R.listing_id = :id''',{"id":listing_ids[i]})

        reviews_info = [dict(row) for row in cursor.fetchall()]
        
        listing_info['reviews'] = reviews_info

        '''
        insert the entry for the given listing
        '''
        listings.insert_one(listing_info)

    return

def test():
    '''
    testing to ensure that the ETL process works as expected
    '''

    c2 = db.listings.aggregate([{"$group": {"_id": "null", 'min': {'$min': "$host_id"}, 
                                'max': {'$max': "$host_id"}, 
                                'avg': {'$avg': "$host_id"}, 'count': {'$sum': 1}}} ])
    
    result = list(c2)
    print(result)
    
    c3 = db.listings.aggregate([{'$unwind': "$reviews"}, 
                                {'$group': {'_id': 'null', 'min': {'$min': "$reviews.id"}, 
                                'max': {'$max': "$reviews.id"}, 'avg': {'$avg': "$reviews.id"}, 
                                'count': {'$sum': 1}}}])

    result2 = list(c3)
    print(result2)

    return

def main():

    global connection, cursor

    sqlite_path = "./A5.db"
    connect_sqlite(sqlite_path)

    setup_mongoDB()
    create_collection()
    test()

    connection.commit()
    connection.close()
    return

if __name__ == "__main__":
    main()