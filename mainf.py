# want to import base64
import base64

# then make a function that will convert str t byte to base64
def to_base64(string):
 # encode string to utf-8
 string = string.encode('utf-8')
 # then return a converted string to base64
 return base64.b64encode(string)

