


if __name__ == '__main__':
    game = [
        [[],[],[]],
        [[],[],[]],
        [[],[],[]]
    ]

    complete = 1
    turn = 'o'

    while complete:
        x, y = input("Type X and Y coordinate 0 to 2\n").split()
        int(x)
        int(y)
        
        if game[x][y].count("x") + game[x][y].count("o") > 0:
            print(game)
            print("Retry")
            continue
        else:
            game[x][y] = turn
            turn = 'x'


    

