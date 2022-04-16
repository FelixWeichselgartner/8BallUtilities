
teams = {

}

all_teams = list()


with open('match_history.txt') as history:
    for h in history:
        if (h == "" or h == "\n"):
            continue

        try:
            a = h.split(' = ')
        except:
            print('error in match history file')
            exit()
        
        b = a[0].split(' vs ')
        c = a[1].split(' ')

        # b[0] -> Team 1
        # b[1] -> Team 2
        # c[0] -> Match outcome for Team 1
        # c[1] -> Match outcome for Team 2

        team1 = list(sorted(b[0]))
        team1 = team1[0] + team1[1]
        outcome1 = c[0]
        team2 = list(sorted(b[1]))
        team2 = team2[0] + team2[1]
        outcome2 = c[1].replace('\n', '')

        if team1 not in all_teams:
            all_teams.append(team1)

        if team2 not in all_teams:
            all_teams.append(team2)

        if outcome1 == 'W' and outcome2 == 'L':
            try:
                teams[team1 + '_W'] += 1
            except KeyError:
                teams[team1 + '_W'] = 1
            
            try:
                teams[team2 + '_L'] += 1
            except KeyError:
                teams[team2 + '_L'] = 1
        elif outcome1 == 'L' and outcome2 == 'W':
            try:
                teams[team1 + '_L'] += 1
            except KeyError:
                teams[team1 + '_L'] = 1
            
            try:
                teams[team2 + '_W'] += 1
            except KeyError:
                teams[team2 + '_W'] = 1

winrates = dict()

for t in all_teams:
    if t + '_W' not in teams.keys():
        teams[t + '_W'] = 0
    
    if t + '_L' not in teams.keys():
        teams[t + '_L'] = 0
    

for t in all_teams:
    if (teams[t + '_W'] + teams[t + '_L']) > 0:
        winrates[t] = round(float(teams[t + '_W']) / (teams[t + '_W'] + teams[t + '_L']) * 100)

print(winrates)

marklist = list(sorted(winrates.items(), key=lambda x:x[1]))
sortdict = dict(list(reversed(marklist)))
print(sortdict)

best_5_teams = dict(list(reversed(marklist))[0:5])
print('Best 5 teams after winrate are:')
i = 1
for b in best_5_teams:
    print(f'{i}: {b} with {best_5_teams[b]}%')
    i += 1
