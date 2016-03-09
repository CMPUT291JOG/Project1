def search (cur):
    while True:
	print ("What to search for?")
	print ("\t1. Driver Info")
	print ("\t2. Violation Records")
	print ("\t3. Vehichle History")
	print ("\t4. Back to Main Menu")
	program = input("Choose Program Number: \n\t")
	if program == "1":
	    drive_search()
	    break
	elif program == "2":
	    violation_search()
	    break
	elif program == "3":
	    history_search()
	    break
	elif program == "4":
	    return
	else:
	    print ("Invalid Input")
	    continue
    
	while True:
	    try_again = input("Do you want to search another? (y/n)")
	    if try_again == y:
		search(cur)
		return
	    elif try_again == n:
		return
	    else:
		print("invalid input")        
	

def drive_search():
    while True:
	print ("What to search by?")
	print ("\t1. Licence Number")
	print ("\t2. Name")
	print ("\t3. Go Back")
	program = input("Choose Program Number: \n\t")
	if program == "1":
	    
	    licence_num = input ('Enter Licence number: ')
	    while len(licence_num) > 15:
		print('Invalid licence number input.')
		licence_num = input ('Enter Licence number: ')
	    
	    curs.execute("SELECT name, licence_no, addr, birthday, class, driving_condition, expiring_date from ")
	    
	    
	    
	    
	    
	elif program == "2":
	    
	    
	elif program == "3":
	    return
	else:
	    print ("Invalid Input")

def violation_search()

def history_search()
