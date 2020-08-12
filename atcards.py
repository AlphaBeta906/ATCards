# ATCards 2020
from time import *
from random import *
import sys
import pickle as p
try:
    import requests
    file = requests.get("https://raw.githubusercontent.com/AlphaBeta906/ATCards/master/atcards.py")
    file = bytes(file.text, 'utf-8')
    with open('atcards.py', 'wb') as f:
        f.truncate(0)
        f.write(file)
        f.close()
    del file
except ModuleNotFoundError:
    print ("This game need you to have the requests module")
    print ("Intstall via using 'python -m pip install requests'")
    sys.exit()
print ("ATCards [Version 1.5.18.14]")
print ("(cc) 2020 Alternate Territories Wiki")
playercards = {"Republic of Castile": ["120", "90"], "Kingdom of Leon": ["100", "110"], "Belastan": ["110", "100"], "Duchy of Koelsa": ["90", "100"], "Satlantis": ["80", "90"], "Atlantis": ["90", "90"], "Alphadonia": ["130", "160"], "Googleplus Republic": ["100", "130"], "The New Republic of Assaria": ["70", "90"], "Olderion": ["30", "50"], "PR Asturas": ["150", "160"], "ACTO": ["200", "180"], "DigitalNewia": ["120", "130"], "New Republic of Chrome": ["50", "60"], "Saxony Kingdom": ["120", "100"], "Kingdom of Israel": ["50", "80"], "UCSO": ["200", "170"], "Anti-OK Alliance": ["130", "120"], "4th German Reich": ["70", "90"], "Communist State of Honey": ["70", "80"], "Gyrwhen Republic": ["120", "100"], "Russian Kingdoms": ["130", "150"], "South Asian Federation": ["150", "140"]}
cardinfo = {"Republic of Castile": ["Towering Castile: Increaces ATK and DEF for 5 moves(reacharge 2 moves)"], "Kingdom of Leon": ["Leon Blast: Increase ATK by 50 for one attack(reacharge of 6 moves)"], "Belastan": ["Polish Army: Draw 2 cards"], "Duchy of Koelsa": ["Power Steal: Get 1 card from you're opponent's card"], "Satlantis": ["Altantic Power: If you have Atlantis in you're deck increase ATK to 110 until Atlantis dies"], "Atlantis": ["Altantic Power: If you have Satlantis in you're deck increase ATK to 110 until Satlantis dies"], "Alphadonia": ["Reign of Alpha: Increse DEF and ATK to 200 for 10 moves(used once)", "Tech Master: Draw a card"], "Googleplus Republic": ["Google Allies: If any of the Google Cards(Google Republic, New Republic of Crome, YouTube Federation and Googleplus Republic) is in you're deck, increse ATK to by 40 until card dies"], "The New Republic of Assaria": ["Asserian Power: Increase ATK to 110 for 3 moves"], "PR Asturas": ["Communist Rule: Increase ATK and DEF to 210 for 15 moves(used once)", "Tech Master: Draw a card"], "ACTO": ["Capitalist Power: Increase ATK by 20 to all of you're card's in you're deck"], "New Republic of Chrome": ["Google Allies: If any of the Google Cards(Google Republic, New Republic of Crome, YouTube Federation and Googleplus Republic) is in you're deck, increse ATK to by 40 until card dies"], "Kingdom of Israel": ["Star of David: Increase ATK by 20 for 5 moves(recharge of 10 moves)"], "UCSO": ["Communist Power: Increase ATK by 20 for 10 moves(recrage of 5 moves)"], "Russian Kingdoms": ["Moskow Punch: Increase ATK by 20 for 1 move (recharge of 5 moves)"]}
with open('things.pkl', 'rb') as f:
    currentcards = list(f.read())
with open('money.pkl', 'rb') as f:
    money = str(f.read()).replace("b'", "").replace("'", "")
    money = len(money)
index = 1
common = ["The New Republic of Assaria", "New Republic of Chrome", "Olderion", "Satlantis", "Atlantis", "Kingdom of Israel", "4th German Reich", "Communist State of Honey"]
rare = ["Republic of Castile", "Kingdom of Leon", "Belastan", "DigitalNewia", "Republic of Castile", "Googleplus Republic", "Saxony Kingdom", "Anti-OK Alliance", "Gyrwhen Republic", "Russian Kingdoms", "South Asian Federation"]
ultra = ["Googleplus Republic", "ACTO", "PR Asturas"]
epic = ["UCSO"]
print ("Common - 10 ")
print ("Rare   - 40 ")
print ("Ultra  - 100")
print ("Epic   - 200")
cs = input("> ").lower()
if cs == "common" or "rare" or "ultra" or "epic":
    if cs == "common" and money > 10:
        money -= 10
        for x in range(1, 6):
            print ("====Card " + str(index) + "====")
            card = choice(common)
            print (f"{card}, ATK: {playercards[card][0]} DEF: {playercards[card][1]}")
            sleep(1)
            print ("Special Moves:")
            sleep(1)
            try:
                print ("\n".join(cardinfo[card]))
            except KeyError:
                print ("No special moves")
            enter = input("==PRESS ENTER TO CONTINUE==")
            del enter
            index += 1
            currentcards.append(card)
    elif cs == "rare" and money > 40:
        money -= 40
        for x in range(1, 6):
            print ("====Card " + str(index) + "====")
            card = choice(rare)
            print (f"{card}, ATK: {playercards[card][0]} DEF: {playercards[card][1]}")
            sleep(1)
            print ("Special Moves:")
            sleep(1)
            try:
                print ("\n".join(cardinfo[card]))
            except KeyError:
                print ("No special moves")
            enter = input("==PRESS ENTER TO CONTINUE==")
            del enter
            index += 1
            currentcards.append(card)
    elif cs == "ultra" and money > 100:
        money -= 100
        for x in range(1, 6):
            print ("====Card " + str(index) + "====")
            card = choice(ultra)
            print (f"{card}, ATK: {playercards[card][0]} DEF: {playercards[card][1]}")
            sleep(1)
            print ("Special Moves:")
            sleep(1)
            try:
                print ("\n".join(cardinfo[card]))
            except KeyError:
                print ("No special moves")
            enter = input("==PRESS ENTER TO CONTINUE==")
            index += 1
            currentcards.append(card)
    elif cs == "epic" and money > 200:
        money -= 200
        for x in range(1, 6):
            print ("====Card " + str(index) + "====")
            card = choice(epic)
            print (f"{card}, ATK: {playercards[card][0]} DEF: {playercards[card][1]}")
            sleep(1)
            print ("Special Moves:")
            sleep(1)
            try:
                print ("\n".join(cardinfo[card]))
            except KeyError:
                print ("No special moves")
            enter = input("==PRESS ENTER TO CONTINUE==")
            del enter
            index += 1
            currentcards.append(card)
    else:
        print ("Too expencive to buy",cs,"pack")
else:
    print ("No pack named '" + cs + "'")
sleep(3)
with open('things.pkl', 'wb') as f:
    f.truncate(0)
    p.dump(currentcards, f)
with open('money.pkl', 'wb') as f:
    f.truncate(0)
    p.dump(money, f)
