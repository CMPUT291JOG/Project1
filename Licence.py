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

def licence_input(licence_num, sin, lic_class, photo, issuing_date, expiring_date):
  
  # create and initialize variables
    licence_num = ""  	# char
    sin = "" 		# char
    lic_class = ""	# char
    photo = null      	# BLOB - from local disk
    issuing_date = null 	# DATE
    expiring_date = null # Date

    licence_num = input ('Enter Licence number: ')
    sin = input ('Enter Social insurance number: ')

    lic_class = input ('Enter licence class')

    photo = input ('Insert photo ')

    issuing_date = input ('Enter issuing date')

    licence_num = input ('Enter expiring date ')
    
    return (licence_num, sin, lic_class, photo, issuing_date, expiring_date)

def licence_main():
  # get username
	user = input("Username [%s]: " % getpass.getuser())
	if not user:
  		user=getpass.getuser()
	
	# get password
	pw = getpass.getpass()

	# The URL we are connnecting to 
	conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
	
	# SQL statement to execute
	createLicence = ("create table Licence "
	"(T_NAME VARCHAR(32) PRIMARY KEY, SUP_ID INTEGER, PRICE FLOAT, SALES INTEGER, TOTAL INTEGER)")
	"(licence_no. CHAR(15) PRIMARY KEY, sin CHAR(15), class VARCHAR(10), photo BLOB, issuing_date DATE, expiring_date DATE)")
	
	try:  
	  # Establish a connection in Python
	  connection = cx_Oracle.connect(conString)

	  #create a cursor 
	  curs = connection.cursor()
	  
	  # TODO: if licence table null, create licence table
	  # curs.execute(createLicence)
	  #else continue

	  # executing a query to display
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

