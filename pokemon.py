Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying",),
"Lapras": ("Water", "Ice",),
"Mewtwo": ("Psychic", "Fighting",),
"Lugia": ("Psychic", "Flying", "Water",),
"Onix": ("Rock", "Ground",)
}
from itertools import combinations

pokemons = ["Pikachu", "Charizard", "Lapras","Mewtwo","Lugia","Onix"]
max_types = 0
good_teams=[]
for teams in combinations(pokemons, 3):
    teams_type = set()
    for s in teams:
        teams_type.update(Pokedex[s])
    #print(teams,"=",teams_type)
    if len(teams_type) > max_types:
        max_types = len(teams_type) 
        good_teams=[(teams,teams_type)]
    elif len(teams_type)==max(teams_type):
        good_teams.append((teams, teams_type))
print("The strongest team is : \n",good_teams)
#print(max_types)#this will print the number of types the good team has which is 6