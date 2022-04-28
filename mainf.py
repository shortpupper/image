# want to import base64
import base64
# will need the time so import time
import time


# then make a function that will convert str to byte to base64
def to_base64(string):
 # encode string to utf-8
 string = string.encode('utf-8')
 # then return a converted string to base64
 return base64.b64encode(string)


# make a class that will hold constant vars
class Constant:
 char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789="
 abas = "abcdefghijklmnopqrstuvwxyz"


# then make a functin that takes base64 encoded string and returns a tuple of 3 ints
def to_int_tuples(string):
 # var for testing
 takeinp = "abcdefg"
 # make a for loop that will loop through takeinp and every 4 characters add a & to it
 # split takeinp into a list of strings that split every 4 characters
 charactersList = [takeinp[(x-1)*4:x*4] for x in range(int(len(takeinp)/4))][1:]
 # then have four for loop because there is only going to be four inps at a time
 for xa in []:
  for xb in []:
   for xc in []:
    for xd in []:
     pass

 


