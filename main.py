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
                        name
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
                                    format
                                    season
                                    seasonYear
                                    episodes
                                    genres
                                    averageScore
                                    studios{
                                        edges{
                                            isMain
                                            node{
                                                name
                                            }
                                        }
                                    }
                                    staff{
                                        edges{
                                        role
                                            node{
                                                name{
                                                    full
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                    '''
                variables = {"userName": "coffeee"}
                thingy = requests.post(Url, json ={"query": query, 'variables': variables})
                user_list = thingy.json()['data']['MediaListCollection']['lists']
                print(user_list)
                anistats = thingy.json()['data']['MediaListCollection']['user']['statistics']['anime']
                #print(scoretobasedifficultyon)
                return user_list, anistats

               
            def load():
                try:
                    file = 'users.json'
                    with open(file, 'r') as f:
                        bwah = json.load(f)
                        global people
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
                print(self.name)
                try:
                    with open(self.name, 'r') as r:
                        file = json.load(r)
                        config = file["config"]
                    print(f'''
{self.name}'s game config settings
configuress what you are given to guess based off of!
harder elements
1. tags = {config['tags']}
2. studio = {config['studios']}
3. staff = {config['staff']}
medium elements
4. genre = {config['genres']}
5. format = {config['format']}
6. season = {config['season']}
easy elements
7. year = {config['seasonYear']}
8. episode count = {config['episodes']}
9. rating on anilist = {config['averageScore']}
  type "back" to go mack to menu 
                        ''')                    
                    try:
                        choice = int(input("# of option: "))
                        change = str(input("T or F only: ")).lower()
                        if change == 't':
                            change = True
                        elif change =='f':
                            change = False
                        
                        elif change == 'back':
                            return
                        n=0
                        for i in config:
                            n+=1
                            if n == choice:
                                config[i] = change
                            else:
                                continue
                        file['config'] = config
                        with open(self.name, 'w') as f:
                            json.dump(file, f)
                        try:
                            again = int(input("1. configure something else? \n2.leave?"))
                            if again == 1:
                                config()
                            elif again ==2:
                                menu()
                        except:
                            print("ok to menu you go since you didnt type 1 or 2")
                            return
                        
                    except:
                        print("please type an int and t,f, or back")
                        config()
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
                        "studios": False,
                        "staff": False,
                        "genres": True,
                        "format": True,
                        "season": False,
                        "seasonYear": True,
                        "episodes": True,
                        "averageScore": False,
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
                    self.name = ui['name']
                    self.t_guesses =ui['guesses']['total']
                    self.w_guesses = ui['guesses']['wrong']
                    self.c_guesses =ui['guesses']['correct']
                    self.list = ui['list']
                    self.anistats = ui['anistats']
                    self.config = ui['config']
                    self.currentUser = ui['name']
                    self.choose_user= True
                    load()
                    return
                except:
                    print("not a dude bruhh")
            def save():
                    with open(self.name, 'w') as file:
                        gather = {
                                "guesses": {
                                "total": self.t_guesses,
                                "correct": self.c_guesses,
                                "wrong": self.w_guesses,
                                "accuracy": self.t_guesses / self.w_guesses
                             },
                         "config": self.config,
                         "anistats": self.anistats,
                         "list": self.list
                         }
                        json.dump(gather, file, index=2)
                    return
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
                        return
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


def get_animepool(player_list):
    animepool = []
    player_list= player_list['entries']
    total = len(player_list)
    while len(animepool) < 5:
        anime_number = random.randint(0,total)
        if anime_number in animepool:
            continue
        else:
            animepool.append(player_list[anime_number])
    return animepool
def question(current_anime, config):
    for setting in config:
        if config[setting] == True:
            try:
                if setting == 'tags':
                    for tag in current_anime['media']['tags']:
                        if tag['rank'] >= 80:
                            print(f'{tag['name']}: {tag['rank']}%')
                        else:
                            break
                elif setting == 'studios':
                    for studio in current_anime['media']['studios']['edges']:
                        print(studio)
                else:
                    print(f'{setting}: {current_anime['media'][setting]}')
            except:
                print(f'{setting}: {current_anime[setting]}')
    Anime_blanked = ""
    anime_name = current_anime['media']['title']['english'].lower()
    for i in anime_name:
        if i == " ":
            Anime_blanked += i
        else:
            Anime_blanked += "_"
    print(Anime_blanked)
    print(current_anime['media']['title']['english'])
    guess = "idk"
    guesses = 0
    while guess != anime_name:
        guesses += 1
        guess = input("guess?: ").lower()
        if guess == anime_name:
            return guesses
            continue
        else:
            print('try again')
    print("you got it!")
        
    #question_number+=1
    return







def __main__():
    running = True
    while running == True:
        player = user()
        animepool = get_animepool(player.list[0])
        print(len(animepool))
        score = 0
        for anime in animepool:
            score = question(anime, player.config)
            player.t_guesses +=score
            player.w_guesses += score - 1
            player.c_guesses += 1
            player.save()
if __name__== "__main__":
    __main__()
