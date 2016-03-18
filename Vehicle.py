# New Vehichle Registration
# Gemma
# This component is used to register a new vehicle by an auto registration officer.
# By a new vehicle, we mean a vehicle that has not been registered in the database. 
# The component shall allow an officer to enter the detailed information about the
# vehicle and personal information about its new owners, if it is not in the database.
# You may assume that all the information about vehicle types has been loaded in the initial database.

# how is it assigning these registering people to the following vehicle?
# how are we assuring there is at least one primary owner?

def vehicleInput(cur):

	sin = input('Enter Owner SIN Number: ')
	while len(sin) > 15:
		print('Invalid SIN Number Format [too long]')
		sin = input('Enter Owner SIN Number: ')
	
	valid_people = 'SELECT sin FROM people WHERE sin = :sin'
	cur.execute(valid_people, {'sin', violator_no})
	valid_people = cur.fetchall()
	if len(valid_people) == 0:
		# sin match not found
		while True:
			answer = insert("Person not in database, Register person?(y,n) \n\t")
			if answer == 'y':
				person_input(cur,sin)
				break
			elif try_again == 'n':
				print("Back to Main Menu")
				return
			else:
				print("Invalid Input")	
	
	is_primary_owner = input('Is this owner the primary vehicle owner? (y/n) \n\t')
	while ((is_primary_owner != 'y') and (is_primary_owner != 'n')):
		print ("Invalid Input")
		is_primary_owner = input('Is this owner the primary vehicle owner? (y/n)\n\t')	

	while True:
		serial_no = input('Please enter vehicle serial number: ')
		while len(serial_no) > 15:
			print('Invalid Serial Number length')
			serial_no = input('Please enter vehicle serial number: ')
		
		# Query to make sure serial doesnt already exist in database
		serials = 'SELECT serial_no FROM vehicle WHERE serial_no = :serial_no'
		cur.execute(serials, {'serial_no', vehicle_id})
		inDb = cur.fetchall()
		if len(inDb) == 0:
			break
		else:
			answer = insert("Vehicle already regestered, try new Vehicle?(y,n) \n\t")
			if answer == 'y':
				continue
			elif try_again == 'n':
				print("Back to Main Menu")
				return
			else:
				print("Invalid Input")			
	 	
	maker = input('Please enter vehicle maker: ')
	while len(maker) > 20:
		print('Invalid Maker length')
		maker = input('Please enter vehicle maker: ')
		
	model = input('Please enter vehicle model: ')
	while len(model) > 20:
		print('Invalid Model length')
		model = input('Please enter vehicle model: ')
	
	while True:
		year = input('Please enter vehicle year [yyyy]: ')
		if len(year) != 4:
			print('Invalid Year')
			continue
		else:
			try:
				year = int(year)
			except ValueError:
				print('Invalid Year')
				continue
			break
		
	color = input('Please enter vehicle color: ')
	while len(color) > 10:
		print('Invalid Color length')
		color = input('Please enter vehicle color: ')
		
	
	while True :
		type_id = input('Please enter type_id: ')
		try: 
			int(type_id)
		except ValueError:
			print('Invalid type Id format [Must be Integer]')
			continue
		
		types = 'SELECT type_id FROM vehicle_type WHERE type_id = :type_id'
		cur.execute(types, {'type_id', type_id})
		exists = cur.fetchall()
		if len(exists) > 0:
			break
		else:
			print("Type ID does not exist")	
	
	sqlstr = "INSERT INTO vehicle VALUES(:serial_no, :maker, :model, :year, :color, :type_id"
	try:
		curs.execute(sqlstr, {'serial_no':serial_no, 'maker':maker, 'model':model, 'year':year, 'color':color, 'type_id':type_id})
  
	except cx_Oracle.DatabaseError as exc:
		error = exc.args[0]
		print( sys.stderr, "Oracle code:", error.code)
		print( sys.stderr, "Oracle message:", error.message)
				
	# Owner table entry
	# Owner_id is the one of above entered sin number

	while True:
	
		sqlstr = "INSERT INTO owner VALUES(:owner_id, :vehicle_id, :is_primary_owner"
		try:
			curs.execute(sqlstr, {'owner_id':sin, 'vehicle_id':serial_no, 'is_primary_owner':is_primary_owner})
		except cx_Oracle.DatabaseError as exc:
			error = exc.args[0]
			print( sys.stderr, "Oracle code:", error.code)
			print( sys.stderr, "Oracle message:", error.message)  
		
		while True:
			answer = input("Add another Owner?(y/n)\n\t")
			if answer == "y":
			
				sin = input('Enter Owner SIN Number: ')
				while len(sin) > 15:
					print('Invalid SIN Number Format [too long]')
					sin = input('Enter Owner SIN Number: ')
					  
				valid_people = 'SELECT sin FROM people WHERE sin = :sin'
				cur.execute(valid_people, {'sin', violator_no})
				valid_people = cur.fetchall()
				if len(valid_people) == 0:
					# sin match not found
					while True:
						answer = insert("Person not in database, Register person?(y,n) \n\t")
						if answer == 'y':
							person_input(cur,sin)
							break
						elif try_again == 'n':
							print("Back to Main Menu")
							return
						else:
							print("Invalid Input")	
				
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
		
	print("Input Successfull!")
	
	while True:
		try_again = input("Do you want to input another? (y/n)")
		if try_again == 'y':
			violation_input(cur)
			return
		elif try_again == 'n':
			return
		else:
			print("invalid input") 


def person_input(cur, sin):
	
	name = input('Enter Name: ')
	while len(name) > 15:
		print('Invalid Name format [max 15 char]')
		sin = input('Enter Name: ')
	
	while True:
		height = input('Enter registrants height: ')
		if len(height) > 8:
			print("invalid input")
			continue
		else:
			try: 
				float(height)
			except ValueError: 
				print('Invalid height format')
				continue
			break

	
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
		  
	eyecolor = input('Enter registrants eye color: ')
	while len(eyecolor) > 10:
		print('Invalid eyecolor format [max 10 char]')
		eyecolor = input('Enter registering eye color: ')
		
	haircolor = input('Enter registrants hair color: ')
	while len(haircolor) > 15:
		print('Invalid hair color format [max 15 char]')
		haircolor = input('Enter registrants hair color: ')
		
	addr = input('Enter registrants address: ')
	while len(addr) > 50:
		print('Invalid address format [only 50 characters]')
		sin = input('Enter registrants address: ')
	  
	gender = input('Enter registrants gender [m/f]: ')
	while ((gender != 'm') and (gender != 'f')):
		print('Invalid gender format [m/f]')
		sin = input('Enter registrants gender [m/f]: ')
	  
	birthday = input('Enter registrants birthday [ddmmyyyy]: ')
	while len(birthday) != 8:
		print('Invalid birthday format [ddmmyyyy]')
		sin = input('Enter registrants birthday [ddmmyyyy]: ')
		    
	# converting birthday to sql date format
	birthday = datetime.datetime.strptime(birthday, "%d%m%y").date()
	
	# inputting into database
	sqlStr = 'INSERT INTO people VALUES(:sin, :name, :height, :weight, :eyecolor, :haircolor, :addr, :gender, :birthday)'
	
	try:
	  	cur.execute (sqlStr, {'sin':sin, 'name':name, 'height':height, 'weight':weight, 'eyecolor':eyecolor, 'haircolor':haircolor, 'addr':addr, 'gender':gender, 'birthday':birthday})
	except cx_Oracle.DatabaseError as exc:
		error = exc.args[0]
		print( sys.stderr, "Oracle code:", error.code)
		print( sys.stderr, "Oracle message:", error.message)