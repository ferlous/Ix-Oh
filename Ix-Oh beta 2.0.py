import itertools

won = False


def aquire_game_length():  # gets the game's size
    game_length_not_set = True
    while game_length_not_set:
        global game_length
        try:
            game_length = int(
                input("what is the game\'s size (betwen 2 and 10) "))
            assert (1 < game_length < 11)
        except AssertionError:
            print('hey! you must write a number betwen 2 and 10')
        except:
            print('hey! you must write a number')
        else:
            game_length_not_set = False


def gamebord_creation():  # create the gamebord
    aquire_game_length()
    global gamebord
    gamebord = []
    for i in range(game_length):
        gamebord.append([])
        for row in range(game_length):
            gamebord[i].append(" ")


def gamebord_display():  # displys the gamebord
    print("   "+"   ".join([str(i)for i in range(game_length)]))
    print("")
    counter = 0
    for row in gamebord:
        print(counter, "", "   ".join([str(i)for i in row]))
        counter += 1
        print("")


def play():  # takes the input from the user to play the game
    e = True
    while e:
        try:
            row = int(
                input("what row wold you play (between 0 and "+str(game_length-1)+') '))
            assert (-1 < row < game_length)
        except AssertionError:
            print("the number must be between 0 and ", (game_length-1))
        except:
            print("you must enter a number")
        else:
            e = False
    e = True
    while e:
        try:
            col = int(
                input("what column wold you play (between 0 and "+str(game_length-1)+') '))
            assert (-1 < col < game_length)
        except AssertionError:
            print("the number must be between 0 and ", (game_length-1))
        except:
            print("you must enter a number")
        else:
            e = False
    return row, col


def playing():
    won = False
    e = True
    while e:
        current_player = next(player)
        try:
            row, col = play()
            assert (gamebord[row][col] == " ")
            gamebord[row][col] = current_player
        except AssertionError:
            print("sorry but some one alrady played there")
        else:
            e = False
    gamebord_display()
    # horizontal win
    for i in gamebord:
        if ((([i[0]]*game_length) == i)and(i[0] != " ")):
            print('the player', current_player, ' won')
            won = True
    return won


while True:
    gamebord_creation()
    gamebord_display()
    global player
    player = itertools.cycle([1, 2])
    while not won:
        won = playing()
    quiting_or_replaying = input("would you like to replay(y or n) ")
    if (quiting_or_replaying == "y"):
        won = False
    else:
        quit()
