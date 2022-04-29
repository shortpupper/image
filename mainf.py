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

# function to turn leetters to numbers
def nTL(strings): return [x-47 for x in strings]

def TnL(lists): return [chr(x+47) for x in lists]

# funtion to get a list of four numbers
def fourNumber(lists): return sum([x*63 for x in lists[:-1]])+lists[-1]

# then make a functin that takes base64 encoded string and returns a list of chars in groups of 4
def toFourLists(lists): return [xa for xa in [lists[(x-1)*4:x*4] for x in range(int(len(lists)/2))] if xa != []]

# return the valeus
def valeus(strings): return [fourNumber(x) for x in (toFourLists(nTL(to_base64(strings))))]

print(valeus("yesgdsfas"))
