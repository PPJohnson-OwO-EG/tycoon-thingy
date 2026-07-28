import random       #requirements
import time
import pygame
import os
import sys
from colorama import init
init()

RED = "\033[31m"                #ansi codes, just type variable name in any string and you'll have the beauty of colour
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
BLACK   = "\033[30m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"
RESET = "\033[0m"


pygame.init()                            #have to loud event sound effects here, otherwise undefined error
pygame.mixer.init()

if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

fire_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Fire_Scream.mp3"))        #simply tells the program that the path to the files is inside the music folder, not next to the .exe
cough_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Cough.mp3"))             #must define all audio files here, besides main track and boot
build_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Build.mp3"))
breathe1_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Breathe_1.mp3"))
breathe2_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Breathe_2.mp3"))
effect_channel = pygame.mixer.Channel(1)
insanity_channel = pygame.mixer.Channel(3)



def gamestart(): #intro
    music_path = os.path.join(script_dir, "Music", "Boot.mp3")
    
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(1)
    dots("Loading")
    print()

    
    print('CD loaded successfully.')
    print()
    time.sleep(3)
    
    


    leadership = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Leadership.mp3"))
    leadership_channel = pygame.mixer.Channel(2)

    leadership_channel.play(leadership, loops=-1)
    leadership_channel.set_volume(0)

    steps = 30                                               #yes I stole this code, no I dont fucking care
    duration = 1.5  # seconds
    for i in range(steps + 1):
        vol = i / steps
        pygame.mixer.music.set_volume(1 - vol)   # Boot fades out
        leadership_channel.set_volume(vol)        # Main fades in
        time.sleep(duration / steps)

    pygame.mixer.music.stop()  # Boot is fully silent now, free up the music channel
    
    print('Welcome to Leadership.')
    print()
    time.sleep(1)
    
    
    while True:
        print('PLAY                   EXIT')
        game_select = input()
        print()
        
        if game_select == 'PLAY':
            time.sleep(0.5)
            break
        
        elif game_select == 'EXIT':
            time.sleep(0.5)
            print('Formatting C: Drive.')
            exit()
            
        elif game_select == 'SKIP':
            return
        
        else:
            print('Invalid input.')
            print()
    
    menu_stuff["manager name"] = input("What is the manager's name?-")
    dots(menu_stuff["manager name"])
    
    if menu_stuff["manager name"] == "Manager" or menu_stuff["manager name"] == "manager":
        dots("Hilarious")
        
    elif menu_stuff["manager name"] == 'John Pork':
        dots('I know who you are')
    
    else:
        dots("Brilliant")
    
    print()
    menu_stuff["name"] = input("What is your name?-")
    dots(menu_stuff["name"])
    
    if menu_stuff["name"] == menu_stuff["manager name"]:
        dots('Of course')
        print("Of course they're the same.")
        time.sleep(2.5)
        
    elif menu_stuff["name"] == 'Ismael' or menu_stuff["name"] == 'ismael':
        print('Leave')
        menu_stuff["ismael mode"] = 1
        time.sleep(3)
        
    elif menu_stuff["name"] in suspicious_names:
        dots("Oh")
        dots("It's")
        print('You.')
        time.sleep(3)
        
        
    else:
        dots("Lovely")
    
    print()
    print(f'{menu_stuff["name"]}, you will begin now.')
    print()
    
    time.sleep(3)


def dots(text):
    print()                              #for the dots at the end of each line in the intro
    print(text, end="", flush=True)      #end allows for the dots to be on the same line as the text, flush fixes time.sleep bug in python terminal
    time.sleep(0.75)

    for delay in (0.75, 1, 1.25):         #goes through each timer and adds a dot.
        print(".", end="", flush=True)
        time.sleep(delay)

    print()


def time_change():                                      #time progression
    time_stuff["days"] += 1
    time_stuff["days_total"] += 1
    time_stuff["insanity"] += 1
    
    if time_stuff["days"] == 7:                         #on each cycle of the while loop, the days increase by 1. When it reaches 7 it adds an extra week and goes into the menu. 
        time_stuff["days"] = 0
        time_stuff["weeks"] += 1
        print(f'Week {time_stuff["weeks"]}')
        time_stuff["selection mode"] = 1
        time_stuff["insanity"] += 3
        
        return
    else:
        time_stuff["selection mode"] = 0
        
    

def selection():                                        #selection menu that shows up every 7 days.
    if time_stuff["selection mode"] == 1:
        print('Choose something-')
        
        while True:
            selection_choice = input('Build, Research, Continue-')
            if selection_choice == 'Continue':
                time_stuff["selection mode"] = 0
                return
            elif selection_choice == 'Build':
                build()
                
                        
            elif selection_choice == 'Research':
                research()
                
            elif selection_choice == 'Debug':
                debug()
                
        
            else:
                print('Invalid input.')

def build():                         #new build menu, much more modular and efficient
    while True:
        print()
        print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}')
        print()
        print("What would you like to build? ('Exit' to leave)")
        print()
        print(available_buildings)
        build_choice = input()
        
        if build_choice in available_buildings:
            print()
            print(f'{building[build_choice]["description"]}   Costs: {building[build_choice]["wood cost"]} wood | {building[build_choice]["gold cost"]} gold | {building[build_choice]["stone cost"]} stone')
            
            while True:
                confirm = input(f'Do you wish to build a {build_choice}? (YES/NO)-')
                
                if confirm == 'YES':
                    if resources["gold"] >= building[build_choice]["gold cost"] and resources["wood"] >= building[build_choice]["wood cost"] and resources["stone"] >= building[build_choice]["stone cost"]:
                        effect_channel.play(build_sound)
                        resources["gold"] -= building[build_choice]["gold cost"]
                        resources["wood"] -= building[build_choice]["wood cost"]
                        resources["stone"] -= building[build_choice]["stone cost"]
                        buildings.append(build_choice)
                        print(f'{build_choice} built!')
                        time_stuff["insanity"] += 3
                        print()
                    else:
                        print()
                        dots('Not enough resources')
                        time_stuff["insanity"] += 5
                        break
                    
                    
                elif confirm == 'NO':
                    time_stuff["insanity"] += 3
                    break
                    
                else:
                    time_stuff["insanity"] += 1
                    print('Invalid input.')
                
        
        
        
        elif build_choice == "Exit":
            break
        
        else:
            print('Invalid input.')

def research():               #research menu
    print()
    print(f'Available for Research: {researchables}')
    print()
    
    while True:
        research_selection = input('Choose something to research (Exit to leave).')
    
        if research_selection in researchables:
            print(f' {researchables_dic[research_selection]["gold cost"]} gold. {researchables_dic[research_selection]["description"]}')
            
            while True:
                confirm = input('Do you wish to research this? (YES/NO)')
        
                if confirm == 'YES':
                    if resources["gold"] >= researchables_dic[research_selection]["gold cost"]:
                        resources["gold"] -= researchables_dic[research_selection]["gold cost"]
                        researched.append(research_selection)
                        researchables.remove(research_selection)
                        time_stuff["insanity"] += 2
                        break
                    
                    elif resources["gold"] < researchables_dic[research_selection]["gold cost"]:
                        print('Not enough resources!')
                        break
                    
                elif confirm == 'NO':
                    time_stuff["insanity"] += 5
                    break
                
                else:
                    time_stuff["insanity"] += 1
                    print('Invalid input!')
                    
        elif research_selection == 'Exit':
            return
                
        else:
            print('Research does not exist.')
        
        
        
            
def resource():                      #resource production
    resources["housing"] = 25        #base housing
    
    for x in buildings:
        if "wood gain" in building[x]:
            resources["wood"] += building[x]["wood gain"]
            
        if "gold gain" in building[x]:
            if 'Better Pickaxes' in researched:
                (resources["gold"]) += (building[x]["gold gain"] * researchables_dic["Better Pickaxes"]["bonus"])
            else:    
                resources["gold"] += building[x]["gold gain"]
                
        if "stone gain" in building[x]:
            if 'Better Pickaxes' in researched:
                (resources["stone"]) += (building[x]["stone gain"] * researchables_dic["Better Pickaxes"]["bonus"])
            else:    
                resources["stone"] += building[x]["stone gain"]
                
        if "food gain" in building[x]:
            if 'Irrigation' in researched:
                (resources["food"]) += (building[x]["food gain"] * researchables_dic["Irrigation"]["bonus"])
            else:    
                resources["food"] += building[x]["food gain"]
                
    for build in buildings:                 #cycles through each building that is a house and adds it to the housing number
        if build == 'housing estate':
            resources["housing"] += building["housing estate"]["housing gain"]
        elif build == 'housing cheat':
            resources["housing"] += building["housing cheat"]["housing gain"]
            

def pop_growth():                       #population growth and decline formula
    pop_hunger = max(1, resources["population"] // 4)
    
    
    if resources["food"] >= pop_hunger:
        resources["food"] -= pop_hunger
        
        population_increase = max(1, resources["population"] // 10)
        resources["population"] += population_increase
        
    else:
        population_decline = max(1, resources["population"] // 3)
        resources["population"] -= population_decline
        
        print(f'{population_decline} people died from starvation.')
        
    resources["population"] = min(resources["population"], resources["housing"])
    
def base_gain():            #prevents soft-locks at the start
    if menu_stuff["ismael mode"] == 0:
        resources["gold"] += 1
        resources["stone"] += 1
        resources["wood"] += 1

def death_check():                 #checks for death
    if resources["population"] <= 0:
        print("All the population has been wiped out, or just left. All that remains is a ghost town.")
        time.sleep(1)
        print()
        print("STATS:")
        print(f'Days survived: {time_stuff["days_total"]}')
        print()
        print("Game will close in 10 seconds.")
        time.sleep(10)
        exit()
        
def resource_clamp(): #prevents stuff from going below 0
    resources["food"] = max(0, resources["food"])
    resources["gold"] = max(0, resources["gold"])
    resources["wood"] = max(0, resources["wood"])
    resources["stone"] = max(0, resources["stone"])
    resources["population"] = max(0, resources["population"])
    
    
def event():
    for event_name in events:
        chance = get_event_chance(event_name) #runs function for chance of event occuring
        roll = random.randint(1,100) #roll that will go up against event chance
        
        if roll <= chance:
            print(f'{event_name}.')
            
            
            effect_channel.play(events_dic[event_name]["sound"])  #plays event sound
            time.sleep(1.5)
            time_stuff["insanity"] += 10
            
            if "pop_loss" in events_dic[event_name]:                                             #dont have to make an if for every type of event
                lost_pop = max(1, resources["population"] // events_dic[event_name]["pop_loss"])
                resources["population"] -= lost_pop
                print(f'You lost {lost_pop} people.')
                
                
                
            
def debug():
    print()
    dots('Choose')
    
    
    while True:
        print("Set Food, Set Gold, Set Wood, Set Stone, Set Population, Set Housing, Max Resources, Insanity. 'Exit' to leave.")
        print()
        debug_choice = input()
    
        if debug_choice == 'Set Food':
            while True:
                amount_desired = input(f"Set the amount of 'food' you desire.")
                if amount_desired.isdigit():
                    resources["food"] = int(amount_desired)
                    print('Amount set.')
                    print()
                    break
                else:
                    print('Invalid input.')
                
            
            
        elif debug_choice == 'Set Gold':
            while True:
                amount_desired = input(f"Set the amount of 'gold' you desire.")
                if amount_desired.isdigit():
                    resources["gold"] = int(amount_desired)
                    print('Amount set.')
                    print()
                    break
                else:
                    print('Invalid input.')
            
        elif debug_choice == 'Set Stone':
            while True:
                amount_desired = input(f"Set the amount of 'stone' you desire.")
                if amount_desired.isdigit():
                    resources["stone"] = int(amount_desired)
                    print('Amount set.')
                    print()
                    break
                else:
                    print('Invalid input.')
                    
        elif debug_choice == 'Set Population':
            while True:
                amount_desired = input(f"Set the amount of 'population' you desire.")
                if amount_desired.isdigit():
                    resources["population"] = int(amount_desired)
                    print('Amount set.')
                    print()
                    break
                else:
                    print('Invalid input.')
                    
        elif debug_choice == 'Set Housing':
            while True:
                amount_desired = input(f"Set the amount of 'housing' you desire.")
                if amount_desired.isdigit():
                    building["housing cheat"]["housing gain"] = int(amount_desired)
                    print('Amount set.')
                    print()
                    buildings.append("housing cheat")
                    break
                else:
                    print('Invalid input.')
                    
        elif debug_choice == 'Max Resources':
            dots('Granted')
            resources["food"] = 10000000
            resources["gold"] = 10000000
            resources["stone"] = 10000000
            resources["wood"] = 10000000
            
        elif debug_choice == 'Insanity':
            while True:
                amount_desired = input(f"Set the amount of 'insanity' you desire.")
                if amount_desired.isdigit():
                    time_stuff["insanity"] = int(amount_desired)
                    print('Amount set.')
                    print()
                    break
                else:
                    print('Invalid input.')
            
        elif debug_choice == 'Exit':
            return
            
        else:
            print('Invalid input.')
            
            
            
def prize_check():
    if time_stuff["weeks"] == 20:
        dots('Congratulations')
        dots('You have survived 20 weeks')
        dots('Keep going')
        time_stuff["insanity"] += 20
    
def get_event_chance(event_name):                #this makes making research that change event chances extremely easy and efficient
    chance = events_dic[event_name]["chance"]    #just easier this way

    for research in researched:
        modifiers = researchables_dic[research].get("event_modifiers", {})   #.get prevents crashes. basically if event modifiers isnt in the dictionary it wont crash
        chance += modifiers.get(event_name, 0) #if the research changes the event, add modifier, if it doesnt add 0

    return max(0, chance)    #no negatives

def building_unlock():                      #research unlocks buildings
    for research in researched:             #checks every finished research
        if "building_unlock" in researchables_dic[research]:                   #building unlock is a list to allow for multiple unlocks from one research
            for unlocked in researchables_dic[research]["building_unlock"]:    #goes through each research that unlocks a building, if the unlocked building is not in the available buildings list, it adds it.     
                if unlocked not in available_buildings:
                    available_buildings.append(unlocked)
            
def insanity_check():
    if time_stuff["insanity"] >= 100:
        insanity_play = random.choice(insanity_sounds)
        insanity_channel.play(insanity_play)
        time_stuff["insanity"] = 0
        
        
    
    
#dictionaries

menu_stuff = {
    "name": "",
    "manager name": "",
    "ismael mode": 0,
    }


time_stuff = {
    "days": 0,
    "days_total": 0,
    "weeks": 0,
    "selection mode": 0,
    "insanity": 0,
    }



resources = {
    "food": 100,
    "gold": 10,
    "wood": 10,
    "stone": 10,
    "population": 10,
    "housing": 25,
    }




building = {
    "Logging Camp" : {
        "wood gain": 5,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "description": "Produces 5 wood per day.",
        },
    "Stone Mine" : {
        "stone gain" : 5,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "description": "Produces 5 stone per day.",
        },
    
    "Trading Post" : {
        "gold gain" : 3,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "description": "Produces 5 gold per day.",
        },
    
    "Farm" : {
        "food gain" : 5,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 0,
        "description": "Produces 5 food per day.",
        },
    
    "Housing Estate" : {
        "housing gain": 25,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "description": "Increases housing by 25.",
        },
    
    "Pharmacy" : {
        "population bonus": 1.05,
        "wood cost": 15,
        "gold cost": 25,
        "stone cost": 20,
        "description": "Increases population growth by 5 percent (stacks)",
        },
    
    "Large Stone Mine" : {
        "stone gain" : 15,
        "wood cost": 8,
        "gold cost": 18,
        "stone cost": 15,
        "description": "Produces 15 stone per day",
        },
    
    "Gold Mine" : {
        "gold gain" : 8,
        "wood cost": 25,
        "gold cost": 15,
        "stone cost": 30,
        "description": "Produces 8 gold per day",
        },
        
    
    "housing cheat" : {
        "housing gain": 0,
        },
    
    }


researchables_dic = {
    "Irrigation" : {
        "gold cost": 20,
        "bonus": 1.2,
        "description": "Increases farm output by 20 percent.",
        },
    
    "Better Pickaxes" : {
        "gold cost": 50,
        "bonus": 1.2,
        "description": "Increases mine output by 20 percent.",
        },
    
    "Wells" : {
        "gold cost": 30,
        "event_modifiers": {
            "Fire": -8
            },
        "description": "Decreases the chances of a fire sprouting.",
        },
    
    "Basic Healthcare" : {
        "gold cost": 30,
        "event_modifiers": {
            "Disease": -8
            },
        "building_unlock": ["Pharmacy"],
        "description": "Decreases the chance of basic diseases spreading. Won't do anything against a real plague however. Unlocks Pharmacies, which increase population growth.",
        },
    
    "Mass Scale Mines" : {
        "gold cost": 125,
        "building_unlock": ["Large Stone Mine", "Gold Mine"],
        "description": "Unlocks the Large Stone Mine and the Gold Mine.",
       }
    
    }

events_dic = {      
    "Fire": {
        "chance": 10,
        "pop_loss": 10,
        "sound": fire_sound,
        },
    
    "Disease": {
        "chance": 10,
        "pop_loss": 10,
        "sound": cough_sound,
        },
    
    }

#lists

buildings = []
available_buildings = ["Logging Camp", "Stone Mine", "Trading Post", "Farm", "Housing Estate"]

researchables = ["Irrigation", "Better Pickaxes", "Wells", "Basic Healthcare", "Mass Scale Mines"]
researched = []

events = ["Fire", "Disease"]

suspicious_names = ["Kirill", "Matthew", "Emmanuel", "Edward", "kirill", "matthew", "emmanuel", "edward",]

insanity_sounds = [breathe1_sound, breathe2_sound]


#game

gamestart()
print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}')
print()
while True:
    death_check()
    time_change()
    resource()
    base_gain()
    pop_growth()
    event()
    insanity_check()
    resource_clamp()
    prize_check()
    selection()
    time.sleep(1.5)
    print('------------------------------------------------------------------------------------------------------------------------')
    print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}')
    print()
    
    
    
    
    