import random       #requirements
import time
import pygame
import os
import sys
import json
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
breathe3_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Breathe_3.mp3"))
bang_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Bang.mp3"))
click_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Click.mp3"))
click2_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Click_2.mp3"))
knocking_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Knocking.mp3"))
flood_sound = pygame.mixer.Sound(os.path.join(script_dir, "Music", "Flood.mp3"))


effect_channel = pygame.mixer.Channel(1)       #different channels for different audios, prevents audio cutting off and allows for overlapping audio
insanity_channel = pygame.mixer.Channel(3)
user_click_channel = pygame.mixer.Channel(4)
game_click_channel = pygame.mixer.Channel(5)





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
    
    game_print('Welcome to Leadership.')
    print()
    time.sleep(1)
    
    
    while True:
        game_print('PLAY     |     LOAD     |     HELP     |     EXIT')
        game_select = input()
        user_click_channel.play(click_sound)
        print()
        
        if game_select == 'PLAY':
            time.sleep(0.5)
            break
        
        elif game_select == 'LOAD':
            load_game()
            print()
            dots('Loading')
            game_print('Game Loaded')
            time.sleep(1)
            return
        
        elif game_select == 'HELP':
            help_func()
        
        elif game_select == 'EXIT':
            time.sleep(0.5)
            game_print('Formatting C: Drive.')
            time.sleep(0.1)
            exit()
            
        elif game_select == 'SKIP':
            menu_stuff["manager name"] = 'null'
            menu_stuff["name"] = 'null'
            return
        
        else:
            game_print('Invalid input.')
            print()
    
    game_print("What is the manager's name?-")
    menu_stuff["manager name"] = input()
    user_click_channel.play(click_sound)
    dots(menu_stuff["manager name"])
    
    if menu_stuff["manager name"] == "Manager" or menu_stuff["manager name"] == "manager":
        dots("Hilarious")
        
    elif menu_stuff["manager name"] == 'John Pork':
        dots('Not funny')
    
    else:
        game_click_channel.play(click2_sound)
        dots("Brilliant")
    
    print()
    game_print("What is your name?-")
    menu_stuff["name"] = input()
    user_click_channel.play(click_sound)
    dots(menu_stuff["name"])
    
    if menu_stuff["name"] == menu_stuff["manager name"]:
        dots('Of course')
        game_print("Of course they're the same.")
        time.sleep(2.5)
        
    elif menu_stuff["name"] == 'Ismael' or menu_stuff["name"] == 'ismael':
        game_print('Leave')
        menu_stuff["ismael mode"] = 1
        time.sleep(3)
        
    elif menu_stuff["name"] in suspicious_names:
        dots("Oh")
        dots("It's")
        game_print('You.')
        time.sleep(3)
        
        
    else:
        dots("Lovely")
    
    print()
    game_print(f'{menu_stuff["name"]}, you will begin now.')
    print()
    
    time.sleep(3)


def help_func():
    print()
    
    if time_stuff["insanity"] >= 50:
        game_print("No.")
        time_stuff["insanity"] += 3
        print()
        time.sleep(1)
        return
    
    
    game_print('Keep your population from reaching zero.')
    time.sleep(3)
    game_print('Always have enough gold to pay for the maintenance of your buildings.')
    time.sleep(3)
    game_print('Otherwise, you must sell your buildings and/or sell your people.')
    time.sleep(3)
    game_print('Always have enough food to feed your population.')
    time.sleep(3)
    game_print('Each building requires a certain amount of workers, if there are more jobs available than there are people, the production of your buildings will decrease.')
    time.sleep(3)
    game_print("This is known as 'worker ratio'. You want to keep it at 1.")
    time.sleep(3)
    game_print('Your people require housing. Your population will not increase past the amount of housing available.')
    time.sleep(3)
    game_print("You have a limit of how many resources you can store. Research 'Storage' and build granaries/warehouses to increase that limit.")
    time.sleep(3)
    game_print('Every seven days, you will have the ability to build new buildings and research new technologies.')
    time.sleep(3)
    game_print('Use this period wisely.')
    time.sleep(3)
    game_print('Always type exactly what is asked of you.')
    time.sleep(3)
    
    print()
    game_print('Understand now?')
    
    
    understand = input('(YES/NO)')
    user_click_channel.play(click_sound)
    
    if understand == 'YES' or understand == 'Yes':
        print()
        dots('Good')
        print()
        return
    else:
        print()
        game_print('Idiot.')
        print()
        time.sleep(1)
        time_stuff["insanity"] += 10
        insanity_play = random.choice(insanity_sounds)
        insanity_channel.play(insanity_play)
        
        return
    
    



def dots(text):
    print()                              #for the dots at the end of each line in the intro
    game_click_channel.play(click2_sound)
    print(text, end="", flush=True)      #end allows for the dots to be on the same line as the text, flush fixes time.sleep bug in python terminal
    time.sleep(0.75)

    for delay in (0.75, 1, 1.25):         #goes through each timer and adds a dot.
        game_click_channel.play(click2_sound)
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
        print()
        game_print(f'Week {time_stuff["weeks"]}')
        time_stuff["selection mode"] = 1
        time_stuff["insanity"] += 3
        
        return
    else:
        time_stuff["selection mode"] = 0
        
    

def selection():                                        #selection menu that shows up every 7 days.
    if time_stuff["selection mode"] == 1:
        
        if 'Taxation' in researched:
            taxation()
            game_print('Population taxed.')
        
        maintenance_check()
        
        game_print('Choose something')
        
        while True:
            game_print('Build, Research, Other, Help, Save, Leave, Continue')
            selection_choice = input()
            user_click_channel.play(click_sound)
            if selection_choice == 'Continue':
                time_stuff["selection mode"] = 0
                print()
                return
            elif selection_choice == 'Build':
                build()
                
                        
            elif selection_choice == 'Research':
                research()
                
            
            elif selection_choice == 'Other':
                other()
                
            elif selection_choice == 'Help':
                help_func()
                
            elif selection_choice == 'Save':
                save()
                print()
                dots('Saving')
                game_print('Game saved.')
                time.sleep(1)
                print()
                
                
            elif selection_choice == 'Leave':
                dots('')
                game_print('Really? (YES/NO)')
                
                while True:
                    confirmation = input()
                    if confirmation == 'YES':
                        game_print('Coward.')
                        time.sleep(0.5)
                        exit()
                    elif confirmation == 'NO':
                        game_print('Good.')
                        time_stuff["insanity"] += 20
                        time.sleep(1)
                        break
                    else:
                        if time_stuff["insanity"] >= 40:
                            game_print(f'Type correctly, {menu_stuff["name"]}.')
                        else:
                            game_print('Invalid input.')
            
            elif selection_choice == 'Debug':
                debug()
                
        
            else:
                if time_stuff["insanity"] >= 40:
                    game_print('Type correctly, idiot.')
                else:
                    game_print('Invalid input.')

def build():                         #new build menu, much more modular and efficient
    while True:
        print()
        game_print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}')
        print()
        game_print("What would you like to build? ('Exit' to leave)")
        print()
        game_print(available_buildings)
        build_choice = input()
        user_click_channel.play(click_sound)
        
        if build_choice in available_buildings:
            print()
            game_print(f'{building[build_choice]["description"]}   Costs: {building[build_choice]["wood cost"]} wood | {building[build_choice]["gold cost"]} gold | {building[build_choice]["stone cost"]} stone | {building[build_choice]["maintenance"]} gold per week in maintenance | Requires {building[build_choice]["required workers"]} workers')
            
            while True:
                game_print(f'Do you wish to build a {build_choice}? (YES/NO)-')
                confirm = input()
                user_click_channel.play(click_sound)
                
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
                        time.sleep(0.5)
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
                    game_print('Invalid input.')
                
        
        
        
        elif build_choice == "Exit":
            break
        
        else:
            game_print('Invalid input.')

def research():               #research menu
    print()
    game_print(f'Available for Research: {researchables}')
    print()
    
    while True:
        game_print('Choose something to research (Exit to leave).')
        research_selection = input()
        user_click_channel.play(click_sound)
    
        if research_selection in researchables:
            game_print(f' {researchables_dic[research_selection]["gold cost"]} gold. {researchables_dic[research_selection]["description"]}')
            
            while True:
                game_print('Do you wish to research this? (YES/NO)')
                confirm = input()
                user_click_channel.play(click_sound)
        
                if confirm == 'YES':
                    if resources["gold"] >= researchables_dic[research_selection]["gold cost"]:
                        resources["gold"] -= researchables_dic[research_selection]["gold cost"]
                        researched.append(research_selection)
                        researchables.remove(research_selection)
                        building_unlock()
                        time_stuff["insanity"] += 2
                        print()
                        game_print('Research acquired.')
                        print()
                        break
                    
                    elif resources["gold"] < researchables_dic[research_selection]["gold cost"]:
                        game_print('Not enough resources!')
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
    resources["housing"] = 25        #base housing and resource limits, resets to this upon every cycle so buildings don't stack forever
    
    
    
    
    
    resources["food limit"] = 200
    resources["gold limit"] = 50
    resources["wood limit"] = 50
    resources["stone limit"] = 50
    
    
    
    
    for b in buildings:                 #cycles through each building that is a house and adds it to the housing number
        if b == 'Granary':
            resources["food limit"] += building["Granary"]["food storage"]
        elif b == 'Warehouse':
            resources["gold limit"] += building["Warehouse"]["gold storage"]
            resources["wood limit"] += building["Warehouse"]["wood storage"]
            resources["stone limit"] += building["Warehouse"]["stone storage"]
            
    resources["food"] = min(resources["food"], resources["food limit"])
    resources["gold"] = min(resources["gold"], resources["gold limit"])
    resources["wood"] = min(resources["wood"], resources["wood limit"])
    resources["stone"] = min(resources["stone"], resources["stone limit"])
            
            
    
    
    workers()
    
    for x in buildings:
        if "wood gain" in building[x]:
            if "Better Axes" in researched:
                (resources["wood"]) += ((building[x]["wood gain"] * resources["worker ratio"]) * researchables_dic["Better Axes"]["bonus"])
            else:
                resources["wood"] += building[x]["wood gain"] * resources["worker ratio"]
            
        if "gold gain" in building[x]:
            if 'Better Pickaxes' in researched:
                (resources["gold"]) += ((building[x]["gold gain"] * resources["worker ratio"]) * researchables_dic["Better Pickaxes"]["bonus"])
            else:    
                resources["gold"] += building[x]["gold gain"] * resources["worker ratio"]
                
        if "stone gain" in building[x]:
            if 'Better Pickaxes' in researched:
                (resources["stone"]) += ((building[x]["stone gain"] * resources["worker ratio"]) * researchables_dic["Better Pickaxes"]["bonus"])
            else:    
                resources["stone"] += building[x]["stone gain"] * resources["worker ratio"]
                
        if "food gain" in building[x]:
            if 'Irrigation' in researched:
                (resources["food"]) += ((building[x]["food gain"] * resources["worker ratio"]) * researchables_dic["Irrigation"]["bonus"])
            else:    
                resources["food"] += building[x]["food gain"] * resources["worker ratio"]
                
    for build in buildings:                 #cycles through each building that is a house and adds it to the housing number
        if build == 'Housing Estate':
            resources["housing"] += building["Housing Estate"]["housing gain"]
        elif build == 'housing cheat':
            resources["housing"] += building["housing cheat"]["housing gain"]
            

def pop_growth():                       #population growth and decline formula
    pop_hunger = max(1, resources["population"] // 4)
    
    
    if resources["food"] >= pop_hunger:
        resources["food"] -= pop_hunger
        
        growth_multiplier = 1.0
        for b in buildings:
            if "population bonus" in building[b]:
                growth_multiplier *= building[b]["population bonus"]
        
        population_increase = max(1, int((resources["population"] // 10) * growth_multiplier)) 
        resources["population"] += population_increase
        
    else:
        population_decline = max(1, resources["population"] // 3)
        resources["population"] -= population_decline
        
        game_print(f'{population_decline} people died from starvation.')
        
    resources["population"] = min(resources["population"], resources["housing"])
    
def base_gain():            #prevents soft-locks at the start
    if menu_stuff["ismael mode"] == 0:
        resources["gold"] += 1
        resources["stone"] += 1
        resources["wood"] += 1

def death_check():                 #checks for death
    if resources["population"] <= 0:
        game_print("All the population has been wiped out, or just left. All that remains is a ghost town.")
        time.sleep(1)
        print()
        game_print("STATS:")
        game_print(f'Days survived: {time_stuff["days_total"]}')
        print()
        game_print("Game will close in 10 seconds.")
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
            print()
            game_print(f'{events_dic[event_name]["colour"]}{event_name}{RESET}.')
            
            
            effect_channel.play(events_dic[event_name]["sound"])  #plays event sound
            time.sleep(1.5)
            time_stuff["insanity"] += 10
            
            if "pop_loss" in events_dic[event_name]:                                             #dont have to make an if for every event
                lost_pop = max(1, resources["population"] // events_dic[event_name]["pop_loss"])
                resources["population"] -= lost_pop
                game_print(f'You lost {lost_pop} people.')
                
                
def special_event_func():
    for event_name in special_events_list:
        chance = get_special_event_chance(event_name)
        roll = random.randint(1,100)
        
        if roll <= chance:
            print()
            game_print(f'{special_events[event_name]["name"]}:')
            game_print(f'{special_events[event_name]["description"]}')
            print()
            
    
            
            while True:
                game_print('YES/NO')
                confirm = input()
                
                if confirm == 'YES':
                    success = random.randint(1,2)
                    if success == 1:
                        print()
                        game_print(special_events[event_name]["success text"])
                        
                        if "gold increase" in special_events[event_name]:
                            resources["gold"] += special_events[event_name]["gold increase"]
                            game_print(f'You gained {special_events[event_name]["gold increase"]}.') 
                            print()
                            
                        if "pop increase" in special_events[event_name]:
                            resources["population"] += special_events[event_name]["pop increase"]
                            game_print(f'You gained {special_events[event_name]["pop increase"]}.')
                            
                        if "stone increase" in special_events[event_name]:
                            resources["stone"] += special_events[event_name]["stone increase"]
                            game_print(f'You gained {special_events[event_name]["stone increase"]}.')
                            
                        return
                        
                        
            
                    else:
                        print()
                        game_print(special_events[event_name]["loss text"])
                        if "pop_loss" in special_events[event_name]:
                            lost_pop = max(1, resources["population"] // special_events[event_name]["pop_loss"])
                            resources["population"] -= lost_pop
                            time_stuff["insanity"] += 25
                            game_print(f'You lost {lost_pop} people.')
                            print()
                            
                        
                        if "gold_loss" in special_events[event_name]:
                            lost_gold = max(1, resources["gold"] // special_events[event_name]["gold_loss"])
                            resources["gold"] -= lost_gold
                            time_stuff["insanity"] += 25
                            game_print(f'You lost {lost_gold} gold.')
                            print()
                               
                        return
                    
                    
                elif confirm == 'NO':
                    return
                
                else:
                    game_print('Invalid input.')
            
            
def debug():
    print()
    dots('Choose')
    
    
    while True:
        game_print("Set Food, Set Gold, Set Wood, Set Stone, Set Population, Set Housing, Max Resources, Insanity. 'Exit' to leave.")
        print()
        debug_choice = input()
        user_click_channel.play(click_sound)
    
        if debug_choice == 'Set Food':
            while True:
                game_print(f"Set the amount of 'food' you desire.")
                amount_desired = input()
                if amount_desired.isdigit():
                    resources["food"] = int(amount_desired)
                    game_print('Amount set.')
                    print()
                    break
                else:
                    game_print('Invalid input.')
                
            
            
        elif debug_choice == 'Set Gold':
            while True:
                game_print(f"Set the amount of 'gold' you desire.")
                amount_desired = input()
                user_click_channel.play(click_sound)
                if amount_desired.isdigit():
                    resources["gold"] = int(amount_desired)
                    game_print('Amount set.')
                    print()
                    break
                else:
                    game_print('Invalid input.')
            
        elif debug_choice == 'Set Stone':
            while True:
                game_print(f"Set the amount of 'stone' you desire.")
                amount_desired = input()
                user_click_channel.play(click_sound)
                if amount_desired.isdigit():
                    resources["stone"] = int(amount_desired)
                    game_print('Amount set.')
                    print()
                    break
                else:
                    game_print('Invalid input.')
                    
        elif debug_choice == 'Set Population':
            while True:
                game_print(f"Set the amount of 'population' you desire.")
                amount_desired = input()
                if amount_desired.isdigit():
                    resources["population"] = int(amount_desired)
                    game_print('Amount set.')
                    print()
                    break
                else:
                    game_print('Invalid input.')
                    
        elif debug_choice == 'Set Housing':
            while True:
                game_print(f"Set the amount of 'housing' you desire.")
                amount_desired = input()
                user_click_channel.play(click_sound)
                if amount_desired.isdigit():
                    building["housing cheat"]["housing gain"] = int(amount_desired)
                    game_print('Amount set.')
                    print()
                    buildings.append("housing cheat")
                    break
                else:
                    game_print('Invalid input.')
                    
        elif debug_choice == 'Max Resources':
            dots('Granted')
            resources["food"] = 10000000
            resources["gold"] = 10000000
            resources["stone"] = 10000000
            resources["wood"] = 10000000
            
        elif debug_choice == 'Insanity':
            while True:
                game_print(f"Set the amount of 'insanity' you desire.")
                amount_desired = input()
                user_click_channel.play(click_sound)
                if amount_desired.isdigit():
                    time_stuff["insanity"] = int(amount_desired)
                    game_print('Amount set.')
                    print()
                    break
                else:
                    game_print('Invalid input.')
            
        elif debug_choice == 'Exit':
            return
            
        else:
            print('Invalid input.')
            
            
            
def prize_check():     #fixed repeating bug
    if time_stuff["weeks"] == 10 and time_stuff["10 weeks"] == 0:
        dots('Brilliant')
        dots('You have survived 10 weeks')
        dots('Protect your people')
        time_stuff["10 weeks"] = 1
        time_stuff["insanity"] += 10
        time.sleep(2)
        
    elif time_stuff["weeks"] == 20 and time_stuff["20 weeks"] == 0:
        dots('Congratulations')
        dots('You have survived 20 weeks')
        dots('Keep going')
        time_stuff["20 weeks"] = 1
        time_stuff["insanity"] += 20
        time.sleep(2)
        
    elif time_stuff["weeks"] == 50 and time_stuff["50 weeks"] == 0:
        dots('Wow')
        dots('You are')
        game_print('Skilled.')
        time_stuff["50 weeks"] = 1
        time_stuff["insanity"] += 50
        time.sleep(2)
        
    elif time_stuff["weeks"] == 100 and time_stuff["100 weeks"] == 0:
        dots('You have exceeded my expectations greatly')
        game_print('Enjoy')
        game_print('You have received 1000 gold.')
        resources["gold"] += 1000
        time_stuff["100 weeks"] = 1
        time_stuff["insanity"] += 100
        time.sleep(2)
    
def get_event_chance(event_name):                #this makes making research that change event chances extremely easy and efficient
    chance = events_dic[event_name]["chance"]    #just easier this way

    for research in researched:
        modifiers = researchables_dic[research].get("event_modifiers", {})   #.get prevents crashes. basically if event modifiers isnt in the dictionary it wont crash
        chance += modifiers.get(event_name, 0) #if the research changes the event, add modifier, if it doesnt add 0

    return max(0, chance)    #no negatives

def get_special_event_chance(event_name):
    special_chance = special_events[event_name]["chance"]
    
    return max(0, special_chance)





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
        
        
        
        
        
        
def game_print(x):
    print(x)
    game_click_channel.play(click2_sound)
    
    
    
    
def maintenance_check():             #maintenance system
    maintenance_cost = 0             #must reset upon every week
    for build in buildings:            #checks every building and adds its maintenace to the overall
        if "maintenance" in building[build]:
            maintenance_cost += building[build]["maintenance"]
            
    while True:
        print()
        game_print(f'Maintenace for buildings: {maintenance_cost} gold.')
        
        if resources["gold"] >= maintenance_cost:
            game_print('Maintenance cost met.')
            print()
            resources["gold"] -= maintenance_cost
            return
        
        else:
            game_print('Not enough gold!')
            print()
            
            while True:
                game_print(f'Gold: {resources["gold"]} | Gold required: {maintenance_cost}')
                game_print('Sell a building, Sell people, Exit.')
                sell_choice = input()
                user_click_channel.play(click_sound)
                print()
                
                if sell_choice == 'Sell a building':
                    while True:
                        game_print("Choose a building to sell. 'Exit' to leave.")
                        game_print(buildings)
                    
                        building_sell_choice = input()
                        user_click_channel.play(click_sound)
                        
                        if building_sell_choice in buildings:
                            game_print(f'{building_sell_choice} : {building[building_sell_choice]["value"]} value')
                            print()
                            
                            while True:
                                game_print('Do you wish to sell this building? (YES/NO)')
                                sell_confirm = input()
                                
                                if sell_confirm == 'YES':
                                    game_print('Building sold.')
                                    buildings.remove(building_sell_choice)
                                    resources["gold"] += building[building_sell_choice]["value"]
                                    
                                elif sell_confirm == 'NO':
                                    break
                                
                                else:
                                    game_print('Invalid input.')
                                    
                        elif building_sell_choice == 'Exit':
                            print()
                            break
                                    
                        else:
                            game_print('Building does not exist.')
                    
                    
                
                elif sell_choice == 'Sell people':
                    game_print('One person is worth 0.1 gold, so sell in large batches for maximum gold yield.')
                    while True:                                 #death if you sell everything and still haven't reached maintenance quota
                        if resources["population"] <= 0:
                            dots('You sold everyone')
                            death_check()
                        
                        
                        game_print(f'{resources["population"]} people available for sale.')
                        game_print("How many will you sell? ('Exit' to leave)")
                        
                        sell_people = input()
                        user_click_channel.play(click_sound)
                        
                        if sell_people.isdigit() and int(sell_people) <= resources["population"]:  #if sell people is a digit and if sell people itself is greater than or equal to population
                            sell_people = int(sell_people)   #did it this way as I dont want the game to crash if the user inputs regular letters instead of digits
                            while True:
                                if sell_people > 0:
                                    resources["gold"] += 0.1
                                    time_stuff["insanity"] += 1
                                else:
                                    game_print(f'{resources["gold"]} gold   |   {maintenance_cost} maintenance quota')
                                    break
                                sell_people -= 1
                         
                         
                        elif sell_people == 'Exit':
                            break
                         
                         
                        else:
                            game_print('Invalid input.')
                        
                        
                elif sell_choice == 'Exit':
                    break
                    
                    
                
                else:
                    game_print('Invalid input!')
            
            
def workers():
    resources["total workers"] = 0
    
    for y in buildings:            
        if "required workers" in building[y]:
            resources["total workers"] += building[y]["required workers"]
    
    if resources["total workers"] == 0:
        resources["worker ratio"] = 1
    else:
        resources["worker ratio"] = min(1, resources["population"] / resources["total workers"])
        
def taxation():
    taxables = resources["population"]
    
    while True:
        if taxables > 0:
            resources["gold"] += 0.1
        else:
            break
        taxables -= 1
        
def other():
    counting()
    print()
    game_print('Other Menu:')
    print('------------------------------------------------------------------------------------------------------------------------')
    game_print(f'Main Stats: Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}   Workers Required: {resources["total workers"]}')
    game_print(f'Other Stats: Food limit: {resources["food limit"]} | Gold limit: {resources["gold limit"]} | Wood limit: {resources["wood limit"]} | Stone limit: {resources["stone limit"]} | Worker ratio: {resources["worker ratio"]}')
    print('------------------------------------------------------------------------------------------------------------------------')
    print()
    print('------------------------------------------------------------------------------------------------------------------------')
    game_print('Buildings:')
    game_print(f'Food producing buildings: {count["food producing count"]} | Gold producing buildings: {count["gold producing count"]} | Wood producing buildings {count["wood producing count"]} | Stone producing buildings {count["stone producing count"]}')
    print('------------------------------------------------------------------------------------------------------------------------')
    print()
    game_print("Type 'Details' to see a more detailed view of your buildings. Type 'Exit' to leave.")
    
    while True:
        confirm = input()
        print()
        if confirm == 'Details':
            print('------------------------------------------------------------------------------------------------------------------------')
            game_print('Buildings:')
            game_print(f'Farms: {count["farm count"]} | Logging camps: {count["logging camp count"]} | Trading posts: {count["trading post count"]} | Stone mines: {count["stone mine count"]} | Housing estates: {count["housing estate count"]}') 
            game_print(f'Granaries: {count["granary count"]} | Warehouses: {count["warehouse count"]} | Gold mines: {count["gold mine count"]} | Large stone mines: {count["large stone mine count"]} | Pharmacies: {count["pharmacy count"]}')
            print('------------------------------------------------------------------------------------------------------------------------')
            print()
            
            
        elif confirm == 'Exit':
            print()
            return
        else:
            if time_stuff["insanity"] >= 50:
                print('Wrong input, {menu_stuff["name"]}.')
            else:
                print('Invalid input.')
    
    
    
    
    print()
    
def counting(): #what a mess
                                           #basic stats
    count["food producing count"] = 0  #must always reset so stats don't increase forever
    count["stone producing count"] = 0
    count["gold producing count"] = 0
    count["wood producing count"] = 0
    count["other count"] = 0
    
    for x in buildings:
        if "food gain" in building[x]:
            count["food producing count"] += 1
        elif "stone gain" in building[x]:
            count["stone producing count"] += 1
        elif "gold gain" in building[x]:
            count["gold producing count"] += 1
        elif "wood gain" in building[x]:
            count["wood producing count"] += 1
        else:
            count["other count"] += 1
            
            
            
    count["farm count"] = 0                               #detailed stats
    count["stone mine count"] = 0
    count["trading post count"] = 0
    count["logging camp count"] = 0
    count["housing estate count"] = 0
    count["pharmacy count"] = 0
    count["large stone mine count"] = 0
    count["gold mine count"] = 0
    count["granary count"] = 0
    count["warehouse count"] = 0
    
    
    for b in buildings:   #when making a new building, gotta add it to this list so it shows up on the detailed stats screen, otherwise it'll automatically come up in the basic stats 'other' category
        if b == 'Farm':
            count["farm count"] += 1
        elif b == 'Stone Mine':
            count["stone mine count"] += 1
        elif b == 'Trading Post':
            count["trading post count"] += 1
        elif b == 'Logging Camp':
            count["logging camp count"] += 1
        elif b == 'Housing Estate':
            count["housing estate count"] += 1
        elif b == 'Pharmacy':
            count["pharmacy count"] += 1
        elif b == 'Large Stone Mine':
            count["large stone mine count"] += 1
        elif b == 'Gold Mine':
            count["gold mine count"] += 1
        elif b == 'Granary':
            count["granary count"] += 1
        elif b == 'Warehouse':
            count["warehouse count"] += 1


def get_save_path():                                                       #yes i stole the save code and just changed it around, no i dont care
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)                        #gets save path
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "savegame.json")
            
            
def save():                                        #puts all of the current important data into a json
    save_data = {
        "resources": resources,
        "time_stuff": time_stuff,
        "menu_stuff": menu_stuff,
        "buildings": buildings,
        "researched": researched,
        "available_buildings": available_buildings,
    }
    with open(get_save_path(), "w") as f:
        json.dump(save_data, f, indent=2)
        
def load_game():
    path = get_save_path()
    if not os.path.exists(path):
        return False

    with open(path, "r") as f:
        save_data = json.load(f)

    resources.clear()                                    #removes the current stats and replaces them with the ones in the file
    resources.update(save_data["resources"])
    time_stuff.clear()
    time_stuff.update(save_data["time_stuff"])
    menu_stuff.clear()
    menu_stuff.update(save_data["menu_stuff"])

    buildings.clear()
    buildings.extend(save_data["buildings"])
    researched.clear()
    researched.extend(save_data["researched"])
    available_buildings.clear()
    available_buildings.extend(save_data["available_buildings"])

    return True
    
            
            
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
    "10 weeks": 0,
    "20 weeks": 0,
    "50 weeks": 0,
    "100 weeks": 0,
    }



resources = {
    "food": 100,
    "gold": 10,
    "wood": 10,
    "stone": 10,
    "population": 10,
    "housing": 25,
    "worker ratio": 0,
    "total workers": 0,
    "food limit": 200,
    "gold limit": 50,
    "wood limit": 50,
    "stone limit": 50,
    }




building = {               #building dictionary
    "Logging Camp" : {
        "wood gain": 5,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "maintenance": 1,
        "value": 3,
        "required workers": 5,
        "description": "Produces 5 wood per day.",
        },
    "Stone Mine" : {
        "stone gain" : 5,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "maintenance": 1,
        "value": 3,
        "required workers": 5,
        "description": "Produces 5 stone per day.",
        },
    
    "Trading Post" : {
        "gold gain" : 3,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "maintenance": 1,
        "value": 3,
        "required workers": 5,
        "description": "Produces 5 gold per day.",
        },
    
    "Farm" : {
        "food gain" : 5,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 0,
        "maintenance": 1,
        "value": 3,
        "required workers": 5,
        "description": "Produces 5 food per day.",
        },
    
    "Housing Estate" : {
        "housing gain": 25,
        "wood cost": 5,
        "gold cost": 5,
        "stone cost": 2,
        "maintenance": 1,
        "value": 3,
        "required workers": 0,
        "description": "Increases housing by 25.",
        },
    
    "Pharmacy" : {
        "population bonus": 1.05,
        "wood cost": 15,
        "gold cost": 25,
        "stone cost": 20,
        "maintenance": 5,
        "value": 40,
        "required workers": 10,
        "description": "Increases population growth by 5 percent (stacks).",
        },
    
    "Large Stone Mine" : {
        "stone gain" : 15,
        "wood cost": 8,
        "gold cost": 18,
        "stone cost": 15,
        "maintenance": 3,
        "value": 10,
        "required workers": 10,
        "description": "Produces 15 stone per day.",
        },
    
    "Gold Mine" : {
        "gold gain" : 8,
        "wood cost": 25,
        "gold cost": 15,
        "stone cost": 30,
        "maintenance": 2,
        "value": 8,
        "required workers": 10,
        "description": "Produces 8 gold per day.",
        },
    
    "Granary" : {
        "wood cost": 10,
        "gold cost": 5,
        "stone cost": 10,
        "maintenance": 1,
        "value": 5,
        "required workers": 1,
        "food storage": 50,
        "description": "Increases the food storage limit by 50.",
        },
    
    "Warehouse" : {
        "wood cost": 20,
        "gold cost": 10,
        "stone cost": 20,
        "maintenance": 2,
        "value": 10,
        "required workers": 2,
        "wood storage": 25,
        "stone storage": 25,
        "gold storage": 25,
        "description": "Increases the wood, stone and gold storage limit by 25.",
        },
        
    
    "housing cheat" : {
        "housing gain": 0,
        },
    
    }


researchables_dic = {       #research dictionary
    "Storage" : {
        "gold cost": 25,
        "building_unlock": ["Granary", "Warehouse"],
        "description": "Unlocks storage buildings that allow us to store more food, gold, stone and wood.",
        },
    
    
    "Irrigation" : {
        "gold cost": 30,
        "bonus": 1.2,
        "description": "Increases farm output by 20 percent.",
        },
    
    "Better Pickaxes" : {
        "gold cost": 50,
        "bonus": 1.2,
        "description": "Increases mine output by 20 percent.",
        },
    
    "Better Axes" : {
        "gold cost": 40,
        "bonus": 1.2,
        "description": "Increases wood output by 20 percent.",
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
    
    "Flood Barriers" : {
        "gold cost": 20,
        "event_modifiers": {
            "Flood": -3
            },
        "description": "Decreases the chance of a flood occurring",
        },
    
    "Mass Scale Mines" : {
        "gold cost": 125,
        "building_unlock": ["Large Stone Mine", "Gold Mine"],
        "description": "Unlocks the Large Stone Mine and the Gold Mine.",
       },
    
    "Taxation" : {
        "gold cost": 150,
        "description" : "Taxes the population on a weekly basis. Earns 0.1 gold per person.",
        },
    
    }

events_dic = {      
    "Fire": {
        "chance": 10,
        "pop_loss": 10,
        "sound": fire_sound,
        "colour": RED,
        },
    
    "Disease": {
        "chance": 10,
        "pop_loss": 10,
        "sound": cough_sound,
        "colour": GREEN,
        },
    
    "Flood": {
        "chance": 5,
        "pop_loss": 20,
        "sound": flood_sound,
        "colour": BLUE,
        },
    
    }

special_events = {
    "Caving": {
        "name": "Cave Expedition",
        "chance": 1,
        "pop_loss": 5,
        "gold_loss": 25,
        "gold increase": 50,
        "success text": "The expedition was a success, whilst the cave was small, its surface was covered in all sorts of valuable ores.",
        "loss text": "The expedition was a failure, the expedition group got caved in and are still stuck inside.",
        "description": "A group of your people wish to explore an untouched cave system. Perhaps there may be some valuable minerals inside. Do you wish to explore it?",
        "unique": 0
        },
    
    "Refugees": {
        "name": "Fleeing Refugees",
        "chance": 1,
        "pop_loss": 10,
        "gold_loss": 30,
        "gold increase": 10,
        "pop increase" : 25,
        "success text" : "The refugees from the nearby village were extremely grateful for your kindness, and graciously showered you in gifts.",
        "loss text": "The refugee story was a cover for a plan to rob your village, they ransacked a neighbourhood and killed multiple people.",
        "description": "A strange group of refugees have approached your village, they seek refuge here. Will you let them stay here?",
        "unique": 0,
        },
    
    "Ruins": {
        "name": "Old Ruins",
        "chance": 1,
        "pop_loss": 5,
        "gold_loss": 15,
        "gold increase": 5,
        "pop increase": 1,
        "stone increase": 15,
        "success text" : "The expedition group gathered up any useful materials without any trouble, they even brought back a squatter that lived amongst the ruins.",
        "loss text": "Our scout failed to see, or mention that there was a large group of squatters camping out at the ruins, our group was slaughtered.",
        "description": "A young scout has told us that there is a small abandoned ruin nearby. Perhaps there are some useful materials there. Will you send out a group to explore them?",
        "unique": 0,
        },
    
    
    
    }

count = {
    "food producing count": 0,
    "stone producing count": 0,
    "gold producing count": 0,
    "wood producing count": 0,
    "other count": 0,
    "farm count": 0,
    "stone mine count": 0,
    "trading post count": 0,
    "logging camp count": 0,
    "housing estate count": 0,
    "pharmacy count": 0,
    "large stone mine count": 0,
    "gold mine count": 0,
    "granary count": 0,
    "warehouse count": 0,
    }


#lists

buildings = []
available_buildings = ["Logging Camp", "Stone Mine", "Trading Post", "Farm", "Housing Estate"] #starting buildings, new buildings are .appended from a research that adds a building

researchables = ["Irrigation", "Better Pickaxes", "Better Axes", "Wells", "Basic Healthcare", "Mass Scale Mines", "Taxation", "Storage", "Flood Barriers"]
researched = []

events = ["Fire", "Disease", "Flood"]
special_events_list = ["Caving", "Refugees", "Ruins"]

suspicious_names = ["Kirill", "Matthew", "Emmanuel", "Edward", "kirill", "matthew", "emmanuel", "edward",]

insanity_sounds = [breathe1_sound, breathe2_sound, breathe3_sound, bang_sound, knocking_sound]


#game

gamestart()
game_print(f'Starting resources: Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}')
print()
while True:
    death_check()
    time_change()
    resource()
    base_gain()
    pop_growth()
    event()
    special_event_func()
    insanity_check()
    resource_clamp()
    prize_check()
    selection()
    time.sleep(1.5)
    print('------------------------------------------------------------------------------------------------------------------------')
    game_print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}   Housing: {resources["housing"]}   Workers Required: {resources["total workers"]}')
    print()
    
    
    
    
    