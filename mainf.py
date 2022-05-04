# want to import base64
import base64
import os
# will need the time so import time
import time
# need to edit images so import pillow
from PIL import Image


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

#print(valeus("-asdfyes"))

# function to test if string is disable by 3
def mobd(strg):
 strgd = strg
 for x in range(4):
  if not len(strgd) % 3: return strgd
  else: strgd += "="

# function that just turn a string to a list of ascii numbers
def toasciis(strg): return [ord(x) for x in strg]
def outasciis(listg): return ''.join([chr(x) for x in listg])

# functon to take a list and every 3 make it a tuple
def torgd(listg): return [(listg[x], listg[x+1], listg[x+2]) for x in range(0, len(listg), 3)]
def outrgd(listg): return [y for x in listg for y in x]

# function to make it encdoe?
def torun(strings): return torgd(toasciis(mobd(strings)))

# function to take a list and add to it to make a image size
def toimage(listg, size): return listg+[(61,)*3 for x in range((size[0]*size[1])-len(listg))]

# function to make a new image from name and size
def newimage(name, size):
 # make a new image
 Image.new("RGB", size)
 # now save the image
 Image.save(name)

# function to put the data into the image and save it
def putimage(listg, name):
 # open the image
 with Image.open(name) as im:
  # then write the data
  im.putdata(listg)
  # then save
  im.save(name)


#r0 = torun("yes food")

text = "I love food yes me and this test"

name = os.getcwd()+"/test1.jpg"

size = (round(len(text) / 2),)*2 # you might have to divide by 3

data = toimage(torun(text), size)




