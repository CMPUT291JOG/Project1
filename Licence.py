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

def licence_input(cur):
  
    # create and initialize variables
    file = None
    blobvar = db.var(cx_Oracle.BLOB)
    try_again = True
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
	sin = input ('Enter Social insurance number: ')

    licence_class = input ('Enter licence class: ')
    while len(licence_class) > 10:
	print('Invalid licence class iput.')
	licence_classhg = input ('Enter Licence class: ')

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
		return
	    else:
		print("invalid input")
		
    print("Input Successfull!")

    while try_again == True:
		try_again = input("Do you want to input another? (y/n)")
		if try_again == y:
		    licence_input(cur)
		    return
		elif try_again == n:
		    return
		else:
		    try_again = True
		    print("invalid input")    
