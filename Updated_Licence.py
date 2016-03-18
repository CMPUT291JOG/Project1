# python3 Licence.py  -- Driver Licence Regestration -- For Project 1
# edited: 15 Mar 2016 by Jen
#########################################################
# General information:
# Record information as needed to issue a drive licence 
# licence no.CHAR(15), sin CHAR(15), class VARCHAR(10), photo BLOB,
# issuing_date DATE, expiring_date DATE, 
# PRIMARY KEY (licence_no), UNIQUE (sin), FOREIGN KEY (sin) REFERENCES people
# assume image files are stored in a local disk system
#########################################################
# Specific Requirement:   
# -Register a new driver license (with photo) where the person does not exist in the database.
# -New person should be added.
# -Add driver license for an existing person in database.
# -Add driver license of a person who already has a license. An error message should be shown.
# Note: Most python code are referenced from lab files
########################################################
# function for inputting licence registration
def licence_main(cur):

    ## create and initialize variables
    #file = None
    #blobvar = db.var(cx_Oracle.BLOB)
    #try_again = 0
    #issue = 1
    
    # try to get SIN and in proper format, 15 character or less
    sin = input ('Enter Social insurance number: ')
    while len(sin) > 15:
	print('Invalid SIN input.')
	sin = input ('Enter Social insurance number: ')

    # execute query to get licence number by the specified SIN	
    check = "SELECT  licence_no FROM driver_licence WHERE SIN = :sin" 
    cur.execute(check)   
    rows = cur.fetchall()
    
    # if there's a driver licence by the specified SIN, error message
    if (rows != 0):
	if row[0] != null:
	    print ("Licence already exists in database and cannot be edited!")
	# if there's no licence exists, just add one
	else:
	    licence_num = input ('Enter Licence number: ')
	    while len(licence_num) > 15:
		print('Invalid licence number input.')
		licence_num = input ('Enter Licence number: ')	
	    # call input function for the rest
	    licence_input()
    # if there is no SIN and driver licence, then add new SIN and licence  
    # and then call input function for the rest
    else:
	sin = input ('Enter Social insurance number: ')
	while len(sin) > 15:
	    print('Invalid SIN input.')
	    sin = input ('Enter Social insurance number: ')
	
	licence_num = input ('Enter Licence number: ')
	while len(licence_num) > 15:
	    print('Invalid licence number input.')
	    licence_num = input ('Enter Licence number: ')	    
	licence_input()	
    return

# for inputting the rest of the input	    
def licence_input():
    # create and initialize variables
    file = None
    blobvar = db.var(cx_Oracle.BLOB)
    try_again = 0
    issue = 1

    # try to get the licence class and in proper format which is 10 character or less
    licence_class = input ('Enter licence class: ')
    while len(licence_class) > 10:
	print('Invalid licence class iput.')
	licence_class = input ('Enter Licence class: ')

    # while there's nothng in file
    while file == None :
    	# try to get a photo and open it
	photo = input ('Insert photo path: ')
	try:
	    file = open (photo,'rb') 
	# if can't open photo, print error message
	except IOError :	
	    print('File not found!')
    # read file and then close it	    
    content = file.read ()
    file.close ()

    # try to get input for issuing_date in proper format length of 8
    while issue == 1:    
	issuing_date = input ('Enter issuing date (ddmmyyyy): ')
	# error message for wrong format
	if len(issuing_date) != 8:
	    print("Invalid input")
	    continue
	# otherwise try convert to integer
	else: 
	    try: 
		int(issuing_date)
	    # print error message if failed to convert to integer
	    except ValueError:
		print("invalid input")
		continue
	issue = 0
    
    # reset issue to 1
    issue = 1
    
    # try to get input for expiring_date in proper format length of 8
    while issue == 1:    
	    expiring_date = input ('Enter expiring date (ddmmyyyy): ')
	    # if not 8 character, invalid input
	    if len(expiring_date) != 8:
		print("Invalid input")
		continue
	    else: 
	    	# try to convert character to integer
		try: 
		    int(expiring_date)
		# print error message if failed to convert to integer
		except ValueError:
		    print("invalid input")
		    continue
	    issue = 0    
	  
    # converting integer to date format 
    datetime.datetime.strptime(issuing_date, "%d%m%Y").date()
    datetime.datetime.strptime(expiring_date, "%d%m%Y").date()

    # get ready to insert values
    blobvar.setvalue(0,content)
    sqlStr = "INSERT INTO Licence VALUES(l_n, sin, l_c, blobData, i_d, e_d"
    cur.setinputsizes (blobData = cx_Oracle.BLOB)
    # try to execute insert to the Licence table
    try:
	cur.execute (sqlStr, {'l_n': licence_num, 'sin': sin, 'l_c': licence_class, 'blobData': blobvar, 'i_d': issuing_date, 'e_d': expiring_date"})
    # if result in error, print error message
    except cx_Oracle.DatabaseError as exc:
	print ("Licence or SIN already in database. \nNo new entry created.")
	# if failed, check if user wants to try again for new input
	while True:
	    try_again = input('Would you like to try new input? (y/n)')
	    # if yes, call the function again
	    if try_again == y:
		licence_input(cur)
		return
	    # otherwise error message
	    elif try_again == n:
		print("invalid input")
    # if pass all, input success	
    print("Input Successfull!")
    # check if user want to have another input
    while True:
	try_again = input("Do you want to input another? (y/n)")
	# if so, call function again, otherwise exit
	if try_again == y:
	    licence_input(cur)
	    return
	elif try_again == n:
	    return
	else:
		return
	    else:
		print("invalid input")   
    return	    
