def main() :
	#user = input("Username [%s]: " % getpass.getuser())
	#if not user:
	#user=getpass.getuser()
	
	## get password
	#pw = getpass.getpass()

	## The URL we are connnecting to 
	#conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
	
	#try:  
	## Establish a connection in Python
	#connection = cx_Oracle.connect(conString)

	##create a cursor 
	#cur = connection.cursor()     
     
	print ("Programs Available:")
	print ("\t1. New Vehicle Registration")
	print ("\t2. Auto Transaction Registration")
	print ("\t3. Driver Licence Registration")
	print ("\t4. Violation Record")
	print ("\t5. Search Engine")
	print ("\t6. Exit")
	while 0 == 0:
		program = input("Choose Program Number: \n\t")
		if program == "1":
			print(1)
		elif program == "2":
			print(2)
		elif program == "3":
			print(3)
		elif program == "4":
			print(4)
		elif program == "5":
			print(5)
		elif program == "6":
			print(6)
			break
		else:
			print ("Invalid Input")
		      
main()