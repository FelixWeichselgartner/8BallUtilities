import random


teammates = ['Eva', 'Lukas', 'Dani', 'Toni', 'Felix', 'Manu', 'Johanna', 'Laura', 'Lisa', 'Jakob', 'Simon', 'Lohbi', 'Basti']
random.shuffle(teammates)

individual_games = 8
amount_of_games = len(teammates) * individual_games / 4
amount_of_games_int = int(amount_of_games)
while amount_of_games != float(amount_of_games_int):
    individual_games += 1
    amount_of_games = len(teammates) * individual_games / 4
    amount_of_games_int = int(amount_of_games)
amount_of_games = amount_of_games_int

print(f'creating {amount_of_games} games')


def gen_team(least):
    global teammates
    team = teammates.copy()

    if least != None:
        if len(least) == 4:
            return least
        
        while len(team) > 4 - len(least):
            n = random.randint(0, len(team) - 1)
            out_for_this_round = team.pop(n)
        return team + least
    else:      
        while len(team) > 4:
            n = random.randint(0, len(team) - 1)
            out_for_this_round = team.pop(n)
        return team


def find_least_selected_players(amount):
    indices = [i for i, x in enumerate(amount) if x == min(amount)]
    random.shuffle(indices)
    selected_indices = indices[:4]
    selected_players = list()
    for s in selected_indices:
        selected_players.append(teammates[s])
    return selected_players


def gen_all_teams():
    amount = list([0] * len(teammates))
    all_teams = list()
    least = None
    for i in range(amount_of_games):
        new_team = gen_team(least)
        random.shuffle(new_team)
        for p in new_team:
            for i in range(len(teammates)):
                if p == teammates[i]:
                    amount[i] += 1
        all_teams.append(new_team)
        least = find_least_selected_players(amount)

    print(teammates)
    print(amount)
    print('===================')
    print()
    for i in range(amount_of_games):
        oneteam = all_teams[i].copy()
        random.shuffle(oneteam)
        print(f'{oneteam[0]}, {oneteam[1]} vs {oneteam[2]}, {oneteam[3]}')


gen_all_teams()
