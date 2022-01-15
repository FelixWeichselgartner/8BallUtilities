import random

teammates = ['Eva', 'Lukas', 'Dani', 'Toni', 'Felix']

def gen_team():
    global teammates
    n = random.randint(0, 4)
    team = teammates.copy()
    out_for_this_round = team.pop(n)
    return team

def gen_all_teams():
    amount = list([0, 0, 0, 0, 0])
    all_teams = list()
    for i in range(25):
        all_teams.append(gen_team())

    for thisteam in all_teams:
        for p in thisteam:
            for i in range(len(teammates)):
                if p == teammates[i]:
                    amount[i] += 1

    if amount[0] == amount[1] == amount[2] == amount[3] == amount[4]:
        print(teammates)
        print(amount)
        print('===================')
        print()
        for i in range(25):
            oneteam = all_teams[i].copy()
            random.shuffle(oneteam)
            print(f'{oneteam[0]}, {oneteam[1]} vs {oneteam[2]}, {oneteam[3]}')
        exit()

while True:
    gen_all_teams()
