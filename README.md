8 Ball Utilities
================

This repository includes utilities my friends and me use for playing 8 Ball pool.

Features:
* `TeamPicker.py`: Random Team Generator (useful if you have more than 4 players)
* `RatingSystem.py`: Elo rating system for all players
    * `match_history.txt`: `AB vs CD = W L`, where A, B, C and D are initials of players. Before vs is one team and after vs is one team. After = is the game outcome. The first outcome is for Team 1, the second for Team 2. W means win, L means lose.
* `TeamWinrates.py`: Outputs overall winrates, best teams sorted and the best 5 teams sorted.