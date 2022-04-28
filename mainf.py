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
 takeinp = "a"
 # then get the ord of the character
 ordCar = ord(takeinp)-97
 # 

