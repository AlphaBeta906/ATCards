# ATCards 2020
from time import *
from random import randint
import requests
print ("ATCards 2020")
print ("Version 1.0.0")
test1 = requests.get("https://raw.githubusercontent.com/AlphaBeta906/ATCards/master/atcards.py")
test1 = test1.text
te = open("atcards.py", "r")
tes = te.read()
if test1 == tes:
    print ("Its ok its same")
else:
    print ("Uh oh, the file has been updated. Wait five minuites if it says this again get it updated.")
del test1, te, tes


