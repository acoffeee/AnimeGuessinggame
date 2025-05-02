import requests
import random
import os
import json

class user:
        def __init__(self):
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
            def config():
                try:
                    with open(self.name, 'r') as r:
                        file = json.load(r)
                        config = file['config']
                    print(f'''
                          {self.name}'s game config settings
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
                except:
                    print("come back when youve loaded a user")
                    return
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
                    self.name = ui['name']
                    self.t_guesses =ui['guesses']['total']
                    self.w_guesses = ui['guesses']['wrong']
                    self.c_guesses =ui['guesses']['correct']
                    self.list = ui['list']
                    self.anistats = ui['anistats']
                    self.config = ui['config']
                    self.currentUser = ui['name']
                    self.choose_user=True
                    load()
                    return
                except:
                    print("not a dude bruhh")
            def menu():
                display_page = f'''
                welcome to my anime guessing game!
                1: start thy game 
                2. new user
                3: Loaded user(s): {self.currentUser}
                4. game config settings
                5: join_multiplayer room( never getting implanted lmao)
            '''
                print(display_page)
                if self.currentUser== "no users":
                    x = input("no matter what you click your gonna be forced to create a new user lmao\n")
                    new()
                    print("you should probably config your settings")
                else:
                    try: 
                        y = int(input("your choice: "))
                    except:
                        print("choice 1-6 lmao")
                        menu()
                    if y ==1:
                        #place
                        pass
                    elif y==2:
                        new()
                    elif y==3:
                        pick()
                    elif y==4:
                        config()
                    elif y==5:
                        #place
                        pass         
            x = True
            while x == True:
                try: 
                    if self.choose_user == True:
                        menu()
                        break
                    else:
                        self.currentUser=load()
                        menu()
                except: 
                    self.currentUser=load()
                    menu()
            
            def update(guesses):
                correct +=1
                total_guesses += guesses
                wrong -= guesses - 1

if __name__== "__main__":
    ok = user()
