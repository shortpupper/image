# want to import base64
import base64
import os
# will need the time so import time
import time
# need to edit images so import pillow
from PIL import Image
# round numbers better
import math
# needed for things
import requests

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
def outasciis(listg): return b''.join([chr(ord(chr(x))).encode("utf-8") for x in listg])

# functon to take a list and every 3 make it a tuple
def torgd(listg): return [(listg[x], listg[x+1], listg[x+2]) for x in range(0, len(listg), 3)]
def outrgd(listg): return [y for x in listg for y in x]

# function to make it encdoe?
def torun(strings): return torgd(toasciis(mobd(strings)))

# function to decode the list?
def unrun(listg): return outasciis(outrgd(listg))

# function to take a list and add to it to make a image size
def toimage(listg, size): return listg+[(61,)*3 for x in range((size[0]*size[1])-len(listg))]

# function to make a new image from name and size
def newimage(name, size):
 # make a new image
 im = Image.new("RGB", size)
 # now save the image
 im.save(name)

# function to put the data into the image and save it
def putimage(listg, name):
 # open the image
 with Image.open(name) as im:
  # do
  f = [((xa, ya), listg[xa+ya*im.height]) for xa in range(im.width) for ya in range(im.height)]
  # then write the data
  [im.putpixel(v[0], v[1]) for v in f]
  # then save
  im.save(name)

# read an image
def getimagedata(name):
 with Image.open(name) as im: return list(im.getdata())

# then a decode the data and return a string
def readimage(name): return unrun(getimagedata(name))

# make a new image and put data there
def doimage(text, name):
 name = name+".png"
 data1 = torun(text)
 size = (math.ceil(math.sqrt(len(data1))),)*2
 data = toimage(data1, size)
 newimage(name, size)
 putimage(data, name)


# function to read the bemovie script
def reader():
 url = "https://raw.githubusercontent.com/shortpupper/image/master/beemovie.txt"
 # request the data
 r = requests.get(url)
 # then return the text
 return r.text


j = reader()
j =j.upper()

# doimage(j, "bee2")

# print(readimage(os.getcwd()+"/bees.png"))

