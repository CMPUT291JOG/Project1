# Violation Record
# Gemma
# This component is used by a police officer to issue a traffic ticket
# and record the violation. You may assume that all the information about
# ticket_type has been loaded in the initial database.

# assume ticket_type already initialized with:  vtype CHAR(10) and fine number(5,2),
# Violation as Ticket records should contain:
#  ticket_no     int,
#  violator_no   CHAR(15),  
#  vehicle_id    CHAR(15),
#  office_no     CHAR(15),
#  vtype        char(10),
#  vdate        date,
#  place        varchar(20),
#  descriptions varchar(1024),
import cx_oracle

def violation_input(cur):
	while True :
		ticket_no = input('Enter Ticket Number: ')
		try: 
			int(ticket_no)
		except ValueError:
			print('Invalid Ticket Number format [Must be Integer]')
			continue
		break
			
	violator_no = input('Enter Violator Number: ')
	while len(violator_no) > 15:
		print('Invalid Violator Number Format [too long]')
		violator_no = input('Enter Violator Number: ')
	
	# Making sure Violator_no is a valid SIN number thats already existant
	valid_people = 'SELECT sin FROM people WHERE sin = :sin'
	cur.execute(valid_people, {'sin', violator_no})
	valid_people = cur.fetchall()
	while len(valid_people) == 0:
		# sin match not found
		print('Violator Number doesnt exist, try again [must be registered sin number]')
		violator_no = input('Enter Violator Number: ')
		valid_people = 'SELECT sin FROM people WHERE sin = :sin'
		cur.execute(valid_people, {'sin', violator_no})
		valid_people = cur.fetchall()

		
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
		
	office_no = input('Enter Officer Number: ')
	while len(office_no) > 15:
		print('Invalid Officer Number Format [too long]')
		office_no = input('Enter Officer Number: ') 
		 
	vtype = input('Enter Violation Type: ')
	while len(vtype) > 10:
		print('Invalid Officer Number Format [too long]')
		vtype = input('Enter Violation Type: ')
		
	vdate = input('Enter Violation Date [ddmmyyyy]: ')
	while len(vdate) > 8:
		print('Invalid Violation Date format')
		vdate = input('Enter Violation Date [ddmmyyyy]: ')
	
	place = input('Enter Violation Place: ')
	while len(place) > 20:
		print('Invalid violation place length')
		place = input('Enter Violation Place: ')
		
	descriptions = input('Enter Violation Description: ')
	while len(descriptions) > 1024:
		print('Invalid description length')
		descriptions = input('Enter Violation Description: ')
	
	vdate = datetime.datetime.strptime(vdate, "%d%m%Y").date()
	
	sqlstr = "INSERT INTO ticket VALUES(:ticket_no, :violator_no, :vehicle_id, :office_no, :vtype, :vdate, :place, :descriptions"
	
	try:
		curs.execute(sqlstr, {'ticket_no':ticket_no, 'violator_no':violator_no, 'vehicle_id':vehicle_id, 'office_no':office_no, 'vtype':vtype, 'vdate':vdate, 'place':place, 'descriptions':descriptions})
		
	except cx_Oracle.DatabaseError as exc:
		error = exc.args[0]
		print( sys.stderr, "Oracle code:", error.code)
		print( sys.stderr, "Oracle message:", error.message)
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

