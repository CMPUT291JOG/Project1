#-------------------------------New Vehichle Registration---------------------------------------#
# This component is used to register a new vehicle by an auto registration officer.
# A new vehicle is one that has not been registered in the database. 
# This will allow an officer to enter the detailed information of vehicle and personal information 
# with new owners, if it is not in the database.
# You may assume that all the information about vehicle types has been loaded in the initial database.
# how is it assigning these registering people to the following vehicle?
# how are we assuring there is at least one primary owner?
#---------------------------------------------------------------------------------------------
# Assume vehicle type is loaded in database with two attributes in specified format as follow:  
#      type_id     integer	an	  type    CHAR(10),
#----------------------------------------------------------------------------------------------
# A Vehicle has  8 attributes in specified format as follow accordingly:
# serial_no    CHAR(15),  maker   VARCHAR(20),  model   VARCHAR(20),
# year     number(4,0),  color    VARCHAR(10),  type_id   integer
#--------------------------------------------------------------------------------------------
# Function for vehicle input
def vehicle_input(cur):
	# try to get the SIN in proper format which is 15 character or less
	sin = input('Enter Owner SIN Number: ')
	while len(sin) > 15:
		print('Invalid SIN Number Format [too long]')
		sin = input('Enter Owner SIN Number: ')
	
	# execute query to get for matched SIN
	valid_people = "SELECT sin FROM people WHERE sin = '%s'" % (sin)
	cur.execute(valid_people)
	valid_people = cur.fetchall()
	# if result empty, no match for SIN
	if len(valid_people) == 0:
		# while SIN not found, check with user to register person or not
		while True:
			answer = input("Person not in database, Register person?(y,n) \n\t")
			# if register person, call for inputting person data
			if answer == 'y':
				person_input(cur,sin)
				break
			# if not registering person, back to main menu
			elif answer == 'n':
				print("Back to Main Menu")
				return
			# otherwise error message
			else:
				print("Invalid Input")	
	# try to check with user where this person is primary vehicle owner, with proper input
	is_primary_owner = input('Is this owner the primary vehicle owner? (y/n) \n\t')
	while ((is_primary_owner != 'y') and (is_primary_owner != 'n')):
		print ("Invalid Input")
		is_primary_owner = input('Is this owner the primary vehicle owner? (y/n)\n\t')	
	# try to get serial number in proper format for 15 character or less
	while True:
		serial_no = input('Please enter vehicle serial number: ')
		while len(serial_no) > 15:
			print('Invalid Serial Number length')
			serial_no = input('Please enter vehicle serial number: ')
		
		# execute query to confirm serial number does not already exist in database
		serials = "SELECT serial_no FROM vehicle WHERE serial_no = '%s'" % (serial_no)
		cur.execute(serials)
		inDb = cur.fetchall()
		if len(inDb) == 0:
			break
		else:
			# if vehicle already registered, check with user for registering another vehicle
			answer = input("Vehicle already registered, try new Vehicle?(y,n) \n\t")
			# if yes, continue
			if answer == 'y':
				continue
			# if no, back to main menu
			elif answer == 'n':
				print("Back to Main Menu")
				return
			# otherwise error message
			else:
				print("Invalid Input")			
	# try to get vehicle maker input in proper format 20 character or less	
	maker = input('Please enter vehicle maker: ')
	while len(maker) > 20:
		print('Invalid Maker length')
		maker = input('Please enter vehicle maker: ')
	# try to get model in format 20 character or less	
	model = input('Please enter vehicle model: ')
	while len(model) > 20:
		print('Invalid Model length')
		model = input('Please enter vehicle model: ')
	# try to get year input in 4 character
	while True:
		year = input('Please enter vehicle year [yyyy]: ')
		if len(year) != 4:
			print('Invalid Year')
			continue
		else:
			# try to convert string to integer
			try:
				year = int(year)
			# if failed, improper format and print error message
			except ValueError:
				print('Invalid Year')
				continue
			break
	# try to get vheicle color in 10 character or less	
	color = input('Please enter vehicle color: ')
	while len(color) > 10:
		print('Invalid Color length')
		color = input('Please enter vehicle color: ')
		
	# try to get type ID and check if input is integer
	while True :
		type_id = input('Please enter type_id: ')
		try: 
			int(type_id)
		# if input failed to convert to integer, print error message
		except ValueError:
			print('Invalid type Id format [Must be Integer]')
			continue
		# execute query to check type ID inputed correctly whether in database
		types = "SELECT type_id FROM vehicle_type WHERE type_id = '%s'" % (type_id)
		cur.execute(types)
		exists = cur.fetchall()
		if len(exists) > 0:
			break
		else:
			# if not, wrong input for type ID
			print("Type ID does not exist")	
	# try execute query for inserting values into vehicle table and commit
	sqlstr = "INSERT INTO vehicle VALUES (:serial_no, :maker, :model, :year, :color, :type_id)"
	try:
		cur.execute(sqlstr, {'serial_no':serial_no, 'maker':maker, 'model':model, 'year':year, 'color':color, 'type_id':type_id})
		cur.execute("commit")
  	# if failed, print error message
	except cx_Oracle.DatabaseError as exc:
		error = exc.args[0]
		print( sys.stderr, "Oracle code:", error.code)
		print( sys.stderr, "Oracle message:", error.message)
				
	# Owner table entry
	# Owner_id is the one of above entered sin number
	
	# try inserting values into owner table and commit
	while True:
	
		sqlstr = "INSERT INTO owner VALUES(:owner_id, :vehicle_id, :is_primary_owner)"
		try:
			cur.execute(sqlstr, {'owner_id':sin, 'vehicle_id':serial_no, 'is_primary_owner':is_primary_owner})
			cur.execute("commit")
		# otherwise print error messge
		except cx_Oracle.DatabaseError as exc:
			error = exc.args[0]
			print( sys.stderr, "Oracle code:", error.code)
			print( sys.stderr, "Oracle message:", error.message)  
		# check with user for inputting another owner
		while True:
			answer = input("Add another Owner?(y/n)\n\t")
			if answer == "y":
				# try to get the SIN in proper format which is 15 character or less
				sin = input('Enter Owner SIN Number: ')
				while len(sin) > 15:
					print('Invalid SIN Number Format [too long]')
					sin = input('Enter Owner SIN Number: ')
					
				# execute query to get for matched SIN
				valid_people = "SELECT sin FROM people WHERE sin = '$s'" % (sin)
				cur.execute(valid_people)
				valid_people = cur.fetchall()
				# if result empty, no match for SIN
				if len(valid_people) == 0:
					# while SIN not found, check with user to register person or not
					while True:
						answer = insert("Person not in database, Register person?(y,n) \n\t")
						# if register person, call for inputting person data
						if answer == 'y':
							person_input(cur,sin)
							break
						# if not registering person, back to main menu
						elif try_again == 'n':
							print("Back to Main Menu")
							return
						# otherwise error message
						else:
							print("Invalid Input")	
				# try to check with user where this person is primary vehicle owner, with proper input
				is_primary_owner = input('Is this owner the primary vehicle owner? (y/n) \n\t')
				while ((is_primary_owner != 'y') and (is_primary_owner != 'n')):
					print ("Invalid Input")
					is_primary_owner = input('Is this owner the primary vehicle owner? (y/n)\n\t')				
				
				break
			elif answer == 'n':
				break
			else:
				print("invalid input")
				continue
			
		if answer == "y":
			continue
		else:
			break
	# successfully input data	
	print("Input Successfull!")
	# check with user for inputting another vehicle
	while True:
		try_again = input("Do you want to input another vehichle? (y/n)")
		if try_again == 'y':
			vehicle_input(cur)
			return
		elif try_again == 'n':
			return
		else:
			print("invalid input") 

# function for inputting a person
def person_input(cur, sin):
	
	# try to get input of the person's name in 15 characters or less
	name = input('Enter Name: ')
	while len(name) > 15:
		print('Invalid Name format [max 15 char]')
		name = input('Enter Name: ')
	# try to get input for height in 8 character or less
	while True:
		height = input('Enter registrants height: ')
		# if more than 8 characters, print error
		if len(height) > 8:
			print("invalid input")
			continue
		# otherwise try converting it to float format
		else:
			try: 
				float(height)
			# if failed, print error
			except ValueError: 
				print('Invalid height format')
				continue
			break
	# try to get input weight in 8 characters or less
	while True:
		weight = input('Enter registrants weight: ')
		if len(weight) > 8:
			print("invalid input")
			continue
		else:
			try: 
				float(weight)
			except ValueError: 
				print('Invalid height format')
				continue
			break
	# try to get eyecolor in 10 characters or less	  
	eyecolor = input('Enter registrants eye color: ')
	while len(eyecolor) > 10:
		print('Invalid eyecolor format [max 10 char]')
		eyecolor = input('Enter registering eye color: ')
	# try to get hair color in 15 characters or less		
	haircolor = input('Enter registrants hair color: ')
	while len(haircolor) > 15:
		print('Invalid hair color format [max 15 char]')
		haircolor = input('Enter registrants hair color: ')
	# try to get address in 50 characters or less		
	addr = input('Enter registrants address: ')
	while len(addr) > 50:
		print('Invalid address format [only 50 characters]')
		addr = input('Enter registrants address: ')
	# try to get gender in m or f	  
	gender = input('Enter registrants gender [m/f]: ')
	while ((gender != 'm') and (gender != 'f')):
		print('Invalid gender format [m/f]')
		gender = input('Enter registrants gender [m/f]: ')
	# try to get birthday in 8 characters	  
	birthday = input('Enter registrants birthday [ddmmyyyy]: ')
	while len(birthday) != 8:
		print('Invalid birthday format [ddmmyyyy]')
		birthday = input('Enter registrants birthday [ddmmyyyy]: ')
		    
	# converting birthday to sql date format
	birthday = datetime.datetime.strptime(birthday, "%d%m%Y").date()
	
	# inputting into database
	sqlStr = 'INSERT INTO people VALUES(:sin, :name, :height, :weight, :eyecolor, :haircolor, :addr, :gender, :birthday)'
	
	# try execute query to insert values into people
	try:
		cur.execute (sqlStr, {'sin':sin, 'name':name, 'height':height, 'weight':weight, 'eyecolor':eyecolor, 'haircolor':haircolor, 'addr':addr, 'gender':gender, 'birthday':birthday})
		cur.execute ("commit")
	# if failed, print error message
	except cx_Oracle.DatabaseError as exc:
		error = exc.args[0]
		print( sys.stderr, "Oracle code:", error.code)
		print( sys.stderr, "Oracle message:", error.message)
