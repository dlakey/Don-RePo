import sys
import os
#
# User List
usernames = {'Adrian':'12345','John':'GVEST','Richard':'REJ321','Caleb':'875'}
#
# User Input Section
user = input("Please enter your username:")

if user in usernames:
  pword = usernames.get(user)

  password = input("Please enter your password:")

  if password == pword:
    print('Thank You')

  else:
    print('You entered an incorrect password. Please try again.')

else:

   print('You are not a registered user.')

