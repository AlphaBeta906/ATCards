# ATCards 2020
from time import *
from random import *
import pickle as p
print ("ATCards [Version 1.1.10.2]")
print ("(cc) 2020 Alternate Territories Wiki")
playercards = {"Republic of Castile": ["120", "90"], "Kingdom of Leon": ["100", "110"], "Belastan": ["110", "100"], "Duchy of Koelsa": ["90", "100"], "Satlantis": ["80", "90"], "Atlantis": ["90", "90"], "Alphadonia": ["130", "160"], "Googleplus Republic": ["100", "130"], "The New Republic of Assaria": ["70", "90"], "Olderion": ["30", "50"], "PR Asturas": ["150", "160"], "ACTO": ["200", "180"], "DigitalNewia": ["120", "130"], "New Republic of Chrome": ["50", "60"], "Saxony Kingdom": ["120", "100"], "Kingdom of Israel": ["50", "80"], "UCSO": ["200", "170"]}
cardinfo = {"Republic of Castile": ["Towering Castile: Increaces ATK and DEF for 5 moves(reacharge 2 moves)"], "Kingdom of Leon": ["Leon Blast: Increase ATK by 50 for one attack(reacharge of 6 moves)"], "Belastan": ["Polish Army: Draw 2 cards"], "Duchy of Koelsa": ["Power Steal: Get 1 card from you're opponent's card"], "Satlantis": ["Altantic Power: If you have Atlantis in you're deck increase ATK to 110 until Atlantis dies"], "Atlantis": ["Altantic Power: If you have Satlantis in you're deck increase ATK to 110 until Satlantis dies"], "Alphadonia": ["Reign of Alpha: Increse DEF and ATK to 200 for 10 moves(used once)", "Tech Master: Draw a card"], "Googleplus Republic": ["Google Allies: If any of the Google Cards(Google Republic, New Republic of Crome, YouTube Federation and Googleplus Republic) is in you're deck, increse ATK to by 40 until card dies"], "The New Republic of Assaria": ["Asserian Power: Increase ATK to 110 for 3 moves"], "PR Asturas": ["Communist Rule: Increase ATK and DEF to 210 for 15 moves(used once)", "Tech Master: Draw a card"], "ACTO": ["Capitalist Power: Increase ATK by 20 to all of you're card's in you're deck"], "New Republic of Chrome": ["Google Allies: If any of the Google Cards(Google Republic, New Republic of Crome, YouTube Federation and Googleplus Republic) is in you're deck, increse ATK to by 40 until card dies"], "Kingdom of Israel": ["Star of David: Increase ATK by 20 for 5 moves(recharge of 10 moves)"], "UCSO": ["Communist Power: Increase ATK by 20 for 10 moves(recrage of 5 moves)"]}
with open('things.pkl', 'rb') as f:
    currentcards = list(f.read())
with open('money.pkl', 'rb') as f:
    money = str(f.read()).replace("b'", "").replace("'", "")
index = 1
common = ["The New Republic of Assaria", "New Republic of Chrome", "Olderion", "Satlantis", "Atlantis", "Kingdom of Israel"]
rare = ["Republic of Castile", "Kingdom of Leon", "Belastan", "DigitalNewia", "Republic of Castile", "Googleplus Republic", "Saxony Kingdom"]
ultra = ["Googleplus Republic", "ACTO", "PR Asturas"]
epic = ["UCSO"]
print ("common/rare/ultra/epic")
cs = input("> ").lower()
if cs == "common" or "rare" or "ultra" or "epic":
    for x in range(1, 6):
        print ("====Card " + str(index) + "====")
        if cs == "common":
            card = choice(common)
        elif cs == "rare":
            card = choice(rare)
        elif cs == "ultra":
            card = choice(ultra)
        else:
            card = choice(epic)
        print (f"{card}, ATK: {playercards[card][0]} DEF: {playercards[card][1]}")
        sleep(1)
        print ("Special Moves:")
        sleep(1)
        try:
            print ("\n".join(cardinfo[card]))
        except KeyError:
            print ("No special moves")
        enter = input()
        index += 1
        currentcards.append(card)
else:
    print ("No pack named '" + cs + "'")
sleep(3)
with open('things.pkl', 'wb') as f:
    p.dump(currentcards, f)
with open('money.pkl', 'wb') as f:
    p.dump(money, f)
