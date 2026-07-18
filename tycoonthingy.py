import random
import time



def gamestart():
    print('Welcome to this text-based citybuilder!')
    print()

def time_change():
    time_stuff["days"] += 1
    
    if time_stuff["days"] == 7:
        time_stuff["days"] = 0
        time_stuff["weeks"] += 1
        print(f'Week {time_stuff["weeks"]}')
        time_stuff["selection mode"] = 1
        
        return
    else:
        time_stuff["selection mode"] = 0
        
    

def selection():
    if time_stuff["selection mode"] == 1:
        print('Choose something.')
        
        while True:
            selection_choice = input('Build, Continue.')
            if selection_choice == 'Continue':
                selection_choice = 0
                return
            elif selection_choice == 'Build':
                while True:
                    print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}')
                    print('What would you like to build?')
                    build_choice = input('Logging Camp, Stone Mine, Trading Post, Farm or Exit.')
                    
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
                    
                    elif build_choice == "Exit":
                        break
                    
                    else:
                        print('Invalid input.')
        
            else:
                print('Invalid input.')
                
            
def resource():
    for x in buildings:
        if "wood gain" in building[x]:
            resources["wood"] += building[x]["wood gain"]
        if "gold gain" in building[x]:
            resources["gold"] += building[x]["gold gain"]
        if "stone gain" in building[x]:
            resources["stone"] += building[x]["stone gain"]
        if "food gain" in building[x]:
            resources["food"] += building[x]["food gain"]

def pop_growth():
    if resources["food"] > 0:
        population_increase = resources["population"] // 10
        resources["population"] += population_increase
    else:
        population_decline = resources["population"] // 7
        resources["population"] -= population_decline
        
    pop_hunger = resources["population"] // 4
    resources["food"] -= pop_hunger

time_stuff = {
    "days": 0,
    "weeks": 0,
    "selection mode": 0,
    }



resources = {
    "food": 100,
    "gold": 10,
    "wood": 10,
    "stone": 10,
    "population": 10,
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
    
    }

buildings = []


gamestart()
while True:
    time_change()
    resource()
    pop_growth()
    selection()
    time.sleep(1.5)
    print(f'Food: {resources["food"]}   Gold: {resources["gold"]}   Wood: {resources["wood"]}   Stone: {resources["stone"]}   Population: {resources["population"]}')
    
    
    
    
    
    