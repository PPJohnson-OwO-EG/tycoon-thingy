import random       #requirements
import time
import pygame
import os
import sys


def gamestart(): #simple intro. add name input and change into main menu later
    pygame.init()
    pygame.mixer.init()
        
    if getattr(sys, 'frozen', False):
        script_dir = os.path.dirname(sys.executable)
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))    
        
    music_path = os.path.join(script_dir, "Music", "Boot.mp3")
    
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(1)
    dots("Loading")
    print()

    
    print('CD loaded successfully.')
    print()
    time.sleep(3)
    
    


    music_path = os.path.join(script_dir, "Music", "Leadership.mp3")

    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)    #makes it loop
    
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
        
        else:
            print('Invalid input.')
            print()
    
    menu_stuff["manager name"] = input("What is the manager's name?-")
    dots(menu_stuff["manager name"])
    
    if menu_stuff["manager name"] == "Manager" or menu_stuff["manager name"] == "manager":
        dots("Hilarious")
    
    else:
        dots("Brilliant")
    
    menu_stuff["name"] = input("What is your name?-")
    dots(menu_stuff["name"])
    
    if menu_stuff["name"] == menu_stuff["manager name"]:
        dots('Of course')
        print("Of course they're the same.")
        time.sleep(2.5)
        
    else:
        dots("Lovely")
    
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
    
    if time_stuff["days"] == 7:                         #on each cycle of the while loop, the days increase by 1. When it reaches 7 it adds an extra week and goes into the menu. 
        time_stuff["days"] = 0
        time_stuff["weeks"] += 1
        print(f'Week {time_stuff["weeks"]}')
        time_stuff["selection mode"] = 1
        
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
                
        
            else:
                print('Invalid input.')

def build():                         #build menu
    while True:
        print()
        print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}')
        print()
        print('What would you like to build?')
        print()
        build_choice = input('Logging Camp, Stone Mine, Trading Post, Farm, Housing Estate or Exit.')
        
        if build_choice == 'Logging Camp':
            if resources["gold"] >= 5 and resources["wood"] >= 5 and resources["stone"] >= 2: 
                buildings.append('logging camp')
                resources["gold"] -= 5
                resources["wood"] -= 5
                resources["stone"] -= 2
            else:
                print('Not enough resources!')
            
        elif build_choice == 'Stone Mine':
            if resources["gold"] >= 5 and resources["wood"] >= 5 and resources["stone"] >= 2: 
                buildings.append('stone mine')
                resources["gold"] -= 5
                resources["wood"] -= 5
                resources["stone"] -= 2
            else:
                print('Not enough resources!')
            
        elif build_choice == 'Trading Post':
            if resources["gold"] >= 5 and resources["wood"] >= 5 and resources["stone"] >= 2: 
                buildings.append('trading post')
                resources["gold"] -= 5
                resources["wood"] -= 5
                resources["stone"] -= 2
            else:
                print('Not enough resources!')
                
        elif build_choice == 'Farm':
            if resources["gold"] >= 5 and resources["wood"] >= 5:
                buildings.append('farm')
                resources["gold"] -= 5
                resources["wood"] -= 5
            else:
                print('Not enough resources!')
                
        elif build_choice == 'Housing Estate':
            if resources["gold"] >= 5 and resources["wood"] >= 5 and resources["stone"] >= 7:
                buildings.append('housing estate')
                resources["gold"] -= 5
                resources["wood"] -= 5
                resources["stone"] -= 7
            else:
                print('Not enough resources!')
        
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
                        break
                    
                    elif resources["gold"] < researchables_dic[research_selection]["gold cost"]:
                        print('Not enough resources!')
                        break
                    
                elif confirm == 'NO':
                    break
                
                else:
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
            resources["housing"] += 25
            

def pop_growth():                       #population growth and decline formula
    if resources["food"] > 0:
        population_increase = resources["population"] // 10
        resources["population"] += population_increase
    else:
        population_decline = resources["population"] // 7
        resources["population"] -= population_decline
        
    pop_hunger = resources["population"] // 4
    
    resources["food"] -= pop_hunger
    
    resources["population"] = min(resources["population"], resources["housing"])
    
def base_gain():            #prevents soft-locks at the start 
    resources["gold"] += 1
    resources["stone"] += 1
    resources["wood"] += 1
    resources["food"] += 1

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
    for event_loop in events:
        roll = random.randint(1,100)
        
        if roll <= events_dic[event_loop]["chance"]:
            print(f'{event_loop}!')
            
            if "pop_loss" in events_dic[event_loop]:
                lost_pop = resources["population"] // events_dic[event_loop]["pop_loss"]
                resources["population"] -= lost_pop
                print(f'You lost {lost_pop} people!')
                
            
            
    
    
    
    
    
#dictionaries

menu_stuff = {
    "name": "",
    "manager name": "",
    }


time_stuff = {
    "days": 0,
    "days_total": 0,
    "weeks": 0,
    "selection mode": 0,
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
    "logging camp" : {
        "wood gain": 5,
        },
    "stone mine" : {
        "stone gain" : 5,
        },
    
    "trading post" : {
        "gold gain" : 5,
        },
    
    "farm" : {
        "food gain" : 5,
        },
    
    "housing estate" : {
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
    
    }

events_dic = {
    "Fire": {
        "chance": 2,
        "pop_loss": 10,
        },
    }

#lists

buildings = []

researchables = ["Irrigation", "Better Pickaxes"]
researched = []

events = ["Fire"]


#game

gamestart()
print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}')
print()
while True:
    time_change()
    death_check()
    resource()
    base_gain()
    pop_growth()
    event()
    resource_clamp()
    selection()
    time.sleep(1.5)
    print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}')
    print()
    
    
    
    
    