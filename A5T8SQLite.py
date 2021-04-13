import sqlite3, time

''' 
    A5T4SQLite.py
    Created by Brad Conklin, Mashiad Hasan and Klyde Pausang
    For CMPUT 291 - Assignment 5
    University of Alberta
    Winter 2021
    
    Task 8 (A5T8SQLite.py and A5T8MongoDB.py): Given a listing_id at run-time 
    (e.g., using command line prompt or via an application parameter) find the 
    host_name, rental_price and the most recent review for that listing.
'''

conn = None
c = None

def connect(path):
    '''
    Connect to the sqlite3 database located at path
    '''
    global conn, c

    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute(' PRAGMA foreign_keys=ON; ')
    conn.commit()
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
    

def handle_query():
    '''
    run the query 20 times and 
    find the average running time in ms
    '''
    user_input = "x"
    
    while (not user_input.isdigit()):
        user_input = input("Please enter a listing ID: ")
    user_input = int(user_input)

    start_time = time.time()

    for i in range (0,20):
        c.execute('''SELECT host_name, price, comments FROM
                     (SELECT L.host_name, L.price, R.comments, MAX(R.date)
                     FROM Listings L JOIN Reviews R
                     WHERE L.id = R.listing_id AND L.id = :list_id)''',
                     {"list_id":user_input})
    
    q = ((time.time() - start_time)*1000)/20
    q = "{:.3f}".format(q)

    '''
    output the task result
    '''
    entry = c.fetchone()
    
    if (entry["host_name"] != None):
        print('*'*32)
        print('|  {:^9s}      | {:^9s}  |'.format('host_name','price'))
        print('-'*32)        
        print('|  {:>9s}      | {:>9d}  |'.format(entry["host_name"],entry["price"]))
    else:
        print("No listing_id = " + str(user_input) + " exists.")
        return            
            
    print('*'*32)
    print("Latest Review:")
    print()
    printWrap(entry["comments"])
    print()
    
    
    '''
    display the running time
    '''
    print('Average running time for the SQLite Query:',q,'ms')

    return

def main():
    
    global conn, c

    path = "./A5.db"
    connect(path)
    
    

    handle_query()
    
    conn.commit()
    conn.close()
    return

if __name__ == "__main__":
    main()
