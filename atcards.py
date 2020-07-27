# ATCards 2020
from time import *
from random import *
atco = "All capitalist treaty orginization"
print ("ATCards 2020")
print ("Version 1.0.7")
playercards = {"Republic of Castile": ["120", "90"], "Kingdom of Leon": ["100", "110"], "Belastan": ["110", "100"], "Duchy of Koelsa": ["90", "100"], "Satlantis": ["80", "90"], "Atlantis": ["90", "90"], "Alphadonia": ["130", "160"], "Googleplus Republic": ["100", "130"], "The New Republic of Assaria": ["70", "90"], "Olderion": ["30", "50"], "PR Asturas": ["150", "160"], "All capitalist treaty orginization": ["200", "180"]}
cardinfo = {"Republic of Castile": ["Towering Castile: Increaces ATK and DEF for 5 moves(reacharge 2 moves)"], "Kingdom of Leon": ["Leon Blast: Increase ATK by 50 for one attack(reacharge of 6 moves)"], "Belastan": ["Polish Army: Draw 2 cards"], "Duchy of Koelsa": ["Power Steal: Get 1 card from you're opponent's card"], "Satlantis": ["Altantic Power: If you have Atlantis in you're deck increase ATK to 110 until Atlantis dies"], "Atlantis": ["Altantic Power: If you have Satlantis in you're deck increase ATK to 110 until Satlantis dies"], "Alphadonia": ["Reign of Alpha: Increse DEF and ATK to 200 for 10 moves(used once)", "Tech Master: Draw a card"], "Googleplus Republic": ["Google Allies: If any of the Google Cards(Google Republic, New Republic of Crome, YouTube Federation and Googleplus Republic) is in you're deck, increse ATK to by 40 until card dies"], "The New Republic of Assaria": ["Asserian Power: Increase ATK to 110 for 3 moves"], "PR Asturas": ["Communist Rule: Increase ATK and DEF to 210 for 15 moves(used once)", "Tech Master: Draw a card"], "All capitalist treaty orginization": ["Capitalist Power: Increase ATK by 20 to all of you're card's in you're deck"]}
currentcards = {}
cs = input("> ").capitalize()
if cs == "ACTO" or "All Capitalist Treaty Orginization":
    print (f"ATCO, ATK: {playercards[atco][0]} DEF: {playercards[atco][1]}")
    print ("Special Moves:")
    try:
        print ("\n".join(cardinfo[atco]))
    except KeyError:
        print ("No special moves")
elif cs in list(playercards):
    print (f"{cs}, ATK: {playercards[cs][0]} DEF: {playercards[cs][1]}")
    print ("Special Moves:")
    try:
        print ("\n".join(cardinfo[cs]))
    except KeyError:
        print ("No special moves")
else:
    print ("No card named '" + cs + "'")
