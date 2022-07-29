from Elo import EloRating


players = {

}


with open('match_history.txt') as history:
    match_counter = 1
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

        team1 = b[0]
        player1 = team1[0]
        player2 = team1[1]
        outcome1 = c[0]
        team2 = b[1]
        player3 = team2[0]
        player4 = team2[1]
        outcome2 = c[1].replace('\n', '')

        myplayers = [player1, player2, player3, player4]

        for p in myplayers:
            if (p not in players.keys()):
                players[p] = 1000

        # I do not have an algorithm for 2 vs 2 games
        # So I will just use:
        # Player1 vs Player 3
        # Player1 vs Player 4
        # Player2 vs Player 3
        # Player2 vs Player 4
        # with the match outcome for Team 1 vs Team 2.

        # EloRating(ratingPlayer1, ratingPlayer2, winner)
        # winner 0, if team 1 won the game
        # winner 1, if team 2 won the game

        # team 1 won if outcome1 = W and outcome2 = L

        old_player1 = players[player1]
        old_player2 = players[player2]
        old_player3 = players[player3]
        old_player4 = players[player4]

        temp1, temp3 = EloRating(old_player1, old_player3, 0 if outcome1 == 'W' and outcome2 == 'L' else 1)
        delta1 = temp1 - old_player1
        delta3 = temp3 - old_player3
        temp1, temp4 = EloRating(old_player1, old_player4, 0 if outcome1 == 'W' and outcome2 == 'L' else 1)
        delta1 += temp1 - old_player1
        delta4 = temp4 - old_player4
        temp2, temp3 = EloRating(old_player2, old_player3, 0 if outcome1 == 'W' and outcome2 == 'L' else 1)
        delta2 = temp2 - old_player2
        delta3 += temp3 - old_player3
        temp2, temp4= EloRating(old_player2, old_player4, 0 if outcome1 == 'W' and outcome2 == 'L' else 1)
        delta2 += temp2 - old_player2
        delta4 += temp4 - old_player4


        # Toni mode
        # for less frustration
        # on average win more than you lose
        # set this on 1 for normal behaviour
        factor = 0.9
        if delta1 < 0:
            delta1 = delta1 * factor
        if delta2 < 0:
            delta2 = delta2 * factor
        if delta3 < 0:
            delta3 = delta3 * factor
        if delta4 < 0:
            delta4 = delta4 * factor


        players[player1] += delta1
        players[player2] += delta2
        players[player3] += delta3
        players[player4] += delta4

        line = h.replace('\n', '')
        print(f'After Match {match_counter} with {line} player ratings are:')
        print(players)

        match_counter += 1

print('==================')
for i in players.keys():
    players[i] = int(players[i])
print()
print(f'After Match {match_counter} with {line} player ratings are:')
print(players)
