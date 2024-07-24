- Lambda function in Python  
- Regular Expression in Python
```
. -> any Character  
.* ->  O or more characters  
.+ ->  1 or more characters  
P ->  optional  
^ ->  start of input  
$ ->  end of input
```
- SQL 
	- CREATE, INSERT - SELECT - UPDATE - DELETE, DROP
```SQL
$ sqlite3 favorites.db  -- Create new DB file
SQLite version 3.36.0 2023—02—18 14:36:39  
Enter ".help" for usage hints.  
sqlite> .mode csv  -- Entering CSV mode
sqlite> .import favorites.csv favorites -- Import data from CSV
sqlite> .schema -- Outputs a create table statement based on CSV 
```
- Indexes in SQL
	- B-Trees
- SQL Injection attack
- Race condition
	- Locks, Transaction