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
  personInput()
  vehicleInput()

def personInput:
    try_again = 0
    # ask for sin to see if it exists
    sin = input('Enter the SIN of the vehicles primary owner: ')
    # assuming execute field operates like string formatting
    cur.execute('SELECT sin FROM people WHERE sin = %s') % (sin)
    sins = cur.fetchall()
    
    if (sins > 0):
      # if query returns result, the sin exists therefore the
      # vehicle owner already exists in table, may need to set row to sin?
    else:
      
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
         
     # following complete person info retrieval   
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
			personInput(cur)
			return
		elif try_again == 'n' or 'N':
			return
		else:
			print("invalid input")
			
    another_owner = input('Would you like to add another owner? (y/n)')
    if another_owner == 'y' or 'Y':
        # goes to top of function
     	personInput(cur)
    else:
     	# finishes loop to go to vehicle owner input 
     	continue
 
    
def vehicleInput(cur):
  try_again = 0
  
  #all vehicle information in try/except, so if oracle returns error it can be individually handled
  try:
    serial_no = input('Please enter vehicle serial number: ')
    # Query to make sure serial doesnt already exist in database
    cur.execute('SELECT serial_no FROM vehicle WHERE serial_no = %s') % (serial_no)
    serial_nos = cur.fetchall()
    
    if (serial_nos > 0):
      # if query returns result, the sin exists therefore the
      # vehicle registration cannot continue, return to beginning loop
      vehicleInput(cur)
      
    else:
    	continue
    
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
		    
  # Owner table entry
  # Owner_id is the one of above entered sin number
  
  owner_id = input('Enter owner id [one of the entered SIN numbers]: ')
  # Query to make sure owner sin exists, cant continue until matched
  cur.execute('SELECT sin FROM people WHERE sin = %s') % (owner_id)
  sins = cur.fetchall()
  while sins == 0:
  	# sin match not found
  	print('Owner ID doesnt exist, try again [must be registered sin number]
  	owner_id = input('Enter owner id: ')
	cur.execute('SELECT sin FROM people WHERE sin = %s') % (owner_id)
	sins = cur.fetchall()
	
  vehicle_id = input('Enter vehicle if [one of the entered serial numbers]: ')
  # Query to make sure vehicle serial_no exists, cont continue until matched
  cur.execute('SELECT serial_no FROM vehicle WHERE serial_no = %s') % (vehicle_id)
  serials = cur.fetchall()
  while serials == 0:
  	print('Vehicle Number doesnt exist, try again [must be registered serial number]')
  	vehicle_id = input('Enter vehicle ID: ')
	cur.execute('SELECT serial_no FROM vehicle WHERE serial_no = %s') % (vehicle_id)
	serials = cur.fetchall()
	
  is_primary_owner = input('Is this owner the primary vehicle owner? [ONLY answer y or n]')
  if is_primary_owner == 'y':
  	# if answering yes, need to make sure that there is not already a primary 
  	# query returns this vehicles owners marked yes
  	cur.execute('SELECT * FROM owner, vehicle WHERE vehicle.serial_no = owner.vehicle_id AND owner.is_primary_owner = \'y'')
  	primaries = cur.fetchall()
  	if primaries != 0:
  		print('Primary owner already exists, not setting as primary owner and continuing')
  		is_primary_owner = 'n'
  
  else:
  	# no input, can be used, then continue
  	continue
    
  
     



