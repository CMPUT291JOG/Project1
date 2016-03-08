# New Vehichle Registration
# Gemma
# This component is used to register a new vehicle by an auto registration officer.
# By a new vehicle, we mean a vehicle that has not been registered in the database. 
# The component shall allow an officer to enter the detailed information about the
# vehicle and personal information about its new owners, if it is not in the database.
# You may assume that all the information about vehicle types has been loaded in the initial database.

import sys
import cx_oracle

def newVehicleRegistration(cur):
  checkExist()
  
  
  
  def checkExist:
    personExist = input('Does the person registering the vehicle already exist in the database? (y/n)')
    if (personExist == 'y' or 'Y'):
      # vehicle owner already exists, retrieve their table info?
    elif (personExist == 'n'or 'N'):
      # must get person info table
      # sin           CHAR(15),  
      # name          VARCHAR(40),
      # height        number(5,2),
      # weight        number(5,2),
      # eyecolor      VARCHAR (10),
      # haircolor     VARCHAR(10),
      # addr          VARCHAR2(50),
      # gender        CHAR,
      # birthday      DATE,
      # PRIMARY KEY (sin),
      # CHECK ( gender IN ('m', 'f') 
      
      sin = input('Enter Social Insurance number: ')
      while len(sin) > 15:
        print('Invalid SIN input [format XXXXXXXXX]')
        sin = input('Enter Social Insurance number: ')
        
      name = input('Enter registering name: ')
      while len(name) > 15:
        print('Invalid name format [format first last]')
        sin = input('Enter registering name: ')
        
      height = input('Enter registrants height: ')
      while len(height) > 99999.99:
        # first make sure its an int, try except
        # second make sure its < 99999.99
        try: 
          int(height)
        except ValueError: 
          print('Invalid height format [format XXXXX.XX]')
          sin = input('Enter registrants height: ')
          
      weight = input('Enter registrants weight: ')
      while len(weight) > 99999.99:
        # first make sure its an int, try except
        # second make sure its < 99999.99
        try: 
          int(weight)
        except ValueError: 
          print('Invalid weight format [format XXXXX.XX]')
          we = input('Enter registrants weight: ')
          
      eyecolor = input('Enter registrants eye color: ')
      while len(eyecolor) > 10:
        print('Invalid eyecolor format [format XXXXXXXXXX]')
        eyecolor = input('Enter registering eye color: ')
        
      haircolor = input('Enter registrants hair color: ')
      while len(haircolor) > 15:
        print('Invalid hair color format [format XXXXXXXXXX]')
        haircolor = input('Enter registrants hair color: ')
        
      addr = input('Enter registrants address: ')
      while len(addr) > 15:
        print('Invalid address format [format first las]')
        sin = input('Enter registering name: ')
      
    else:
      print( 'Invalid Input, please answer this question again.')
      checkExist()



