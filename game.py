import sys, time, random

lives = 3
Pname = input ("Welcome. What is your name?:  ")
while lives > 0:
    play = 0

    finial = False


    ##Starting stats##
    G = 0
    HP = 10
    AC = 1

        
    ##Monster one time only start#
    roadM = 0
    trailM = 0
    caveM = 0
    deepM = 0
    lpassM = 0
    rpassM = 0
    mainroomM = 0
    bossM = 0


    ##starting atack mod##
    AcB = 0


    ##Drop start##
    drop = (" ")
    droploc = (" ")


    ##Start inv##
    i1 = ("<empty>")
    i2 = ("<empty>")
    i3 = ("<empty>")
    i4 = ("<empty>")
    wp = ("<empty>")


    ##start storage##
    h1 = ("<empty>")
    h2 = ("<empty>")
    h3 = ("<empty>")
    h4 = ("<empty>")


    ##start spell##
    locC = ("house")
    spell = False


    ##start lock state##
    lock = True


    ##weapon attack mods##
    Ax = 2
    Sw = 4
    Bs = 6
    Cm = 8
    Ms = 999


    ##Hill items##
    hillW = False
    msW = False


    ##house items##
    HouseG = False
    HouseF = False
    sleepC = 5


    ##woods items##
    woodedgG = False
    woodedgK = False


    #passage item##
    passG = False
    passSw = False


    ##dungeon entrance##
    dragq = False


    ##passages' items##
    lpassG = False


    ##Main room items##
    mainroomSw = False


    ##Random vars##
    hold = (" ")


    #code to test for dev mode
    if Pname == "Dl213" or  Pname == ("Kuro"):
        if Pname == ("Kuro"):
             print ("Hi, random person whose name is " + Pname + ". To give you some context, " + Pname + " was is my random friend who puts up with testing my crap games. So have fun as a developer. In the house you can use the command 'dvtp' to go to any location in the game but the names aren't always the same as the actual names. Have fun!")
        print ("Welcome Developer")
        devmode = True
        lock = False
        AC = 500
        spell = True
        play = 1
        G = 50
        loc = input ("What location?:  ")


    #code for starting the game
    while play == 0:
        if Pname != ("Dl213"):
            devmode = False
            print (" ")
            start = input ("Greetings " + Pname + ". Welcome to the wonderful world of Derf's poorly working text-only game. Please do not use capital letters. To open your inventory, type openinv. Remember, if you find an item, you have to pick it up. Are you ready to start?:  ")
            loc = ("fto")
        if start == ("yes") or start == ("y"):
            play = 1
            continue
        elif start == ("no"):
            time.sleep(1)
            print ("well, FINE! Don't play then!")
            exit()
        else:
            print ("Please say yes or no")


    #start of play loop
    while play == 1:
        if HP <= 0:
            lives -= 1
            print (" ")
            print (" ")
            print (" ")
            print ("YOU DIED!")
            print (" ")
            print (" ")
            print (" ")
            time.sleep(0.5)
            if lives > 0:
                input("Press enter to restart")
            play = 0
            continue


        ##Inventory code##
        while loc == ("inv"):
            time.sleep(0.5)
            print ("Items: " + i1 + i2 + i3 + i4 + "  Weapon: " + wp +"  Gold: " + str(G) + "  HP: " + str(HP) + "/20  Lives: " + str(lives))
            invact = input ("Would you like to: eat, equip, drop, go back?:  ")
            if invact == ("eat"):
                if i1 == ("<food>"):
                    HP += 5
                    i1 = ("<empty>")
                    print ("You ate the food. You gain 5 HP!")
                elif i2 == ("<food>"):
                    HP += 5
                    i2 = ("<empty>")
                    print ("You ate the food. You gain 5 HP!")
                elif i3 == ("<food>"):
                    HP += 5
                    i3 = ("<empty>")
                    print ("You ate the food. You gain 5 HP!")
                elif i4 == ("<food>"):
                    HP += 5
                    i4 = ("<empty>")
                    print ("You ate the food. You gain 5 HP!")
                else:
                    print ("You don't have any food.")
            elif invact == ("equip"):
                eqs = input ("Slot 1, 2, 3, 4 or cancel:  ")
                if eqs == ("1"):
                    if i1 == ("<axe>") or i1 == ("<sword>") or i1 == ("<broadsword>") or i1 == ("<claymore>") or i1 == ("<Master Sword>"):
                        hold = wp
                        wp = i1
                        i1 = hold
                        hold = (" ")
                    else:
                        print ("That is not a weapon.")
                elif eqs == ("2"):
                    if i2 == ("<axe>") or i2 == ("<sword>") or i2 == ("<broadsword>") or i2 == ("<claymore>") or i2 == ("<Master Sword>"):
                        hold = wp
                        wp = i2
                        i2 = hold
                        hold = (" ")
                    else:
                        print ("that is not a weapon.")
                elif eqs == ("3"):
                    if i3 == ("<axe>") or i3 == ("<sword>") or i3 == ("<broadsword>") or i3 == ("<claymore>") or i3 == ("<Master Sword>"):
                        hold = wp
                        wp = i3
                        i3 = hold
                        hold = (" ")
                    else:
                        print ("that is not a weapon.")
                elif eqs == ("4"):
                    if i4 == ("<axe>") or i4 == ("<sword>") or i4 == ("<broadsword>") or i4 == ("<claymore>") or i4 == ("<Master Sword>"):
                        hold = wp
                        wp = i4
                        i4 = hold
                        hold = (" ")
                    else:
                        print ("that is not a weapon.")
                elif eqs == ("cancel") or eqs == ("back"):
                    print ("OK, it's canceled")
                    loc = ("inv")
                else:
                    print ("You cannot do that here.")
            elif invact == ("drop"):
                if drop != (" "):
                    print ("You should not drop more than one item.")
                    loc = ("inv")
                dropS = input ("Slot 1, 2, 3, 4, or cancel?:  ")
                if dropS == ("1"):
                    drop = i1
                    droploc = locb
                    i1 = ("<empty>")
                elif dropS == ("2"):
                    drop = i2
                    droploc = locb
                    i2 = ("<empty>")
                elif dropS == ("3"):
                    drop = i3
                    droploc = locb
                    i3 = ("<empty>")
                elif dropS == ("4"):
                    drop = i4
                    droploc = locb
                    i4 = ("<empty>")
                elif dropS == ("cancel") or dropS == ("back"):
                    print ("OK, it's canceled")
                    loc = ("inv")
                else:
                    ("That is not an option.")
            elif invact == ("back") or invact == ("go back"):
                loc = locb
            elif invact == ("hp") and devmode == True:
                ask = input ("How much?:  ")
                HP += ask
            elif invact == ("1") and devmode == True:
                give = input (":")
                i1 = ("<" + give + ">")
            elif invact == ("2") and devmode == True:
                give = input (":")
                i2 = ("<" + give + ">")
            elif invact == ("3") and devmode == True:
                give = input (":")
                i3 = ("<" + give + ">")
            elif invact == ("4") and devmode == True:
                give = input (":")
                i4 = ("<" + give + ">")
            else:
                print ("you can " + invact + " in your inventory")
            if wp != ("<empty>"):
                if wp == ("<axe>"):
                    AcB = Ax
                if wp == ("<sword>"):
                    AcB = Sw
                if wp == ("<broadsword>"):
                    AcB = Bs
                if wp == ("<claymore>"):
                    AcB = Cm
                if wp == ("<Master Sword>"):
                    AcB = Ms


        ##Combate code##
        while loc == ("comb"):
            if HP > 20:
                HP = 20
            print ("A " + Mtype + " attacks you!")
            while dead == False:
                if HP <= 0:
                    dead = True
                    loc =(" ")
                    continue
                print (" ")
                print (Mtype + ": " + str(Mhp) + "  Your HP: " + str(HP))
                act = input ("Attack or defend?:  ")
                Mact = random.randint(1,4)
                crit = random.randint(1,4)

                if act == ("attack") or act == ("a"):
                    if Mact == 1 or Mact == 2:
                       if crit == 4:
                           time.sleep(0.5)
                           print ("Critical hit! You deal " + str(((AC + AcB) *2)) + " damage!")
                           Mhp -= ((AC + AcB) *2)
                           time.sleep(0.5)
                           HP -= Mac
                           print ("The " + Mtype + " attacks you! You lose " + str(Mac) + "HP!")
                           time.sleep(0.5)
                       else:
                            time.sleep(0.5)
                            print ("You attack! You deal " + str((AC + AcB)) + " damage!")
                            Mhp -= (AC + AcB)
                            time.sleep(0.5)
                            HP -= Mac
                            print ("The " + Mtype + " attacks you! You lose " + str(Mac) + " HP!")
                            time.sleep(0.5)
                    else:
                        if crit == 4:
                           time.sleep(0.5)
                           print ("Critical hit! You deal " + str((AC + AcB)) + " damage!")
                           Mhp -= ((AC + AcB))
                           time.sleep(0.5)
                        else:
                            time.sleep(0.5)
                            print ("You attack! You deal " + str(((AC + AcB) / 2)) + " damage!")
                            Mhp -= ((AC + AcB) / 2)
                            time.sleep(0.5)
                if act == ("defend") or act == ("d"):
                    if Mact == 2 or Mact == 1:
                        time.sleep(0.5)
                        HP -= (Mac / 2)
                        print ("The " + Mtype + " Attacks! You take " + str((Mac / 2)) + " damage!")
                        time.sleep(0.5)
                    else:
                        print ("No one attacked.")
                        time.sleep(0.5)
                if Mhp <= 0:
                    print ("You won! You got " + str(mG) + " gold!")
                    G += mG
                    time.sleep(1)
                    dead = True
                    loc = locb


        ##Hill first time only code##
        while loc == ("fto"):
            print (" ")
            print ("You wake up on top of a hill with a small house on top and a forest nearby.")
            time.sleep(0.5)
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("enter the house") or act == ("go to the house") or act == ("go into the house") or act == ("enter house") or act == ("go to house") or act == ("go into house"):
                loc = ("house")
            elif act == ("go to forest") or act == ("go into the forest") or act == ("enter the forest"):
                loc = ("woodedg")
            elif act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif act == ("pray") and msW == False:
                msW = True
                print ("You hear a voice booming down from above. 'GO FORTH CHAMPION, AND DESTROY THE MINITOR USING THE BLADE OF EVIL'S BANE!")
                if i1 == ("<empty>"):
                    i1 = ("<Master Sword>")
                elif i2 == ("<empty>"):
                    i2 = ("<Master Sword>")
                elif i3 == ("<empty>"):
                    i3 = ("<Master Sword>")
                elif i4 == ("<empty>"):
                    i4 = ("<Master Sword>")
                print ("You got the master sword!")
                time.sleep(1)
                problemq = input ("yes i'm ripping off Legend of Zelda. Do you have a problem with that?:  ")
                if problemq == ("yes") or problemq == ("y"):
                    print ("well its my game so....")
                    time.sleep(1)
                    HP = -10000
                    loc = (" ")
                    continue
                else:
                    print ("good")
            elif act == ("search") or act == ("look around"):
                print ("You find an axe behind the house.")
            elif act == ("get axe") or act == ("take axe"):
                if hillW != True:
                    if i1 == ("<empty>"):
                        i1 = ("<axe>")
                        hillW = True
                    elif i2 == ("<empty>"):
                        i2 = ("<axe>")
                        hillW = True
                    elif i3 == ("<empty>"):
                        i3 = ("<axe>")
                        hillW = True
                    elif i4 == ("<empty>"):
                        i4 = ("<axe>")
                        hillW = True
                    else:
                        print ("Your inventory is full.")
                else:
                    print ("You already got the axe, or did you think I forgot to make it so you could not get items more that once?")
            elif droploc == loc and drop != (" ") and act == ("take drop") :
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            else:
                print ("You can't " + act + " here.")


        ##Normal hill code##
        while loc == ("hill"):
            print (" ")
            print ("You are on top of a hill with a small house on top and a forest nearby.")
            time.sleep(0.5)
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("enter the house") or act == ("go to the house") or act == ("go into the house") or act == ("enter house") or act == ("go to house") or act == ("go into house"):
                loc = ("house")
            elif act == ("go to the forest") or act == ("go into the forest") or act == ("enter the forest"):
                loc = ("woodedg")
            elif spell == True and act == ("fkxr"):
                locC = loc
                loc = ("home")
            elif act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif act == ("search") or act == ("look around"):
                print ("You find an axe behind the house.")
            elif act == ("get axe") or act == ("take axe"):
                if hillW != True:
                    if i1 == ("<empty>"):
                        i1 = ("<axe>")
                        hillW = True
                    elif i2 == ("<empty>"):
                        i2 = ("<axe>")
                        hillW = True
                    elif i3 == ("<empty>"):
                        i3 = ("<axe>")
                        hillW = True
                    elif i4 == ("<empty>"):
                        i4 = ("<axe>")
                        hillW = True
                    else:
                        print ("Your inventory is full.")
                else:
                    print ("You already got the axe, or did you think I forgot to make it so you could not get items more that once?")
            elif act == ("enter the forest") or act == ("go to the forest") or act == ("go into the forest") or act == ("enter forest") or act == ("go to forest") or act == ("go into forest"):
                loc = ("woodedg")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            else:
                print ("You can't " + act + " here.")


        ##House code##
        while loc == ("house"):
            print (" ")
            print ("you are in a small house. There is a bed in the corner")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            time.sleep(0.5)
            act = input ("What would you like to do?:  ")
            if act == ("look around") or act == ("search"):
                print ("you find a box under the bed with 2 Gold inside. You also find some food in the kitchen.")
            elif act == ("take gold") or act == ("get gold"):
                if HouseG !=True:
                    print ("You got 2 Gold!")
                    G += 2
                    HouseG = True
                else:
                    print ("You already got the gold, or did you think I forgot to make it so you could not get items more that once?")
            elif spell == True and act == ("fkxr"):
                locC = loc
                loc = ("home")
            elif act == ("take food") or act == ("get food"):
                if HouseF != True:
                    if i1 == ("<empty>"):
                        i1 = ("<food>")
                        HouseF = True
                    elif i2 == ("<empty>"):
                        i2 = ("<food>")
                        HouseF = True
                    elif i3 == ("<empty>"):
                        i3 = ("<food>")
                        HouseF = True
                    elif i4 == ("<empty>"):
                        i4 = ("<food>")
                        HouseF = True
                    else:
                        print ("Your inventory is full.")
                else:
                    print ("You already got the food, or did you think I forgot to make it so you could not get items more that once?")
            elif act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif spell == True and act == ("fkxr"):
                locC = loc
                loc = ("home")
            elif act == ("leave") or act == ("exit") or act == ("back"):
                loc = ("hill")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("sleep"):
                if sleepC > 0:
                    sleepC -= 1
                    print ("You slept and got some health!")
                    HP += 3
                else:
                    print ("You are not tired.")
            else:
               print ("You can't " + act + " here.")


        ##forest edge code##
        while loc == ("woodedg"):
            print (" ")
            time.sleep(0.5)
            print ("You are at the edge of the forest. There is a hill behind you. You see a town nearby. There is also a small, dark trail that also leads deeper into the woods.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif spell == True and act == ("fkxr"):
                locC = loc
                loc = ("home")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("search") or act == ("look around"):
                print ("You find a key and 3 gold trampled into the the dirt")
            elif act == ("get key") or act == ("take key"):
                if woodedgK != True:
                    if i1 == ("<empty>"):
                            i1 = ("<key>")
                            woodedgK = True
                    elif i2 == ("<empty>"):
                        i2 = ("<key>")
                        woodedgK = True
                    elif i3 == ("<empty>"):
                        i3 = ("<key>")
                        woodedgK = True
                    elif i4 == ("<empty>"):
                        i4 = ("<key>")
                        woodedgK = True
                    else:
                        print ("Your inventory is full.")
                else:
                    print ("You already got the key, or did you think I forgot to make it so you could not get items more that once?")
            elif act == ("get gold") or act == ("take gold"):
                if woodedgG != True:
                    G += 3
                    woodedgG = True
                    print ("You got 3 gold!")
                else:
                    print ("You already got the gold.")
            elif act == ("go to town"):
                loc = ("town")
            elif act == ("take trail") or act == ("go to trail"):
                loc = ("trail")
            elif act == ("go to hill"):
                loc ("hill")
            else:
               print ("You can't " + act + " here.")


        ##Town code##
        while loc == ("town"):
            roadM += 1
            if roadM == 1:
                print ("While walking to the town, you hear a russeling in the bushes!")
                Mtype = ("goblin")
                Mhp = 5
                Mac = 1
                mG = 2
                dead = False
                locb = loc
                loc = ("comb")
                continue
            print (" ")
            print ("You are in the middle of a small town. There is a forest a short way from the town. There is a shop here. You also see a house with a sign reading : " + Pname + "'s house.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif spell == True and act == ("fkxr"):
                locC = loc
                loc = ("home")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("go to shop") or act == ("enter shop"):
                loc = ("shop")
            elif act == ("go to home") or act == ("enter home") or act == ("go home") or act == ("go to house"):
                if i1 == ("<key>") or i2 == ("<key>") or i3 == ("<key>") or i4 == ("<key>") or lock == False:
                    print ("You used the key to unlock the door.")
                    if i1 == ("<key>"):
                        i1 = ("<empty>")
                    elif i2 == ("<key>"):
                        i2 = ("<empty>")
                    elif i3 == ("<key>"):
                        i3 = ("<empty>")
                    elif i4 == ("<key>"):
                        i4 = ("<empty>")
                    lock = False
                    loc = ("home")
                else:
                    print ("It's locked")
            elif act == ("go to forest") or act == ("got to woods"):
                loc = ("woodedg")
            else:
                print ("You can't " + act + " here.")


        ##Player's home code##
        while loc == ("home"):
            print (" ")
            print ("You are home! There is a bed in the corner and a storage chest against the far wall")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("sleep"):
                print ("you slept and regained some health.")
                HP += 10
            elif act == ("dvtp") and devmode == True:
                loc = input ("what loc: ")
                continue
            elif act == ("look around") or act == ("search"):
                print ("You find a note under the bed reading: REMEMBER TELEPORT SPELL: fkxr")
                spell = True
            elif act == ("fkxr"):
                loc = locC
                locC = (" ")
            elif act == ("leave") or act == ("go back"):
                loc = ("town")
            elif act == ("open chest") or act == ("store"):
                print ("Your items: " + i1 + i2 + i3 + i4)
                print ("Stored items: " + h1 + h2 + h3 + h4)
                slot = input ("What would you like to store: 1, 2, 3, 4")
                if slot == ("1"):
                    hold = i1
                    inslot = input ("Store in what slot?: 1, 2, 3, 4")
                    if inslot == ("1"):
                        i1 = h1
                        h1 = hold
                        hold = (" ")
                    elif inslot == ("2"):
                        i1 = h2
                        h2 = hold
                        hold = (" ")
                    elif inslot == ("3"):
                        i1 = h3
                        h3 = hold
                        hold = (" ")
                    elif inslot == ("4"):
                        i1 = h4
                        h4 = hold
                        hold = (" ")
                elif slot == ("2"):
                    hold = i2
                    inslot = input ("Store in what slot?: 1, 2, 3, 4")
                    if inslot == ("1"):
                        i2 = h1
                        h1 = hold
                        hold = (" ")
                    elif inslot == ("2"):
                        i2 = h2
                        h2 = hold
                        hold = (" ")
                    elif inslot == ("3"):
                        i2 = h3
                        h3 = hold
                        hold = (" ")
                    elif inslot == ("4"):
                        i2 = h4
                        h4 = hold
                        hold = (" ")
                elif slot == ("3"):
                    hold = i3
                    inslot = input ("Store in what slot?: 1, 2, 3, 4")
                    if inslot == ("1"):
                        i3 = h1
                        h1 = hold
                        hold = (" ")
                    elif inslot == ("2"):
                        i3 = h2
                        h2 = hold
                        hold = (" ")
                    elif inslot == ("3"):
                        i3 = h3
                        h3 = hold
                        hold = (" ")
                    elif inslot == ("4"):
                        i3 = h4
                        h4 = hold
                        hold = (" ")
                elif slot == ("4"):
                    hold = i4
                    inslot = input ("Store in what slot?: 1, 2, 3, 4")
                    if inslot == ("1"):
                        i4 = h1
                        h1 = hold
                        hold = (" ")
                    elif inslot == ("2"):
                        i4 = h2
                        h2 = hold
                        hold = (" ")
                    elif inslot == ("3"):
                        i4 = h3
                        h3 = hold
                        hold = (" ")
                    elif inslot == ("4"):
                        i4 = h4
                        h4 = hold
                        hold = (" ")
            else:
                print ("You can't " + act + " here.")


        ##Shop code##
        while loc == ("shop"):
            act = input ("Welcome to the shop! You have " + str(G) + " gold. What would you like to buy? We currently have food, A sword, a broadsword, and a claymore.:  ")
            if act == ("buy food") or act == ("food"):
                if G <= 1:
                    print ("Sorry, you don't have enough gold.")
                else:
                    buyq = input ("That costs 1 gold. Would you like to buy it?:  ")
                    if buyq == ("yes") or buyq == ("y"):
                        print ("OK, here you go.")
                        G -= 1
                        if i1 == ("<empty>"):
                            i1 = ("<food>")
                        elif i2 == ("<empty>"):
                            i2 = ("<food>")
                        elif i3 == ("<empty>"):
                            i3 = ("<food>")
                        elif i4 == ("<empty>"):
                            i4 = ("<food>")
                        else:
                            print ("Your inventory is full. Here is your money back.")
                            G += 1
                    else:
                        print ("Ok then")
            elif act == ("buy sword") or act == ("sword"):
                if G <= 10:
                    print ("Sorry, you don't have enough gold.")
                else:
                    buyq = input ("That costs 10 gold. Would you like to buy it?:  ")
                    if buyq == ("yes") or buyq == ("y"):
                        print ("Ok, here you go.")
                        G -= 10
                        if i1 == ("<empty>"):
                            i1 = ("<sword>")
                        elif i2 == ("<empty>"):
                            i2 = ("<sword>")
                        elif i3 == ("<empty>"):
                            i3 = ("<sowrd>")
                        elif i4 == ("<empty>"):
                            i4 = ("<sword>")
                        else:
                            print ("Your inventory is full. Here is your money back.")
                            G += 10
            elif act == ("buy broadsword") or act == ("broadsword"):
                if G <= 15:
                    print ("Sorry, you don't have enough gold.")
                else:
                    buyq = input ("That costs 15 gold. Would you like to buy it?:  ")
                    if buyq == ("yes") or buyq == ("y"):
                        print ("OK, here you go.")
                        G -= 15
                        if i1 == ("<empty>"):
                            i1 = ("<broadsword>")
                        elif i2 == ("<empty>"):
                            i2 = ("<broadsword>")
                        elif i3 == ("<empty>"):
                            i3 = ("<broadsword>")
                        elif i4 == ("<empty>"):
                            i4 = ("<broadsword>")
                        else:
                            print ("Your inventory is full. Here is your money back.")
                            G += 15
            elif act == ("buy claymore") or act == ("claymore"):
                if G <= 20:
                    print ("Sorry, you don't have enough gold.")
                else:
                    buyq = input ("That costs 20 gold. Would you like to buy it?:  ")
                    if buyq == ("yes") or buyq == ("y"):
                        print ("OK, here you go.")
                        G -= 20
                        if i1 == ("<empty>"):
                            i1 = ("<claymore>")
                        elif i2 == ("<empty>"):
                            i2 = ("<claymore>")
                        elif i3 == ("<empty>"):
                            i3 = ("<claymore>")
                        elif i4 == ("<empty>"):
                            i4 = ("<claymore>")
                        else:
                            print ("Your inventory is full. Here is your money back.")
                            G += 20
            elif act == ("leave") or act == ("go back") or act == ("back"):
                loc = ("town")


        ##Trail code##
        while loc == ("trail"):
            trailM += 1
            if trailM == 1:
                Mtype = ("Goblin")
                Mhp = 5
                Mac = 1
                mG = 2
                dead = False
                locb = loc
                loc = ("comb")
                continue
            print (" ")
            print ("You are on a dark trial. You can see the edge of the woods, and a dark, damp cave further in.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("look around") or act == ("search"):
                print ("It's too dark to find anything but and old skull")
            elif act == ("go to forest"):
                loc = ("woodedg")
            elif act == ("go to cave"):
                loc = ("cave")
            else:
                print ("You can't " + act + " here!")


        ##Cave code##
        while loc == ("cave"):
            caveM += 1
            if caveM == 1:
                Mtype = ("Goblin Boss")
                Mhp = 10
                Mac = 2
                mG = 5
                dead = False
                locb = loc
                loc = ("comb")
                continue
            print (" ")
            print ("You are in a cave. There are torches on the wall. The entrance is a little way up but the cave goes deeper.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("look around") or act == ("search"):
                print ("You find a secret passage behind a fake wall!")
            elif act == ("go to secret passage") or act == ("go to passage"):
                loc = ("passage")
            elif act == ("go deeper") or act == ("keep going"):
                loc = ("deepcave")
            elif act == ("leave") or act == ("go to trail"):
                loc = ("trail")
            else:
                print ("You can't " + act + " here!")


        ##Secret passage code##
        while loc == ("passage"):
            print (" ")
            print ("There is a small room with a few weapon racks, and big bags everywhere. The staircase leeds back up to the cave.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("look around") or act == ("search"):
                print ("You find 6 gold and a sword!")
            elif act == ("take sword") or act == ("get sword"):
                if passSw == False:
                    if i1 == ("<empty>"):
                        i1 = ("<sword>")
                        passSw = True
                    elif i2 == ("<empty>"):
                        i2 = ("<sword>")
                        passSw = True
                    elif i3 == ("<empty>"):
                        i3 = ("<sword>")
                        passSw = True
                    elif i4 == ("<empty>"):
                        i4 = ("<sword>")
                        passSw = True
                    else:
                       print ("Your inventory is full.")
                else:
                    print ("you already got the sword!")
            elif act == ("take gold") or act == ("get gold"):
                if passG == False:
                    G += 6
                    print ("You got 6 gold!")
                    passG = True
                else:
                    print ("You already got the gold!")
            elif act == ("go back") or act == ("go up") or act == ("go to cave"):
                loc = ("cave")
            else:
                print ("You can't " + act + " here!")


        ##Deep cave code##
        while loc == ("deepcave"):
            deepM += 1
            print (" ")
            print ("There is a huge stone door embedded in the cave wall. You feel a slight breeze coming from up the cave")
            if deepM == 1:
                Mtype = ("Jelly Blob")
                Mhp = 1
                Mac = 0
                mG = 1
                dead = False
                locb = loc
                loc = ("comb")
                continue
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("go up") or act == ("leave") or act == ("go to cave"):
                loc = ("cave")
            elif act == ("go to door") or act == ("enter"):
                loc = ("enterdun")
            elif act == ("search") or act == ("look around"):
                print ("You don't find anything")
            else:
                print ("You can't " + act + " here!")


        ##dungeon entrance code##
        while loc == ("enterdun"):
            while dragq == False:
                print ("there is a dragon standing here!")
                act = input ("What the heck will you do?!?!:  ")
                if act == ("run"):
                    loc = ("deepcave")
                elif act == ("kill it") or act == ("kill"):
                    act2 = input ("Well, your sword can't get through its scales, so do you intend to kill it with your bare hands?:  ")
                    if act2 == ("yes") or act2 == ("y"):
                        print ("I can't believe it, but you kill the dragon.")
                        time.sleep(0.75)
                        print ("With your bare hands.")
                        time.sleep(0.5)
                        print ("How?!?")
                        time.sleep(0.5)
                        dragq = True
                        continue
                    else:
                        print ("ok")
                else:
                    print ("That won't work")
            print (" ")
            print ("You are in a large marble room. Two passages lead left and right")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("search") or act == ("look around"):
                print ("You find nothing but old bones")
            elif act == ("go left") or act == ("left") or act == ("l"):
                loc = ("lpass")
            elif act == ("go right") or act == ("right") or act == ("r"):
                loc = ("rpass")
            elif act == ("die"):
                print ("You stab yourself with a dragon fang")
                HP -= 10000000000
                loc = (" ")
                continue
            elif act == ("go back") or act == ("leave"):
                loc = ("deepcave")
            else:
                print ("You can't " + act + " here!")


        #Left passageway code
        while loc == ("lpass"):
            print (" ")
            lpassM += 1
            if lpassM == 1:
                Mtype = ("goblin")
                Mhp = 5
                Mac = 1
                mG = 2
                dead = False
                locb = loc
                loc = ("comb")
                continue
            print (" ")
            print ("You are in a hallway that continues  right, around a corner. There is a large marble room behind you.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("search") or act == ("look around"):
                   print ("you find 20 gold behind a pillar!")
            elif act == ("take gold") or act == ("get gold"):
                if lpassG != True:
                    G += 20
                    lpassG = True
                    print ("you got 20 gold!")
                else:
                    print ("you already got the gold")
            elif act == ("continue") or act == ("go right") or act == ("keep going"):
                loc = ("mainroom")
            elif act == ("go to marble room") or act == ("go to room") or act == ("go back"):
                loc = ("enterdun")
            else:
                print ("You can't " + act + " here!")


        #Right passageway code
        while loc == ("rpass"):
            print (" ")
            print ("You are in a hallway that continuse left, around a corner. There is a large marble room.")
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("search") or act == ("look around"):
                   print ("You don't find anything worth taking.")
            elif act == ("continue") or act == ("go right") or act == ("keep going"):
                loc = ("mainroom")
            elif act == ("go to marble room") or act == ("go to room") or act == ("go back"):
                loc = ("enterdun")
            else:
                print ("You can't " + act + " here!")


        #main room code
        while loc == ("mainroom"):
            print (" ")
            print ("You are in a large room with large two doors leading in on the left and right side and one large door in the center with the words \"Enter to meet your doom!\" echec into the stone above it")
            mainroomM += 1
            if mainroomM == 1:
                Mtype = ("Troll")
                Mhp = 10
                Mac = 2
                mG = 10
                dead = False
                locb = loc
                loc = ("comb")
                continue
            if droploc == loc:
                print ("You dropped a " + drop + " here!")
            act = input ("What would you like to do?:  ")
            if act == ("openinv"):
                locb = loc
                loc = ("inv")
            elif droploc == loc and drop != (" ") and act == ("take drop"):
                if i1 == ("<empty>"):
                    i1 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i2 == ("<empty>"):
                    i2 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i3 == ("<empty>"):
                    i3 = drop
                    drop = (" ")
                    droploc = (" ")
                elif i4 == ("<empty>"):
                    i4 = drop
                    drop = (" ")
                    droploc = (" ")
                else:
                    print ("Your inventory is full.")
            elif act == ("fkxr") and spell == True:
                locC = loc
                loc = ("home")
            elif act == ("search"):
                print ("You find a broadsword among a pile of bones.")
            elif act == ("get broadsword") or act == ("take broadsword"):
                if mainroomSw == False:
                    if i1 == ("<empty>"):
                        i1 = ("<broadsword>")
                        mainroomSw = True
                    elif i2 == ("<empty>"):
                        i2 = ("<broadsword>")
                        mainroomSw = True
                    elif i3 == ("<empty>"):
                        i3 = ("<broadsword>")
                        mainroomSw = True
                    elif i4 == ("<empty>"):
                        i4 = ("<broadsword>")
                        mainroomSw = True
                    else:
                       print ("Your inventory is full.")
                else:
                    print ("You already got the broadsword")
            elif act == ("go left"):
                loc = ("lpass")
            elif act == ("go right"):
                loc = ("rpass")
            elif act == ("enter") or act == ("go to door"):
                last = input ("There is no going back from here. Do any invintory manegment or other tasks now! Do you want to continue?:  ")
                if last == ("yes"):
                    loc = ("finial")
                else:
                    continue


        #finial room code
        while loc == ("finial"):
            bossM += 1
            print (" ")
            if finial == False:
                print ("You push the door open, to see A huge minotar staring you down. It charges!")
            time.sleep(1)
            if bossM == 1:
                Mtype = ("Minotar")
                Mhp = 25
                Mac = 3
                mG = 10000
                dead = False
                locb = loc
                loc = ("comb")
                finial = True
                continue
            if finial == True and dead == True:
                print ("Congradulations " + Pname + ", you won! You have face the minor challeng of compleeting the game and the major challenge of actuley playing this broken, buggy game! Now go, find a game that is actualy good!")
                time.sleep(5)
                sys.exit()


#game over code
print ("You are out of lives! GAME OVER!!!")
sys.exit()
