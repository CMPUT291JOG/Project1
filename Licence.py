# python3 Licence.py
# File for Project 1
# edited: 03 Mar 2016 by Jen

# Driver Licence Regestration
# - record information needd to issuing a drive licence 
# licence no.CHAR(15), sin CHAR(15), class VARCHAR(10), photo BLOB,
# issuing_date DATE, expiring_date DATE, 
# PRIMARY KEY (licence_no), UNIQUE (sin), FOREIGN KEY (sin) REFERENCES people
# assume image files are stored in a local disk system
# Reference python code from lab files
import sys
import cx_Oracle # the package used for accessing Oracle in Python
import getpass # the package for getting password from user without displaying it

def licence_input(licence_num, sin, licence_class, photo, issuing_date, expiring_date):
  
    # create and initialize variables
    licence_num = ""  	# char
    sin = "" 		# char
    licence_class = ""	# char
    photo = null      	# BLOB - from local disk
    issuing_date = null 	# DATE
    expiring_date = null # Date

    # assign inputs to variables
    # should check input whether they are valid
    # if not valid, prompt proper message
    licence_num = input ('Enter Licence number: ')
    sin = input ('Enter Social insurance number: ')
    licence_class = input ('Enter licence class: ')
    photo = input ('Insert photo ')
    issuing_date = input ('Enter issuing date')
    expiring_date = input ('Enter expiring date ')


    # insert values to the table
    curs.execute("INSERT INTO Licence VALUES(licence_num, sin, lic_class, photo, issuing_date, expiring_date)
    return 
