import datetime
import time
from paypal_me import paypal_me_url


players = {
    'Basti': '20:15-21:41',
    'Dani': '18:46-21:41',
    'Felix': '18:46-21:41',
    'Toni': '18:46-21:41',
}

# 10 percent tip
bill = 36.8 * 1.1

player_list = players.keys()
player_time = {}

overall_time = datetime.timedelta()

for p in player_list:
    s, e = players[p].split('-')
    start = datetime.datetime.strptime(s, '%H:%M').time()
    end = datetime.datetime.strptime(e, '%H:%M').time()
    delta = datetime.datetime.combine(datetime.date.today(), end) - datetime.datetime.combine(datetime.date.today(), start)
    overall_time += delta
    player_time[p] = delta

bill_sum = 0

for p in player_list:
    b = round(player_time[p] / overall_time * bill, 2)
    bill_sum += b
    print(f'{p} {players[p]}: {paypal_me_url}/{b}')

print(f'Felix bleibt auf so viel sitzen: {round(bill_sum - bill, 2)}')
