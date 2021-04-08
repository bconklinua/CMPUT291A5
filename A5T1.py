import csv
import sqlite3 as sq

'''
2 tables: Reviews, Listings

Reviews: {listing_id, id, date, reviewer_id, reviewer_name, comments}
Listings: {id, name, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365}

'''

def main():
    
    conn = sq.connect('A5.db')
    c = conn.cursor()    

    c.execute('''DROP TABLE IF EXISTS Listings''')
    c.execute('''CREATE TABLE Listings
                 ([id] integer PRIMARY KEY,
                 [name] text,
                 [host_id] integer,
                 [host_name] text,
                 [neighbourhood] text,
                 [room_type] text,
                 [price] integer,
                 [minimum_nights] integer,
                 [availability_365] integer)''')    
    
    with open('YVR_Airbnb_listings_summary.csv', encoding="utf8") as csv_listings:
        dRead = csv.DictReader(csv_listings)
        SQL_Array2 = []
        for row in dRead:
            SQL_Array2.append((row['id'], row['name'], row['host_id'], row['host_name'], row['neighbourhood'], row['room_type'], row['price'], row['minimum_nights'], row['availability_365']))
    
    c.executemany("INSERT INTO Listings (id, name, host_id, host_name, neighbourhood, room_type, price, minimum_nights, availability_365) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", SQL_Array2)    

    c.execute('''DROP TABLE IF EXISTS Reviews''')    
    c.execute('''CREATE TABLE Reviews
                 ([listing_id] integer,
                 [id] integer PRIMARY KEY,
                 [date] date,
                 [reviewer_id] integer,
                 [reviewer_name] text,
                 [comments] text,
                 FOREIGN KEY (listing_id)
                      REFERENCES Listings (id))''')
    
    with open('YVR_Airbnb_reviews.csv', encoding="utf8") as csv_reviews:
        dRead = csv.DictReader(csv_reviews)
        SQL_Array1 = []
        for row in dRead:
            SQL_Array1.append((row['listing_id'], row['id'], row['date'], row['reviewer_id'], row['reviewer_name'], row['comments']))
    
    c.executemany("INSERT INTO Reviews (listing_id, id, date, reviewer_id, reviewer_name, comments) VALUES (?, ?, ?, ?, ?, ?);", SQL_Array1)
     
    conn.commit()
    conn.close()
    
main()