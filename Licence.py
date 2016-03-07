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

def licence_input(cur):
  
    # create and initialize variables
    licence_num = ""  	# char
    sin = "" 		# char
    licence_class = ""	# char
    photo = null      	# BLOB - from local disk
    file = null
    issuing_date = null 	# DATE
    expiring_date = null # Date
    blobvar = db.var(cx_Oracle.BLOB)
    try_again = 0
    issue = 1
    

    # assign inputs to variables
    # should check input whether they are valid
    # if not valid, prompt proper message
    licence_num = input ('Enter Licence number: ')
    while len(licence_num) > 15:
	print('Invalid licence number input.')
	licence_num = input ('Enter Licence number: ')
	    	
    sin = input ('Enter Social insurance number: ')
    while len(sin) > 15:
	print('Invalid SIN input.')
	licence_num = input ('Enter Social insurance number: ')

    licence_class = input ('Enter licence class: ')
    while len(licence_class) > 10:
	print('Invalid licence class iput.')
	licence_num = input ('Enter Licence class: ')

    while file == null:
	photo = input ('Insert photo path: ')
	try:
	    file = open (photo,'rb') 
	except IOError :	
	    print('File not found!')
	    
    content = file.read ()
    file.close ()

    while issue == 1:    
	issuing_date = input ('Enter issuing date (ddmmyyyy): ')
	if len(issuing_date) != 8:
	    print("Invalid input")
	    continue
	else: 
	    try: 
		int(issuing_date)
	    except ValueError:
		print("invalid input")
		continue
	issue = 0
    
    issue = 1
    
    while issue == 1:    
	    expiring_date = input ('Enter expiring date (ddmmyyyy): ')
	    if len(expiring_date) != 8:
		print("Invalid input")
		continue
	    else: 
		try: 
		    int(expiring_date)
		except ValueError:
		    print("invalid input")
		    continue
	    issue = 0    
	
    datetime.datetime.strptime(issuing_date, "%d%m%Y").date()
    datetime.datetime.strptime(expiring_date, "%d%m%Y").date()


    try:

	blobvar.setvalue(0,content)
	sqlStr = "INSERT INTO Licence VALUES(licence_num, sin, lic_class, blobData, issuing_date, expiring_date"
	cur.setinputsizes (blobData = cx_Oracle.BLOB)
	cur.execute (sqlStr, {'blobData': blobvar})
    except cx_Oracle.DatabaseError as exc:
	error, = exc.args
	print( sys.stderr, "Oracle code:", error.code)
	print( sys.stderr, "Oracle message:", error.message)
	while try_again == 0:
	    try_again = input('Would you like to try input again? (y/n)')
	    if try_again == y:
		licence_input(cur)
	    elif try_again == n:
		return
	    else:
		print("invalid input")
		try_again = 0
		
