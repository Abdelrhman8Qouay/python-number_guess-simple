import random


list_scores = []

# get scores of your game function
def curScore():
    if not list_scores:
        print("There's is no score Yet\n")
    else:
        print(f"Your last high score of game.. {min(list_scores)}\n")


# the game will start here
def startGame():
    # options
    end = 5
    randomTrueNum = random.randint(10, 20)
    attempts = 0

    # you want to continue
    wanna_continue = input("do you want to play the game? Enter(Yes/No): ")
    if wanna_continue.lower() == "no":
        print("Okay, Goodbye.")
        exit()
    elif wanna_continue.lower() == "yes":
        curScore()
    else:
        print("i can't understand, Open and try again")
        exit()

    while end >= 1:
        # continue to the game
        try:
            print(f"the rest of life: {end}")
            choice = int(input("what's your choice of number range from 10 to 20: "))

            if choice == randomTrueNum:
                list_scores.append(attempts)
                print("Yaaay good job, your choice is true and the number equal the random\nDon't forget us soon")

                # ask the user again if want play
                wanna_continue = input("Do you want to play Again? Enter(Yes/No): ")
                if wanna_continue.lower() == "no":
                    print("Okay, Goodbye.")
                    break
                elif wanna_continue.lower() == "yes":
                    print("Okay let's go, be ready")
                    end = 5
                    attempts = 0
                    randomTrueNum = random.randint(10, 20)
                    curScore()
                    continue
                else:
                    print("i can't understand, Open and try again")
                    break

            elif choice < 10 or choice > 20:
                print("you are out of range, Please make your number in range")

            else:
                attempts += 1
                end -= 1
                if choice > randomTrueNum:
                    print("Less than that ^_^")
                elif choice < randomTrueNum:
                    print("Bigger than that ^_^")

        except :
            pass

    else:
        print("oooh.. am sorry, but your life now ended for trying..\nComing soon")
        # ask the user again if want play
        wanna_continue = input("Do you want to play Again? Enter(Yes/No): ")
        if wanna_continue.lower() == "no":
            print("Okay, Goodbye.")
            exit()
        elif wanna_continue.lower() == "yes":
            print("Okay let's go, be ready")
            attempts = 0
            end = 5
            randomTrueNum = random.randint(10, 20)
            curScore()
            startGame()
        else:
            print("i can't understand, Open and try again")
            exit()



# you are welcome here  (first lines)
print("\n\nWelcome In The First Project\tWith Number Guessing Game.")
print("we will start with the game and your range from 10 to 20", end=", ")
print("also you have a limit for trying your choices.. life of attempts (5) only and game over\nlet's begin")

if __name__ == '__main__':
    startGame()
