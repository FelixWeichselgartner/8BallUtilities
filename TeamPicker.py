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

        # remove least from team, noone is playing with/against himself/herself.
        team = [i for i in team if i not in least]
        
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
    min_amount = min(amount)
    indices = [i for i, x in enumerate(amount) if x == min_amount]
    selected_indices = random.sample(indices, min(4, len(indices)))
    selected_players = [teammates[i] for i in selected_indices]
    return selected_players


def check_duplicates(lst):
    for item in lst:
        if lst.count(item) > 1:
            return True
    return False


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
        if check_duplicates(oneteam):
            print('error in code')
            exit()
        random.shuffle(oneteam)
        print(f'{oneteam[0]}, {oneteam[1]} vs {oneteam[2]}, {oneteam[3]}')


gen_all_teams()
