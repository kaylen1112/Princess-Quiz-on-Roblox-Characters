print("Find out which Roblox character you are!")
Builderman = 0
Guest = 0
Noob = 0
Bacon_Hair= 0
Jane_Doe =0
print()
color = input("What is your favorite color? (blue, pink, black, yellow, brown):")
if color == "black":
    guest+=1
elif color == "blue":
    Noob+=1
elif color == "pink":
    Jane_Doe+=1
elif color == "yellow":
    Builderman+=1
elif color == "brown":
    Bacon_Hair+=1
else:
    print("sorry, that wasn't an option.")
print()
style = input("What's your style? (Simple outfit, bright colors, casual clothes, work attire, all-black outfit):")
if style == "all-black outfit":
    Jane_Doe+=1
elif style == "bright colors":
    Noob+=1
elif style == "work attire":
    Builderman+=1
elif style == "simple outfit":
    Guest+=1
elif style == "casual clothes":
    Bacon_Hair+=1
else:
    print("sorry, that wasn't an option.")
print()
perception = input("How do you want other to see you? (Helpful leader, Introverted, Friendly, Determined, Mysterious):")
if perception == "helpful leader":
    Builderman+=1
elif perception == "friendly":
    Noob+=1
elif perception == "introverted":
    Guest+=1
elif perception == "mysterious":
    Jane_Doe+=1
elif perception == "determined":
    Bacon_Hair+=1
else:
    print("sorry, that wasn't an option.")
    
print()

game = input("Which Roblox game would you play, if you had to pick one? (Adopt Me - adopt and raise pets, Brookhaven - roleplay daily life, \nJailbreak - escape or catch criminals, Tower of Hell - timed tricky  obby, Piggy - survive scary scenarios):")
if game == "adopt me":
    Bacon_Hair+=1
elif game == "brookhaven":
    Guest+=1
elif game == "tower of hell":
    Noob+=1
elif game == "piggy":
    Jane_Doe+=1
elif game == "jailbreak":
    Builderman+=1
else:
    print("sorry, that wasn't an option.")

print()
adjective = input("Which term best describes your personality? (Hardworking, Secretive, Playful, Curious, Ambitious):")
if adjective == "hardworking":
    Builderman+=1
elif adjective == "secretive":
    Jane_Doe+=1
elif adjective == "curious":
    Guest+=1
elif adjective == "ambitious":
    Bacon_Hair+=1
elif adjective == "playful":
    Noob+=1
else:
    print("sorry, that wasn't an option.")
print()

food = input("Pick a food?! (Burger with fries, Classic sandwhich, batteries, Bloxy cola, Bacon):")
if food == "bloxy cola":
    Noob+=1
elif food == "sandwhich":
    Guest+=1
elif food == "bacon":
    Bacon_Hair+=1
elif food == "burger with fries":
    Builderman+=1
elif color == "batteries":
    Jane_Doe+=1
else:
    print("sorry, that wasn't an option.")
print()
weather = input("What is your favorite type of weather? (Sunny, Cloudy, Rainy, Windy, Foggy):")
if color == "foggy":
    Jane_Doe+=1
elif color == "cloudy":
    Guest+=1
elif color == "sunny":
    Builderman+=1
elif color == "rainy":
    Noob+=1
elif color == "windy":
    Bacon_Hair+=1
print()
food = input("What's your dream pet? (Goldfish, Dog, Parrot, Horse, Black cat):")
if food == "parrot":
    Noob+=1
elif food == "dog":
    Builderman+=1
elif food == "horse":
    Bacon_Hair+=1
elif food == "goldfish":
    Guest+=1
elif color == "black cat":
    Jane_Doe+=1
#seven more questions go here!
    
if Builderman >= Noob and Builderman >= Jane_Doe and Builderman >= Bacon_Hair and Builderman >= Guest:
    print("You are a Builderman!")
elif Guest >= Jane_Doe and Guest>=Bacon_Hair and Guest>=Noob:
    print("You are a Guest!")
elif Noob>=Jane_Doe and Noob>= Bacon_Hair:
    print("You are a Noob!")
elif Bacon_Hair>=Jane_Doe:
    print("You are a Bacon Hair!")
else:
    print("You are a Jane Doe!")