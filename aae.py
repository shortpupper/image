import os
import re

exps = '<A HREF=".*\.txt"><B>.*</B></A>.*<BR><BR>'
exps2 = "Page numer '..'"

# run
def run():
 # get the path of a file named text.txt then print it
 filename = os.getcwd() + "/scraping/data"
 with open(filename+"/text2.txt", "a") as ft: pass
 with open(filename + "/text.txt") as f:
  for line in f:
   # now check if the text is ok in re 
   re1 = re.compile(exps).match(f, 1)
   re2 = re.compile(exps2).match(f, 1)
   if re1 or re2:
    ft.write()
    



run()