class Player:
    def __init__(self, info):
        self.name = info["name"]
        self.age = info["age"]
        self.position = info["position"]
        self.team = info["team"]

	

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

playerData=[kevin,jason,kyrie]

newTeam=[]

for data in playerData:
    player = Player(data)
    newTeam.append(player)


for player in newTeam:
    print(player)
    

	
# player_jason = Player(jason)
# player_kevin = Player(kevin)
# player_kyrie = Player(kyrie)


# print(player_jason)
# print(player_kevin)
# print(player_kyrie)

