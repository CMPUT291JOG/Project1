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
def licence_main(cur):

    ## create and initialize variables
    #file = None
    #blobvar = db.var(cx_Oracle.BLOB)
    #try_again = 0
    #issue = 1
    

    sin = input ('Enter Social insurance number: ')
    while len(sin) > 15:
	print('Invalid SIN input.')
	sin = input ('Enter Social insurance number: ')
	
    check = "SELECT  licence_no FROM driver_licence WHERE SIN = :sin" 
    cur.execute(check)   
    rows = cur.fetchall()
    
    if (rows != 0):
	# if query returns result, the sin exists therefore check licence
	if row[0] != null:
	    print ("Licence already exists in database and cannot be edited!")
	# if no licence exists, just add one
	else:
	    licence_num = input ('Enter Licence number: ')
	    while len(licence_num) > 15:
		print('Invalid licence number input.')
		licence_num = input ('Enter Licence number: ')	
	    # call input function for the rest
	    licence_input()
    # if query empty then input for sin and licence 
    # then call input function for the rest
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

	    
def licence_input():
    # create and initialize variables
    file = None
    blobvar = db.var(cx_Oracle.BLOB)
    try_again = 0
    issue = 1

    licence_class = input ('Enter licence class: ')
    while len(licence_class) > 10:
	print('Invalid licence class iput.')
	licence_class = input ('Enter Licence class: ')

    while file == None :
	photo = input ('Insert photo path: ')
	try:
	    file = open (photo,'rb') 
	except IOError :	
	    print('File not found!')
	    
    content = file.read ()
    file.close ()

    # input for issuing_date
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
    
    # reset issue to 1
    issue = 1
    
    # input for expiring_date
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
	  
    # convert string to date 
    datetime.datetime.strptime(issuing_date, "%d%m%Y").date()
    datetime.datetime.strptime(expiring_date, "%d%m%Y").date()

    blobvar.setvalue(0,content)
    sqlStr = "INSERT INTO Licence VALUES(l_n, sin, l_c, blobData, i_d, e_d"
    cur.setinputsizes (blobData = cx_Oracle.BLOB)

    try:
	cur.execute (sqlStr, {'l_n': licence_num, 'sin': sin, 'l_c': licence_class, 'blobData': blobvar, 'i_d': issuing_date, 'e_d': expiring_date"})
    except cx_Oracle.DatabaseError as exc:
	print ("Licence or SIN already in database. \nNo new entry created.")
	while True:
	    try_again = input('Would you like to try new input? (y/n)')
	    if try_again == y:
		licence_input(cur)
		return
	    elif try_again == n:
		print("invalid input")
		
    print("Input Successfull!")

    while True:
	try_again = input("Do you want to input another? (y/n)")
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