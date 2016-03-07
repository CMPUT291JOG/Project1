# MainMenu
# Omar
def licence_main():
  # get username
	user = input("Username [%s]: " % getpass.getuser())
	if not user:
  		user=getpass.getuser()
	
	# get password
	pw = getpass.getpass()

	# The URL we are connnecting to 
	conString=''+user+'/' + pw +'@gwynne.cs.ualberta.ca:1521/CRS'
	
	# SQL statement to execute
	createLicence = ("create table Licence "
	"(T_NAME VARCHAR(32) PRIMARY KEY, SUP_ID INTEGER, PRICE FLOAT, SALES INTEGER, TOTAL INTEGER)")
	"(licence_no. CHAR(15) PRIMARY KEY, sin CHAR(15), class VARCHAR(10), photo BLOB, issuing_date DATE, expiring_date DATE)")
	
	try:  
	  # Establish a connection in Python
	  connection = cx_Oracle.connect(conString)

	  #create a cursor 
	  curs = connection.cursor()
	  
	  # TODO: if licence table null, create licence table
	  # curs.execute(createLicence)
	  #else continue

	  # executing a query to display
	  curs.execute("SELECT * from autoTransaction")
	  # get all data and print it
	  rows = curs.fetchall()
	  for row in rows:
	    print(row)
	
	  # getting metadata
	  rows = curs.description
	  columnCount = len(rows)
  	  # display column names and type
	  # (name, type, display_size,internal_size,precision,scale,null_ok)
  	  for row in rows:
  	    print(row[0]," ",row[1])
  	
  	  # call for input
  	  licence_input()

	  curs.execute("INSERT INTO TOFFEES VALUES(licence_num, sin, lic_class, photo, issuing_date, expiring_date)

if __name__ == "__main__":
    main()
