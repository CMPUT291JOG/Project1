# New Vehichle Registration
# Gemma
# This component is used to register a new vehicle by an auto registration officer.
# By a new vehicle, we mean a vehicle that has not been registered in the database. 
# The component shall allow an officer to enter the detailed information about the
# vehicle and personal information about its new owners, if it is not in the database.
# You may assume that all the information about vehicle types has been loaded in the initial database.

# how is it assigning these registering people to the following vehicle?
# how are we assuring there is at least one primary owner?


def newVehicleRegistration(cur):
  checkExist()
  vehicleInput()

def checkExist:
    personExist = input('Does the person registering the vehicle already exist in the database? (y/n)')
    if (personExist == 'y' or 'Y'):
      # vehicle owner already exists, retrieve their table info?
    elif (personExist == 'n'or 'N'):
      
      # GETTING PERSON info 
      sin = input('Enter Social Insurance number: ')
      while len(sin) > 15:
        print('Invalid SIN input [format XXXXXXXXX]')
        sin = input('Enter Social Insurance number: ')
        
      name = input('Enter registering name: ')
      while len(name) > 15:
        print('Invalid name format [format first last]')
        sin = input('Enter registering name: ')
        
      height = input('Enter registrants height: ')
      while len(height) > 99999.99:
	# making sure its an int and larger than 99999.99
        try: 
          int(height)
        except ValueError: 
          print('Invalid height format [format XXXXX.XX]')
          sin = input('Enter registrants height: ')
          
      weight = input('Enter registrants weight: ')
      while len(weight) > 99999.99:
        try: 
          int(weight)
        except ValueError: 
          print('Invalid weight format [format XXXXX.XX]')
          weight = input('Enter registrants weight: ')
          
      eyecolor = input('Enter registrants eye color: ')
      while len(eyecolor) > 10:
        print('Invalid eyecolor format [format XXXXXXXXXX]')
        eyecolor = input('Enter registering eye color: ')
        
      haircolor = input('Enter registrants hair color: ')
      while len(haircolor) > 15:
        print('Invalid hair color format [format XXXXXXXXXX]')
        haircolor = input('Enter registrants hair color: ')
        
      addr = input('Enter registrants address: ')
      while len(addr) > 50:
        print('Invalid address format [only 50 characters]')
        sin = input('Enter registrants address: ')
      
      gender = input('Enter registrants gender [m/f]: ')
      while len(gender) > 1:
        print('Invalid gender format [m/f]')
        sin = input('Enter registrants gender [m/f]: ')
      
      birthday = input('Enter registrants birthday [ddmmyyyy]: ')
      while len(birthday) > 8:
        print('Invalid birthday format [ddmmyyyy]')
        sin = input('Enter registrants birthday [ddmmyyyy]: ')
        
        
     # converting birthday to sql date format
    datetime.datetime.strptime(birthday, "%d%m%y").date()
    
    # inputting into database
    sqlStr = 'INSERT INTO people VALUES(sin, name, height, weight, eyecolor, haircolor, addr, gender, birthday)
    
    try:
	cur.execute (sqlStr)
    except cx_Oracle.DatabaseError as exc:
	print ("Person already in database. \nNo new entry created.")
	while True:
	    try_again = input('Would you like to try new input? (y/n)')
	    if try_again == 'y' or 'Y':
		checkExist(cur)
		return
	    elif try_again == 'n' or 'N':
		return
	    else:
		print("invalid input")

     
     another_owner = input('Would you like to add another owner? (y/n)')
     if another_owner == 'y' or 'Y':
     	# goes to top of function
     	checkExist()
     else:
     	# finishes loop to go to vehicle input 
     	continue
    
      
    else:
      print( 'Invalid Input, please answer this question again.')
      checkExist()
      
   
      

def vehicleInput():
  try_again = 0
  #all vehicle information in try/except, so if oracle returns error it can be individually handled
  try:
    serial_no = input('Please enter vehicle serial number: ')
    while len(serial_no) > 15:
    	print('Invalid Serial Number length')
    	serial_no = input('Please enter vehicle serial number: ')
    	
    maker = input('Please enter vehicle maker: ')
    while len(maker) > 20:
    	print('Invalid Maker length')
    	maker = input('Please enter vehicle maker: ')
    	
    model = input('Please enter vehicle model: ')
    while len(model) > 20:
    	print('Invalid Model length')
    	model = input('Please enter vehicle model: ')
    	
    year = input('Please enter vehicle year [yyyy]: ')
    while len(year) > 4:
    	try: 
          int(year)
        except ValueError: 
          print('Invalid year format [format yyyy]')
          year = input('Please enter vehicle year [yyyy]: ')
    	
    color = input('Please enter vehicle color: ')
    while len(color) > 10:
    	print('Invalid Color length')
    	color = input('Please enter vehicle color: ')
    	
    type_id = input('Please enter type_id: ')
    try:
    	int(type_id)
    except ValueError:
    	print('Invalid Type Id [numbers only]')
    	type_id = input('Please enter type_id: ')
    curs.execute("INSERT INTO vehicle VALUES(serial_no, maker, model, year, color, type_id))
  except cx_Oracle.DatabaseError as exc:
	  error = exc.args
	  print( sys.stderr, "Oracle code:", error.code)
	  print( sys.stderr, "Oracle message:", error.message)
	  while try_again == 0:
	    try_again = input('Would you like to try input again? (y/n)')
	    if try_again == y:
		    vehicleInput(cur)
	    elif try_again == n:
		    return
	    else:
		    print("invalid input")
		    try_again = 0




