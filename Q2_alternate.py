import random

def game():
    print("You are playing the game")

    score = random.randint(1, 65)

    # Read high score
    try:
        with open("hiscore.txt", "r") as f:
            hiscore = f.read()
            if hiscore == "":
                hiscore = 0
            else:
                hiscore = int(hiscore)
    except FileNotFoundError:
        hiscore = 0

    print("Your score is:", score)
    print("High score is:", hiscore)

    # Update high score
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
        print("New High Score!")

game()
