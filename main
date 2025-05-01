import requests
import random
import os
import json
def grab_list(Username):
    Url = "https://graphql.anilist.co"
    query = '''
    query($userName: String){
        MediaListCollection(userName: $userName, type: ANIME,status: COMPLETED, sort: FINISHED_ON ){
            user{
                statistics{
                    anime{
                    count
                    meanScore
                    standardDeviation
                    }
                }
            }
            lists{
                entries{
                    score
                    media{
                        title{
                            english
                        }
                        tags{
                        name
                        rank
                        }
                    }
                }
            }
        }
    }
        '''
    variables = {"userName": "coffeee"}
    thingy = requests.post(Url, json ={"query": query, 'variables': variables})
    blah = thingy.json()['data']['MediaListCollection']['lists']
    #print(blah)
    scoretobasedifficultyon = thingy.json()['data']['MediaListCollection']['user']['statistics']['anime']
    #print(scoretobasedifficultyon)
    return blah, scoretobasedifficultyon
loaded = 0
def menu():
    global loaded
    if loaded == 0:
        global duff
        duff = user.load()
        loaded = 1
    #doesnt actually do stuff, just makes sure on start 
    display_page= f'''
    welcome to my anime guessing game!
    1: start thy game 
    2. new user
    3: user settings: {duff}
    4. game config settings
    5: join_multiplayer room( never getting implanted lmao)
    '''
    print(display_page)
    if duff== "no users":
        x = input("no matter what you click your gonna be forced to create a new user lmao\n")
        user.new()
        menu()
        print("you should probably config your settings")
    else:
        try: 
            y = int(input("your choice: "))
        except:
            print("choice 1-6 lmao")
            menu()
        if y ==1:
            game()
        elif y==2:
            user.new()
        elif y==3:
            user.pick()
        elif y==4:
            name.config()
        elif y==5:
            RAAAAAAh
class user:
    def load():
        try:
            file = 'users.json'
            with open(file, 'r') as f:
                global people
                bwah = json.load(f)
                amount = len(bwah['users'])
                people = bwah['users']
                f.close
                return f'{amount} users available'
        except:
            with open('users.json', 'w') as f:
                stuff = {'users':[]}
                json.dump(stuff, f, indent=2)
                f.close
                return "no users"
    def pick():
        try:
            n=1
            for i in people:
                print(f'{n}: {i}')
                n+=1
            choice=int(input("number of person to choose: "))
            thing = str(people[choice - 1])
            with open(thing, 'r') as f:
                ui = json.load(f)
                f.close
            name = ui['name']
            t_guesses =ui['guesses']['total']
            w_guesses = ui['guesses']['wrong']
            c_guesses =ui['guesses']['correct']
            list = ui['list']
            anistats = ui['anistats']
            config = ui['config']
            name = user(name, list, anistats, config, t_guesses, w_guesses, c_guesses)
            global duff
            duff = str(name)
            return duff, menu()
        except:
            print("not a dude bruhh")

    def new():
        name = str(input("name: "))
        name= name
        list = str(input("anilist user: "))
        list, anistats = grab_list(list)
        config = {
                "tags": True,
                "studio": False,
                "director": False,
                "genre": True,
                "format": True,
                "season": False,
                "year": True,
                "episode": True,
                "rating": False,
               }
        file = 'users.json'
        with open(file, 'r') as r:
            stuff = json.load(r)
            inlist = stuff['users']
            r.close
        inlist.append(name)
        print(inlist)
        with open(file, 'w') as f:
            stuff = {"users": inlist}
            json.dump(stuff, f)
            f.close
        with open(name, 'w') as f:
            stuff = {
                "name": name,
                "guesses": {
                    "total": 0,
                    "correct": 0,
                    "wrong": 0,
                    "accuracy": 0
                    },
                "config": config,
                "anistats": anistats,
                "list": list
                }
            json.dump(stuff, f)
            f.close
    def __init__(self, name, list, anistats, config, t_guesses, w_guesses, c_guesses):
        self.name = name
        self.t_guesses = t_guesses
        self.c_guesses = c_guesses
        self.w_guesses = w_guesses
        self.list = list
        self.accuracy = "TBD"
        self.anistats = anistats
        self.config= config

        def update(guesses):
            correct +=1
            total_guesses += guesses
            wrong -= guesses - 1
            return correct, total_guesses, wrong\
        
        def config():
            with open(name, r) as file:
                file.json.load
                config = file['config']
                file.close
            print(f'''
                  [name]'s game config settings
                  configuress what you are given to guess based off of!
                  harder elements
                  1. tags = {config['tags']}
                  2. studio = {config['studio']}
                  3. director = {config['director']}
                  medium elements
                  4. genre = {config['tags']}
                  5. format = {config['format']}
                  6. season = {config['season']}
                  easy elements
                  7. year = {config['year']}
                  8. episode count = {config['episodes']}
                  9. rating = {config['rating']}
                    to format change: 1:true, 3:fale, 4:true...
                    type "back" to go mack to menu 
                  ''')
            change = input("change: ").lower()
            if change == "back":
                return
            else:
                for i in change:
                    if i == int:
                        n = i
                    if n == int:
                        config[n] = i
                        n = "hi"
                    
                    
menu()
