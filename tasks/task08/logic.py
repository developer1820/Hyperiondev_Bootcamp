import random

opponent_age = 0
participant_win = 0
opponent_win = 0

"""
Below in input user should enter age between (15 to 50) but user can enter
    any age below 15 or higher than 50,
which then interfere with rest of the while loop and answer can not be as
    expected, so its a logical error.
so to avoid having these kind of scenario we should use error handling
    method (try, except).
"""
while True:
    participant_age = int(input("Please enter participants age\
    (eligible age between (15 to 50)):"))
    opponent_age = random.randint(15, 50)
    print("opponent_age is:", opponent_age)

    if participant_age > opponent_age:
        print("Its participant chance to pick a player.")
        participant_win += 1
        print("participant total win:", participant_win)
    elif opponent_age > participant_age:
        print("Its opponent chance to pick a player.")
        participant_win += 1
        print("opponent total win:", opponent_win)


# Here instead of (participant_win +=1), (opponent_win +=1) should be there,
# because it increases participant win instead of opponent win,
# so its a logical error.

    else:
        print("Sorry, its a draw.")

    if participant_win == 5:
        print("-"*100)
        print("Participant won the game!!".upper())
    elif opponent_win == 5:
        print("-"*100)
        print("Opponent won the game!!".upper())
        break
