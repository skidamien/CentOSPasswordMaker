#!/usr/bin/python

#Damien J. Michalosky
#Password maker
#June 18, 2013

# This works for CentOS / RHEL 6

import crypt
import random
import sys

print "passwordmaker.py provides an encrypted /etc/shadow ready password with a random SHA512 salt. This needs to be run in CentOS/RHEL as it is tied to the local crypt"
 
enterred_password = raw_input("Enter desired password: ")

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
salt = ''.join(random.choice(ALPHABET) for i in range(16))

saltstring = '$6$' + salt

print crypt.crypt(enterred_password, saltstring)
