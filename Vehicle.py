# New Vehichle Registration
# Gemma
# This component is used to register a new vehicle by an auto registration officer.
# By a new vehicle, we mean a vehicle that has not been registered in the database. 
# The component shall allow an officer to enter the detailed information about the
# vehicle and personal information about its new owners, if it is not in the database.
# You may assume that all the information about vehicle types has been loaded in the initial database.


def newVehicleRegistration(cur):
  checkExist()
  vehicleInput()

def checkExist:
    personExist = input('Does the person registering the vehicle already exist in the database? (y/n)')
    if (personExist == 'y' or 'Y'):
      # vehicle owner already exists, retrieve their table info?
    elif (personExist == 'n'or 'N'):
      # birthday      DATE?? done right?
      
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
        # first make sure its an int, try except
        # second make sure its < 99999.99
        try: 
          int(height)
        except ValueError: 
          print('Invalid height format [format XXXXX.XX]')
          sin = input('Enter registrants height: ')
          
      weight = input('Enter registrants weight: ')
      while len(weight) > 99999.99:
        # first make sure its an int, try except
        # second make sure its < 99999.99
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
      
    else:
      print( 'Invalid Input, please answer this question again.')
      checkExist()
      

def vehicleInput():
  try_again = 0
  #all vehicle information in try/except, so if oracle returns error it can be individually handled
  try:
    serial_no = input('Please enter vehicle serial number: ')
    maker = input('Please enter vehicle maker: ')
    model = input('Please enter vehicle model: ')
    year = input('Please enter vehicle year: ')
    color = input('Please enter vehicle color: ')
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




