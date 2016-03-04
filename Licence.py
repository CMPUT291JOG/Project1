# python3 Licence.py
# File for Project 1
# edited: 03 Mar 2016 by Jen

# Driver Licence Regestration
# - record information needd to issuing a drive licence 
# licence no.CHAR(15), sin CHAR(15), class VARCHAR(10), photo BLOB,
# issuing_date DATE, expiring_date DATE, 
# PRIMARY KEY (licence_no), UNIQUE (sin), FOREIGN KEY (sin) REFERENCES people
# assume image files are stored in a local disk system
# Reference python code from lab files
import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it

def licence_main():
  # get username
	user = input("Username [%s]: " % getpass.getuser())
	if not user:
  		user=getpass.getuser()
	
	# get password
	pw = getpass.getpass()

	# The URL we are connnecting to 
	conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'

	try:  
	  # Establish a connection in Python
	  connection = cx_Oracle.connect(conString)

	  #create a cursor 
	  curs = connection.cursor()
	  
	  #if licence table null, create licence table
	  #curs.execute(createLicence)
    # else continue

	  # executing a query
	  curs.execute("SELECT * from autoTransaction")
	  # get all data and print it
	  rows = curs.fetchall()
	  for row in rows:
	    print(row)
	
	  # getting metadata
	  rows = curs.description
	  columnCount = len(rows)
  	# display column names and type
	  # (name, type, display_size,internal_size,precision,scale,null_ok)
  	for row in rows:
  	print(row[0]," ",row[1])
  	
  	# call for input
  	licence_input()

if __name__ == "__main__":
    main()

def licence_input(a, b, c, d, e, f):
  
  # create and initialize variables
    licence_num = ""
    sin = "" 
    lic_class = ""
    photo = null      # BLOB - from local disk
    issue_date = null # DATE
    summary = []

  licence no.CHAR(15), sin CHAR(15), class VARCHAR(10), photo BLOB,
# issuing_date DATE, expiring_date DATE, 
