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

def violation_input(cur):
  try_again = 0
  try: 
    ticket_no = input('Enter Ticket Number: ')
    try: 
      int(ticket_no)
    except ValueError:
      print('Invalid Ticket Number format [Must be Integer]')
      ticket_no = input('Enter Ticket Number: ')
      
    violator_no = input('Enter Violator Number: ')
    while len(violator_no) > 15:
      print('Invalid Violator Number Format [too long]')
      violator_no = input('Enter Violator Number: ')
    # Making sure Violator_no is a valid SIN number thats already existant
    valid_people = 'SELECT sin FROM people WHERE sin = :violator_no
    cur.execute(valid_people, {'sin', sin})
    valid_people = cur.fetchall()
    while valid_people == 0:
    	# sin match not found
    	print('Violator Number doesnt exist, try again [must be registered sin number]')
    	violator_no = input('Enter Violator Number: ')
    	valid_people = 'SELECT sin FROM people WHERE sin = :violator_no
    	cur.execute(valid_people, {'sin', sin})
    	valid_people = cur.fetchall()
        
        
        """ FOR REFERENCE
  sin = input('Enter the SIN of the vehicles primary owner: ')
    # assuming execute field operates like string formatting
    sins = 'SELECT sin FROM people WHERE sin = :sin'
    cur.execute(sins,{'sin':sin})
    sins = cur.fetchall()
    
   """
      
    vehicle_id = input('Enter Vehicle Identification: ')
    while len(vehicle_id) > 15:
      print('Invalid Vehicle Id Format [too long]')
      vehicle_id = input('Enter Vehicle Identification: ')
    # making sure vehicle id is extant serial no
    serials = 'SELECT serial_no FROM vehicle WHERE serial_no = :vehicle_id'
    cur.execute(serials, {'serial no', serial_no}
    serials = cur.fetchall()
    while serials == 0:
  	print('Vehicle ID Number doesnt exist, try again [must be registered serial number]')
  	vehicle_id = input('Enter vehicle ID: ')
	serials = 'SELECT serial_no FROM vehicle WHERE serial_no = :vehicle_id'
    	cur.execute(serials, {'serial no', serial_no}
    	serials = cur.fetchall()
     
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
    
    curs.execute("INSERT INTO ticket VALUES(ticket_no, violator_no, vehicle_id, office_no, vtype, vdate, place, descriptions))
   except cx_Oracle.DatabaseError as exc:
	  error = exc.args
	  print( sys.stderr, "Oracle code:", error.code)
	  print( sys.stderr, "Oracle message:", error.message)
	  while try_again == 0:
	    try_again = input('Would you like to try input again? (y/n)')
	    if try_again == y:
		    violation_input(cur)
	    elif try_again == n:
		    return
	    else:
		    print("invalid input")
		    try_again = 0

