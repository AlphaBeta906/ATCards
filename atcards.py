# ATCards 2020
from time import *
from random import randint
print ("ATCards 2020")
print ("Version 1.0.1")
playercards = {"Republic of Castile": ["120", "90"], "Kingdom of Leon": ["100", "110"]}
cardinfo = {"Republic of Castile": ["Towering Castile: Increaces ATK and DEF for 5 moves(reacharge 2 moves)"], "Kingdom of Leon": ["Leon Blast: Increase ATK by 50 for one attack(reacharge of 6 moves)"]}
currentcards = {}
cs = input("> ")
print (f"{cs}, ATK:{playercards[cs][0]} DEF:{playercards[cs][1]}")
print ("/n".join(cardinfo[cs]))
