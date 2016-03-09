
import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it



def main() :
	while True:
		# get usename, defult to current user
		user = input("Username [%s]: " % getpass.getuser())
		if not user:
			user=getpass.getuser()
		
		# get password
		pw = getpass.getpass()
	
		# The URL we are connnecting to 
		conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
		
		try:  
			# Establish a connection
			connection = cx_Oracle.connect(conString)
		except cx_Oracle.DatabaseError as exc:
			# Failed connection
			print ("Invalid Username/Password. \nPlease try again\n")
			continue
		
		print ("Connection Established!")
		break
	
	#create a cursor 
	cur = connection.cursor()     
	while True:
		print ("Main Menu \n")
		print ("Programs Available:")
		print ("\t1. New Vehicle Registration")
		print ("\t2. Auto Transaction Registration")
		print ("\t3. Driver Licence Registration")
		print ("\t4. Violation Record")
		print ("\t5. Search Engine")
		print ("\t6. Exit")
	
		program = input("Choose Program Number: \n\t")
		if program == "1":
			# Call New Vehichle Registrarion
			print(1)
		elif program == "2":
			# Call Auto Transaction Registration
			print(2)
		elif program == "3":
			# Call Driver Licence Registration
			print(3)
		elif program == "4":
			# Call Violatio Record
			print(4)
		elif program == "5":
			# Call Search Engine
			print(5)
		elif program == "6":
			# Quit Program
			print(6)
			break
		else:
			print ("Invalid Input")
	
	cur.close()
	connection.close()	
		      
main()