import itertools


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
            gamebord[i].append(0)


gamebord_creation()


def gamebord_display():  # displys the gamebord
    print("   "+"  ".join([str(i)for i in range(game_length)]))
    counter = 0
    for row in gamebord:
        print(counter, row)
        counter += 1


gamebord_display()
error_text1 = 0


def play():
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


def game_play():
    still_playing = True
    player = itertools.cycle([1, 2])
    while still_playing:
        row, col = play()
        gamebord[row][col] = next(player)
        if gamebord[row][col]==1:
            gamebord[row][col]='x'
        else:
            gamebord[row][col]='0'
        gamebord_display()


game_play()
