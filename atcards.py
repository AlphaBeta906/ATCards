# ATCards 2020
from time import *
from random import randint
print ("ATCards 2020")
print ("Version 1.0.3")
playercards = {"Republic of Castile": ["120", "90"], "Kingdom of Leon": ["100", "110"], "Belastan": ["110", "100"], "Duchy of Koelsa": ["90", "100"], "Satlantis": ["80", "90"], "Atlantis": ["90", "90"]}
cardinfo = {"Republic of Castile": ["Towering Castile: Increaces ATK and DEF for 5 moves(reacharge 2 moves)"], "Kingdom of Leon": ["Leon Blast: Increase ATK by 50 for one attack(reacharge of 6 moves)"], "Belastan": ["Polish Army: Draw 2 cards"], "Duchy of Koelsa": ["Power Steal: Get 1 card from you're opponent's card"], "Satlantis": ["Altantic Power: If you have Atlantis in you're deck increase ATK to 110 until Atlantis dies"], "Atlantis": ["Altantic Power: If you have Satlantis in you're deck increase ATK to 110 until Satlantis dies"]}
currentcards = {}
cs = input("> ")
if cs in list(playercards):
    print (f"{cs}, ATK:{playercards[cs][0]} DEF:{playercards[cs][1]}")
    print ("/n".join(cardinfo[cs]))
    
