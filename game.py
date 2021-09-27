# UNDERSEA PALACE ADVENTURE
# Now updated to Python 3

# At the top of the file are declarations and variables we need.
# 
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

import random # random numbers (https://docs.python.org/3.3/library/random.html)
import sys # system stuff for exiting (https://docs.python.org/3/library/sys.html)

# an object describing our player
player = { 
    "name": "p1", 
    "score": 0,
    "items" : ["milk"],
    "friends" : [],
    "location" : "start"
}

rooms = {
    "room1" : "a main room",
    "room2" : "a park path",
    "room3" : "an narrow path"
}

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print ("You roll a: " + str(result) + " out of " + str(maxNum))

    if (result <= difficulty):
        print ("trying again....")
        
        input("press enter >")
        rollDice(minNum, maxNum, difficulty) # this is a recursive call

    return result

def printGraphic(name):
    if (name == "octopus"):
        print ('      ,'""'           ')
        print ('     / _  _ \         ')
        print ('     |(@)(@)|         ')
        print ('     )  __  (         ')
        print ('    /,.))((...\       ')
        print ('    (( ((  )) ))      ')
        print ('    `\ `)(` /`        ')
        print ('    the octopus       ')

    if (name == "gem"):
        print ('      ____      ')
        print ('     /\__/\     ')
        print ('    /_/  \_\    ')
        print ('    \ \__/ /    ')
        print ('     \/__\/     ')
        print ('                ')
        print ('     the gem    ')

    if (name == "scallop"):
        print ('       _.---._       ')
        print ('   .“""./ | \`."".   ')
        print ('  :  .. / | \ `.  :  ')
        print ('  ".“  /  |  \  ："  ')
        print ('   `. /   |   \ .`   ')
        print ('     `-.__|__.- `    ')
        print ('    A  scallop       ') # this one is escaped!

    if (name == "sea horse"):
        print ('     O                          ')
        print ('      O                         ')
        print ('       o  \``/                  ')
        print ('          /o `))                ')
        print ('         /_/\_ss))              ')
        print ('             |_ss))/|           ')
        print ('            |__ss))_|           ')
        print ('            |__sss))_|          ')
        print ('            |___ss))\|          ')
        print ('                |_ss))          ')
        print ('                )_s))           ')
        print ('           (`(  /_s))           ')
        print ('           (_\/_s))             ')
        print ('            (\/))               ')
        print ('        sea horse               ')

    if (name == "title"):
        print ('-----------------------------------------------------------------------------')
        print ('                           ___  ___  __ _                                    ')
        print ('                          / __|/ _ \/ _` |                                   ')
        print ('                          \__ \  __/ (_| |                                   ')
        print ('                          |___/\___|\__,_|                                   ')
        print ('                o                                                            ')
        print ('                  o                                                          ')
        print ('                    o                                                        ')
        print ('                     o   .````.                                              ')
        print ('                         o /O)   `./|                                        ')
        print ('                         > ) \| .`\|                                         ')
        print ('                         `....`                                              ')
        print ('                             ` `                                             ')
        print ('-----------------------------------------------------------------------------')



def gameOver():

    printGraphic("octopus")

    print("-------------------------------")
    print("to be continued!")
    print("name: " + player["name"] ) # customized with a name
    print( "score: " + str(player["score"]) ) # customized with a score
    return

def darkPath():
    print("The path looks are very narrow but you move forward anyway...")
    print("You enter a room that there are one big scallop in the middle of the room, you stop when you see the scallop is alive, you go closer")
    print("You went closer see there is a dice on the floor ...")
    printGraphic("scallop")
    input("press enter >")

    print("You consider your options.")
    print("options: [ roll the dice , keep going , back to mainroom]")

    pcmd = input(">")

    if (pcmd == "roll the dice"): 
        print ("You roll the dice...")
        print ("Let's roll a dice to see what happens next!")

        # roll a dice from 0 to 20 to see what happens
        # if your number is higher than the difficulty, you win!
        difficulty = 8
        roll = rollDice(0, 20, difficulty)
        
        # you have to get lucky! this only happens to the player
        # if you roll the dice high enough
        if (roll >= difficulty):
            print ("It looks like a magic gem. Right here inside the scallop!")
            print ("Do you take the gem?")
            
            printGraphic("gem")

            # we dive further into the logic
            pcmd = input("yes or no >")

            if (pcmd == "no"):
                print ("You leave it there.")
                darkPath()

            elif (pcmd == "yes"):
                print ("You pick it up and return to the main room.")
                player["items"].append("gem") # add an item to the array with append
                player["score"] += 100 # add to the score
                mainRoom()

            else:
                print ("You leave it there.")
                mainRoom()

        else:
            print ("Turns out it's nothing... oh well.")
            darkPath()

    elif (pcmd == "keep going"):
        print ("You keep going forward... you have a strange feeling")
        print ("that you keep went into the same room over and over...") # the lost woods reference
        darkPath()

    elif (pcmd == "back to main room"):
        print ("You decide to go back.")
        pcmd = input(">")
        mainRoom()

    else:
        print ("You can't do that!")
        darkPath()


def narrowPath():
    print ("The dark path leads you to a room with full of gold coins.")
    print ("It is a very glory.")
    input("press enter >")

    printGraphic("octopus")
    print ("You want to grab some gold and put in your backpack, but you feel something is behind you.")
    print ("you trun around, there is a big octopus watching you!")
    print ("...He can talk!")
    input("press enter >")
    
    print ("You consider your options.")

    # check the list for items
    # the 'in' keyword helps us do this easily
    if ("gem" in player["items"]):
        print ("options: [ look around , talk to octopus , give gem, run ]")
    else:
        print ("options: [ go back, talk to octopus, run ]")

    pcmd = input(">")

    # option 1: look at the octopus
    if (pcmd == "go back"):
        print ("You go back...")
        mainRoom() # try again
    
    # option 2: talk to the octopus
    elif (pcmd == "talk to octopus"):
        print ("He told you you need to play with him with a dice, if your number is bigger than 5, you win, otherwise... you stay!")
        print ("Let's roll a dice to see what happens next!")
        input("press enter to roll >")

        difficulty = 5
        chanceRoll = rollDice(0,20,difficulty) # roll a dice between 0 and 20

        # if the roll is higher than 5... 75% chance
        if (chanceRoll >= difficulty):
            print ("It's you're lucky day! You win the Octopus.")
            player["score"] += 50
        else:
            print ("You did not win the octopus, then you feel black out .")
            narrowPath() # try again
        
        # nested actions and ifs
        pcmd = input("he ask you if you want leave the palace? yes or no >")

        # yes
        if (pcmd == "yes"):

            print ("You leave the palace and back to the shore!")

            player["friends"].append("white fox")

            # string and int converstion!
            # we need to convert the score to a number to add to it
            # then convert it back to a string to display it to the player
            player["score"] = int(player["score"]) + 100 # conversion

            # we generate a custom string and add the score
            print ( "Your score increased to: " + str(player["score"]) ) 
            
            gameOver()

        # no
        elif (pcmd == "no"):
            print ("He throw you into darkness!")
            narrowPath()
        
        # try again
        else:
            narrowPath()

    elif (pcmd == "give gem"):
        print ("You give the gem to the octopus!")
        input("press enter>")
        printGraphic("gem")
        gameOver()


    # option 3: run
    elif (pcmd == "run"):
        print ("You run!")
        mainRoom() # back to start

    # try again
    else:
        print ("I don't understand.")
        narrowPath() # forest path

def mainRoom():
    print ("You stand in the main room.")
    print ("There is a path ahead of you and another path to the right,one is dark, one is narrow.")
    
    # this piece of game logic checks to see if the requirements are met to continue.
    # we can have some fun and change the options for the player
    # based on variables we stored

    # 1. check the list of items, to see if it is there
    # 2. check the list of friends, to see if you are in friends list

    if (("gem" in player["items"]) and not ("octopus" in player["friends"])):
        print ("Your options: [ look around, dark path, trade gem with the sea horse]")

    elif ("gem" in player["items"]):
        print ("Your options: [ look around, path, exit ]")

    else:
        print ("Your options: [ look around, dark path , narrow path , exit ]")

    pcmd = input(">") # user input

    # player options
    if (pcmd == "look around"):
        # its a trick!
        print ("You look around... the path behind you is .... gone?")

        input("press enter >")
        mainRoom()

    # path option
    elif (pcmd == "dark path"):
        print ("You take the dark path.")
        input("press enter >")
        narrowPath() # path 1

    # path2 option
    elif (pcmd == "narrow path"):
        print ("You take the narrow path.")
        input("press enter >")
        darkPath() # path 2

    # exiting / catching errors and crazy inputs
    elif (pcmd == "exit"):
        print ("you exit.")
        return # exit the application
        
    elif (pcmd == "trade gem with the sea horse"):
        print ("you give the gem to the sea horse... hugh?")
        printGraphic("sea horse")

        print ("'wooooooooooooow'\", he says.") # escaped
        return # exit the application, secret ending

    else:
        print ("I don't understand that")
        mainRoom() # the beginning

def introStory():
    # let's introduce them to our world
    print ("Good to see you gain! What should I call you?")
    player["name"] = input("Please enter your name >")

    # intro story, quick and dirty (think star wars style)
    print ("Welcome to the undersea adventure " + player["name"] + "!")
    print ("The story so far...")
    print ("You are going to diving yourself at the pacific sea.")
    print ("You start diving down, and you found a palace at the bottom of the sea,.")
    print (" and there seem has a lot of treasure ahead")
    print (" there are couple ways you can go, please choose one....")

    pcmd = input("please choose yes or no >")

    # the player can choose yes or no
    if (pcmd == "yes"):
        print ("You walk down the path, it leads into a main room that has couple path...")
        input("press enter >")
        mainRoom()
    else:
        print ("No? ... the entrance has closed..")
        pcmd = input("press enter >")
        introStory() # repeat over and over until the player chooses yes!



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens