#------------------------------- Violation Record---------------------------------------#
# This component is used by a police officer to issue a traffic ticket
# for each violation. Assume that all information in regards to the ticket type
# has been loaded and initialized to the database. 
#---------------------------------------------------------------------------------------------
# Ticket Type is initialized with two attributes in specified format as follow:  
#     vtype   CHAR(10)   and   fine number   (5,2)
#----------------------------------------------------------------------------------------------
# A violation ticket has  8 attributes in specified format as follow accordingly:
#  ticket_no     int,              violator_no   CHAR(15),     vehicle_id    CHAR(15),
#  office_no     CHAR(15),    vtype          CHAR(10),      vdate             date,
#  place        varchar(20),  descriptions varchar(1024),
#--------------------------------------------------------------------------------------------
import cx_oracle

# function for inputting violation record
def violation_input(cur):
	
	# try to get ticket_no from input in correct integer format
	# keep looping until input is correct
	while True :
		ticket_no = input('Enter Ticket Number: ')
		try: 
			int(ticket_no)
		except ValueError:
			print('Invalid Ticket Number format [Must be Integer]')
			continue
		break
	
	# get violator_no which contains 15 or less character
	# keep looping until getting the proper format
	violator_no = input('Enter Violator Number: ')
	while len(violator_no) > 15:
		print('Invalid Violator Number Format [too long]')
		violator_no = input('Enter Violator Number: ')
	
	# check if violator_no is a valid SIN and for which if it already exists
	valid_people = 'SELECT sin FROM people WHERE sin = :sin'
	# execute query to match violator and SIN
	cur.execute(valid_people, {'sin', violator_no})
	# get data
	valid_people = cur.fetchall()
	
	# while return empty, sin not match
	while len(valid_people) == 0:
		# print error message for sin not match 
		print('Violator Number doesnt exist, try again [must be registered sin number]')
		# request violator_no again until correct and exit while loop
		violator_no = input('Enter Violator Number: ')
		valid_people = 'SELECT sin FROM people WHERE sin = :sin'
		cur.execute(valid_people, {'sin', violator_no})
		valid_people = cur.fetchall()

	# get vehicle_id for charater 15 or less	
	vehicle_id = input('Enter Vehicle Identification: ')
	while len(vehicle_id) > 15:
		print('Invalid Vehicle Id Format [too long]')
		vehicle_id = input('Enter Vehicle Identification: ')
		
	# making sure vehicle id is extant serial no
	serials = 'SELECT serial_no FROM vehicle WHERE serial_no = :serial_no'
	cur.execute(serials, {'serial_no', vehicle_id})
	inDb = cur.fetchall()
	while inDb == 0:
		print('Vehicle ID Number doesnt exist, try again [must be registered serial number]')
		vehicle_id = input('Enter vehicle ID: ')
		serials = 'SELECT serial_no FROM vehicle WHERE serial_no = :serial_no'
		cur.execute(serials, {'serial no', vehicle_id})
		inDb = cur.fetchall()
	
	# input office_no for number  15 or less	
	office_no = input('Enter Officer Number: ')
	while len(office_no) > 15:
		print('Invalid Officer Number Format [too long]')
		office_no = input('Enter Officer Number: ') 
	
	# input violation type with 10 or less number	 
	vtype = input('Enter Violation Type: ')
	while len(vtype) > 10:
		print('Invalid Officer Number Format [too long]')
		vtype = input('Enter Violation Type: ')
	
	# input violation date length less than 8	
	vdate = input('Enter Violation Date [ddmmyyyy]: ')
	while len(vdate) > 8:
		print('Invalid Violation Date format')
		vdate = input('Enter Violation Date [ddmmyyyy]: ')
	
	# input place in length 20 or less
	place = input('Enter Violation Place: ')
	while len(place) > 20:
		print('Invalid violation place length')
		place = input('Enter Violation Place: ')
	
	#input descriptions no more than 1024 characters	
	descriptions = input('Enter Violation Description: ')
	while len(descriptions) > 1024:
		print('Invalid description length')
		descriptions = input('Enter Violation Description: ')
	
	# convert to date
	vdate = datetime.datetime.strptime(vdate, "%d%m%Y").date()
	
	# insert statement
	sqlstr = "INSERT INTO ticket VALUES(:ticket_no, :violator_no, :vehicle_id, :office_no, :vtype, :vdate, :place, :descriptions"
	
	# try execute sql insert statment
	try:
		curs.execute(sqlstr, {'ticket_no':ticket_no, 'violator_no':violator_no, 'vehicle_id':vehicle_id, 'office_no':office_no, 'vtype':vtype, 'vdate':vdate, 'place':place, 'descriptions':descriptions})
	# if fail, print errors	
	except cx_Oracle.DatabaseError as exc:
		error = exc.args[0]
		print( sys.stderr, "Oracle code:", error.code)
		print( sys.stderr, "Oracle message:", error.message)
		
		# allow to choose try again or not
		while True:
			try_again = input('Would you like to try new input? (y/n)')
			if try_again == 'y':
				violation_input(cur)
				return
			elif try_again == 'n':
				return
			else:
				print("invalid input")
	
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

