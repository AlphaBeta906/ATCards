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
if test1 != tes:
    print ("TEST WORKS!")
del test1, te, tes


