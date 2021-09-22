myBackpack = {"brand": "Uniqlo", "color": "black", "material": "Nylon", "speciality":"Waterproof"}
print (myBackpack) 

myJacket = {"brand": "Champion", "color": "black", "material": "Cotton", "Style":"Full-Zip Hoodie"}
print (myJacket)

myBlanket = {"brand": "Ralph Lauren", "color": "black and white", "material": "fur", "Style":"check pattern","touch":"soft"}
print (myBlanket)

myComputer = {"brand": "apple", "color": "spacegray", "model": "MacBook Pro", "Memory":"8 GB", "Year":"2019"}
print (myComputer)

{
    "name": "choco",
    "color": "brown,black and white",
    "species": "dog",
    "breed": "shelti",
    "count": "1",
    "location": "boston"


} 

# let the user know what's going on
print ("Welcome to Yilab!")
print ("Answer the questions below to play.")
print ("-----------------------------------")

# variables containing all of your story info
discribleWord = input("Enter an adjective: ")
animal = input("What is your favorite animal?: ")
country = input("Name a place: ")
number = input("An number from your one to ten: ")
color = input("What is your favorite color: ")
pluralFood = input("Your favorite food: ")
action = input("What were you doing this morning: ")
song = input("Enter one song you like: ")
feeling = input("What do you feel when you lost 100 dollar: ")
language = input("What language do you want to learn: ")
feeling2 = input("How do you feel right now: ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story = "There once was a  " + discribleWord +" " + animal + " from " + country + " Nobody knows he was a " + animal + " because he had" \
+ color + "fur and ate " + pluralFood + " each day." + action + ". He like to  " + action +  \
"and sing " + song  + " Whenever he was " + feeling + " He wouch start speaking " + language + \
"Then he wouch feel " + feeling2 + " . " \


# finally we print the story
print (story)
