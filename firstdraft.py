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


def gamebord_display():  # displys the gamebord
    gamebord_creation()
    print("   "+"  ".join([str(i)for i in range(game_length)]))
    counter = 0
    for row in gamebord:
        print(counter, row)
        counter += 1


gamebord_display()
