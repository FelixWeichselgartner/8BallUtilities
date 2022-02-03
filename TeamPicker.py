import random

teammates = ['Eva', 'Lukas', 'Dani', 'Toni', 'Felix']

def gen_team():
    global teammates
    team = teammates.copy()
    while len(team) > 4:
        n = random.randint(0, len(teammates) - 1)
        out_for_this_round = team.pop(n)
    return team

amount_of_games = len(teammates)**2

def gen_all_teams():
    amount = list([0] * len(teammates))
    all_teams = list()
    for i in range(amount_of_games):
        all_teams.append(gen_team())

    for thisteam in all_teams:
        for p in thisteam:
            for i in range(len(teammates)):
                if p == teammates[i]:
                    amount[i] += 1
    
    same_amount = True
    value = amount[0]
    for i in range(1, len(teammates)):
        same_amount = same_amount and (value == amount[i])

    if same_amount:
        print(teammates)
        print(amount)
        print('===================')
        print()
        for i in range(amount_of_games):
            oneteam = all_teams[i].copy()
            random.shuffle(oneteam)
            print(f'{oneteam[0]}, {oneteam[1]} vs {oneteam[2]}, {oneteam[3]}')
        exit()

while True:
    gen_all_teams()
