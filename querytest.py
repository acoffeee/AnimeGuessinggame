import requests
import os
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
                ok = thingy.json()
                print(ok)
                thing = 
                stats = thingy.json()['data']['MediaListCollection']['user']['statistics']['anime']
                #print(scoretobasedifficultyon)
grab_list("zylda")