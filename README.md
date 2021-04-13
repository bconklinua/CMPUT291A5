# CMPUT291A5
CMPUT 291 - Assignment 5

Contributors:
- Klyde Pausang, CCID: pausang
- Brad Conklin, CCID: bconklin
- Mashiad Hasan, CCID: mashiad

This assignment was done by these 3 students through the collaboration policy.

Each program in this assignment was created in python3.

To run the programs, simply type "python3 prog_name"
Where prog_name is the program name that wished to be run

# Task 1:
- Our task was to create a python application that will create an SQLite database from the provided CSV files, naming the database "A5.db"
- To Run:
     - Type "python3 A5T1.py"

# Task 2:
- Our task was to create a python application that will connect to a MongoDB databased called A5db and create within such a database a single collection where all the reviews associated to one given listing are embedded within that one listing.
- To Run:
     - Type "python3 A5T2.py"


# Task 3: 
- Our interpretation of this task was to find how many listings each host own, sort the host_id in ascending order, then output the first 10 host_id (Ascending Order) with its corresponding amount of listing.
- To run:
     - Type "python3 prog_name" where prog_rame can be either A5T3SQLite.py or A5T3MongoDB.py
     - Should output the result

# Task 4: 
- Our interpretation of this task was to find the ids and names of the listed properties which have not received any review, ordered by listing_id; only outputing the top 10
- To run:
     - Type "python3 prog_name" where prog_rame can be either A5T4SQLite.py or A5T4MongoDB.py
     - Should output the ids and names of the listings which haven't received any review
     - and the running times for the SQLite/MongoDB query
      
# Task 5:
- Our interpretation of this task was to take the average price of a given neighbourhood.
- To run:
     - Type "python3 prog_name" where prog_rame can be either A5T5SQLite.py or A5T5MongoDB.py
     - The program will ask the user to enter a neighbourhood
     - Once the neighbourhood has been entered, the neighbourhood with its corresponding average price will be displayed (rounded to a whole integer)

# Task 8:
- Our task was to create python files to find the host_name, price and most recent review of a listing_id provided by the user, in both SQL and MongoDB
- To run:
     - Type "python3 prog_name" where prog_name can be either A5T8SQLite.py or A5T8MongoDB.py
     - The program will ask the user to enter a listing id
     - The program will output the host_name, price and most recent review for the given listing

# Task 9:
- Our task is to create a python file to find the top 3 listings which have reviews most similar to a set of keywords provided by the user, separated by commas
- To run:
     - Type "python3 A5T9MongoDB.py"
     - Enter keywords separated by commas
     - The program will output the top 3 matching results
