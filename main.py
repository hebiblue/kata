import random
import numpy as np
import pandas as pd

def findChampions(age, elo, players):

    players_infos = pd.DataFrame({  'Player_name': players,
                                'Age' : age,
                                'Elo' : elo})

    champions = players_infos.sort_values(['Elo','Age'], ascending = [False, True], ignore_index = True)

    print(champions)
    print('\n' 'Le champion est: ' , champions['Player_name'].iloc[0])

age = np.random.randint(18,61,10)
elo = np.random.randint(10,101,10)
players = ['Leonard Mclaughlin', 'Joyce Mihaly', 'Jack Hollis', 'Carolina Crockett', 'Mary Paquet', 'Olga Stewart', 'Jan Gomez', 'Linda Henning', 'Brenda Wallace', 'Christopher Shannon']
# age = [1, 10, 12]
# elo = [23, 44, 56]
# players = ['Anael', 'Romy', 'John']

findChampions(age, elo, players)

