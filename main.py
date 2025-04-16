import requests
import random
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
    print(blah)
    scoretobasedifficultyon = thingy.json()['data']['MediaListCollection']['user']['statistics']['anime']
    print(scoretobasedifficultyon)
    return blah, scoretobasedifficultyon
Username = "Coffeee"
thing, avgscore = grab_list(Username)
running = False
#avgscore is purely the users average socore + count
def start_game():
    try:
        thingymabobber = str(input)
        if "ye" or "start" in thingymabobber:
            running = True
        elif "no" or "stop" in thingymabobber:
            x = str(input("ok tbh you dont really have a choice and like this script isnt gonna get more games so see ya i guess maybe ill add a save option"))
            running = False
    except:
        print("make sure to include something like yes or no lol start and stop also work and maybe stuff that starts with ye")
animepool = []
n=0
upper_echoleon = avgscore['meanScore'] + avgscore['standardDeviation']
lower_echoleon = avgscore['meanScore'] - avgscore['standardDeviation']
upper_echoleon = upper_echoleon / 10
lower_echoleon = lower_echoleon / 10
lower_echoleon = round(lower_echoleon, 1)
upper_echoleon = round(upper_echoleon, 1)
n = 0
def based_anime_count():
    if avgscore['count'] >= 200:
        a = 37
        b = 73
        c = 100
        return a, b, c
    else:
        a = avgscore['count'] * 0.33
        a = round(a, 0)
        b = avgscore['count'] * 0.66
        b = round(b, 0)
        c = avgscore['count']
        return a, b, c
easy, mid, hard = based_anime_count()
def easy_difficulty(): 
    n = 0
    for i in thing:
        if n<= easy:
            animepool.append(i)
            n+=1
            continue
        if i['score'] >= upper_echoleon:
            animepool.append(i)
        else:
            break
def mid_difficulty(): 
    n = 0
    for i in thing:
        if n<= mid:
            animepool.append(i)
            n+=1
            continue
        if i['score'] <= upper_echoleon and i['score'] >= lower_echoleon:
            animepool.append(i)
        elif i['score'] <= lower_echoleon:
            break
def hard_difficulty(): 
    n = 0
    for i in thing:
        if n<= hard:
            animepool.append(i)
            n+=1
            continue
        if i['score'] <= upper_echoleon:
            animepool.append(i)
def game_difficulty():
    try:
        thing2 = str(input("What difficulty do you want? theres easy, medium, hard, and extreme: \n")).lower()
        if thing2 == "easy":
            easy_difficulty()
        elif thing2 == "medium":
            mid_difficulty()
        elif thing2 == "hard":
            hard_difficulty()
    except:
        print("bruh thats not a difficulty or not in yet")
#bruh that was only the logic to decide what animes would be condier? bruhh
def oknowtheactualguesspartihavennocludewtfimdoingimissai():
    Bwomp = len(animepool)
    BWOMPBWOMP=random.randrange(0, Bwomp)
    print(animepool['entries'])
game_difficulty()
oknowtheactualguesspartihavennocludewtfimdoingimissai()
