# Auto Transaction - allows the officer to enter infomaion to complete the transaction
# w.r.t the details of seller, buyer, date and price
######################################
# General
#  s_date      date,
#  price       numeric(9,2),
#  t_id        CHAR(15),
#  seller_id   CHAR(15),
#  buyer_id    CHAR(15),
#  vehicle_id  CHAR(15),
#  officer_id  CHAR(15),
#  PRIMARY KEY (t_id),
#  FOREIGN KEY (seller_id) REFERENCES people(sin),
#  FOREIGN KEY (buyer_id) REFERENCES people(sin),
#  FOREIGN KEY (vehicle_id) REFERENCES vehicle(serial_no),
#  FOREIGN KEY (officer_id) REFERENCES registering_officer(id)
#########################################
# Scenerio
# 1) Add a sale record where buyer does not exist in the database
# a new person should be added after asking appropriate information.
# 2) Add a sale record where seller is not an owner of the vehicle 
# an appropriate error message should be shown.
# 3) Add a sale record where vehicle does not exist in the database
# an appropriate message should be displayed.
# Jen
def trans_main(cur):
     # get buyer id and make sure less than 15 characters
     buyer_id = input ('Enter buyer ID: ')
     while len(buyer_id) > 15:
	  print('Invalid buyer ID.')
	  buyer_id = input ('Enter buyer ID: ')            

     checkBuyer = "SELECT SIN FROM people WHERE SIN = :buyer_id" 
     cur.execute(checkBuyer)   
     rows = cur.fetchall()
     
     # if buyer not exist in database
     if (rows == 0):
	  # add new person  
	  ##TODO
	  transaction_input()
     else:
	  continue
     
     # get seller id and make sure less than 15 characters
     seller_id = input ('Enter seller ID: ')
     while len(seller_id) > 15:
	  print('Invalid seller ID.')
	  seller_id = input ('Enter transaction ID: ')      
          
     # get vehicle id and make sure less than 15 characters
     vehicle_id = input ('Enter vehicle ID: ')
     while len(vehicle_id) > 15:
	  print('Invalid vehicle ID.')
	  vehicle_id = input ('Enter vehicle ID: ') 
	  
     # scenerio 3, check if vehicle in database
     checkVehicle = "SELECT serial_no FROM vehicle WHERE serial_no == :vehicle_id")
     cur.execute(checkVehicle)
     rows = cur.fetchall()
     if rows == 0:
	  addVehicle(vehicle_id)
     else:
	  continue
	  
     # scenerio 2 if seller not owner, error msg
     getOwners = "SELECT owner_id, vehicle_id, serial_no FROM owner, vehicle WHERE serial_no = vehicle_id and owner_id = :seller_id" 
     cur.execute(getOwners)   
     rows = cur.fetchall()
     if rows == 0:
	  print("Error, seller does not match owner")
	  return     
	  
def transaction_input(cur): 
     # create and initialize variables
     try_again = 0
     complete = 1
  
    # assign inputs to variables
    # should check input whether they are valid
  
    # if s_date not valid, prompt proper message
     while complete == 1:    
	  s_date = input ('Enter sale date (ddmmyyyy): ')
	  if len(s_date) != 8:
	       print("Invalid input")
	       continue
	  else: 
	       try: 
		    int(s_date)
	       except ValueError:
		    print("invalid input")
		    continue	  
	  complete = 0    
     # convert to date format
     datetime.datetime.strptime(s_date, "%d%m%Y").date()
  
     # input for price with 2 decimals
     while complete == 1:    
	  try:
	       # get input as a float number
	       price = input (float('Enter price (0.00): '))	
	       # price cannot be less than 0
	       if price < 0:
		    print("Invalid selling price!")
		    continue
	       # pass check if it is a positive number
	       else: 
		    complete = 0
		    # try again if it is not a number
	  except ValueError:
	       print("invalid input")
	       continue
	  # otherwise pass checking 
	  complete = 0  
     
     #convert price from float to two decimals
     price = round(price, 2)
  
     # get transaction id and make sure less than 15 character
     t_id = input ('Enter transaction ID: ')
     while len(t_id) > 15:
	  print('Invalid transaction ID.')
	  t_id = input ('Enter transaction ID: ')
  
	  # get seller id and make sure less than 15 characters
	  seller_id = input ('Enter seller ID: ')
	  while len(seller_id) > 15:
	       print('Invalid seller ID.')
	       selle_id = input ('Enter transaction ID: ') 
  
	  # get buyer id and make sure less than 15 characters
	  buyer_id = input ('Enter buyer ID: ')
	  while len(buyer_id) > 15:
	       print('Invalid buyer ID.')
	       buyer_id = input ('Enter buyer ID: ')        

	  # get vehicle id and make sure less than 15 characters
	  vehicle_id = input ('Enter vehicle ID: ')
	  while len(vehicle_id) > 15:
	       print('Invalid vehicle ID.')
	       vehicle_id = input ('Enter vehicle ID: ')    
  
	  # get vehicle id and make sure less than 15 character    
	  officer_id  = input ('Enter officer ID: ')
	  while len(office_id) > 15:
	       print('Invalid officer ID.')
	       officer_id = input ('Enter officer ID: ')
	      
	  try:
	       cur.execute (sqlStr, {s_date: s_date, price: price, t_id: t_id,
	                             seller_id: seller_id, buyer_id: buyer_id,
	                             vehicle_id: vehicle_id, officer_id: officer_id})
	  except cx_Oracle.DatabaseError as exc:
	       print ("Transaction already in database. \nNo new transaction created.")
	  
	  while True:
	       try_again = input('Would you like to try inputing transaction? (y/n)')
	       if try_again == y:
		    licence_input(cur)
		    return
	       elif try_again == n:
		    return
	       else:
		    print("invalid input")
	      # continue ??
	  
     # if pass everything, print and save input
     print("Input Successfull!")
     return