import sqlite3, time

''' 
    A5T3SQLite.py
    Created by Brad Conklin, Mashiad Hasan and Klyde Pausang
    For CMPUT 291 - Assignment 5
    University of Alberta
    Winter 2021
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

def handle_query():
    '''
    run the query 20 times and 
    find the average running time in ms
    '''
    
    start_time = time.time()
    
    for i in range (0,20):
        c.execute('''
        SELECT host_name, host_id, count(id) as amount_listing
        FROM Listings
        GROUP BY host_id 
        ORDER BY host_id ASC
        LIMIT 10
        ''')
        
    q = ((time.time() - start_time)*1000)/20
    q = "{:.3f}".format(q)
        
    print('*'*70)
        
    '''
    output the task result
    '''
    rows = c.fetchall()
    print('|  {:^9s}  | {:^50s}   | {:^9s}  '.format('id','name', 'amount'))
    print('-'*80)

    for each in rows:
        print('| {:>9d}   | {:<50s}   | {:<9d} '.format(each["host_id"],each["host_name"],each["amount_listing"]))



    
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
