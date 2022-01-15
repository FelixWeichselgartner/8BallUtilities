import math

def probability(r1, r2):
    return (1.0/(1.0 + math.pow(10, ((r2 - r1)/400))))


def updateRating(rating, win, p):
    K = 30
    new_rating = rating + K * (win - p)
    return new_rating


def EloRating(r1, r2, win):
    winp1 = None
    winp2 = None

    if win == 0:
        winp1 = 1
        winp2 = 0
    else:
        winp1 = 0
        winp2 = 1

    p1 = probability(r1, r2)
    p2 = probability(r2, r1)
    # print(f"p1 = {p1}, p2 = {p2}, p1+p2 = {p1+p2}\n", p1, p2, p1+p2)
    r1n = updateRating(r1, winp1, p1)
    r2n = updateRating(r2, winp2, p2)

    return r1n, r2n


def test():
    ratingPlayer1 = 1000
    ratingPlayer2 = 1000

    while True:
        winner = input("who is the winner?:\n0 = player1, 1 = player2?: ")
        ratingPlayer1, ratingPlayer2 = EloRating(ratingPlayer1, ratingPlayer2, winner)
        print(f"player1's new rating is {ratingPlayer1}\n")
        print(f"player2's new rating is {ratingPlayer2}\n")

if __name__ == "__main__":
    test()
