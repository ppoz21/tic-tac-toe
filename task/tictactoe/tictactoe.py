def check(cells):
    count_x = 0
    count_o = 0
    count_space = 0
    for letter in cells:
        if letter == "X":
            count_x += 1
        elif letter == "O":
            count_o += 1
        else:
            count_space += 1
    if count_x > count_o + 1 or count_o > count_x + 1:
        print("Impossible")
    else:
        if (cells[0:3] == "XXX" or cells[3:6] == "XXX" or cells[6:9] == "XXX") \
                and (cells[0:3] == "OOO" or cells[3:6] == "OOO" or cells[6:9] == "OOO"):
            print("Impossible")
        elif (cells[0] + cells[3] + cells[6] == "XXX" or cells[1] + cells[4] + cells[7] == "XXX" or cells[2] + cells[5] + cells[8] == "XXX") \
                and (cells[0] + cells[3] + cells[6] == "OOO" or cells[1] + cells[4] + cells[7] == "OOO" or cells[2] + cells[5] + cells[8] == "OOO"):
            print("Impossible")
        else:
            if cells[0:3] == "XXX" or cells[3:6] == "XXX" or cells[6:9] == "XXX" \
                    or cells[0] + cells[3] + cells[6] == "XXX" or cells[1] + cells[4] + cells[7] == "XXX" \
                    or cells[2] + cells[5] + cells[8] == "XXX" \
                    or cells[0] + cells[4] + cells[8] == "XXX" or cells[2] + cells[4] + cells[6] == "XXX":
                print_board()
                print("X wins")
            elif cells[0:3] == "OOO" or cells[3:6] == "OOO" or cells[6:9] == "OOO" \
                    or cells[0] + cells[3] + cells[6] == "OOO" or cells[1] + cells[4] + cells[7] == "OOO" \
                    or cells[2] + cells[5] + cells[8] == "OOO" \
                    or cells[0] + cells[4] + cells[8] == "OOO" or cells[2] + cells[4] + cells[6] == "OOO":
                print_board()
                print("O wins")
            else:
                if count_space == 0:
                    print_board()
                    print("Draw")
                else:
                    return True


def print_board():
    print('---------')
    print('|', cells[0], cells[1], cells[2], '|')
    print('|', cells[3], cells[4], cells[5], '|')
    print('|', cells[6], cells[7], cells[8], '|')
    print('---------')


cells_str = '_________'
cells_str = cells_str.replace('_', " ")
cells = list(cells_str)


counter = 0
while check(cells):
    print_board()
    if counter % 2 == 0:
        printable = 'X'
    else:
        printable = 'O'
    x, y = input().split(' ')
    try:
        x = int(x)
    except ValueError:
        print("You should enter numbers!")
        continue
    else:
        if x not in range(1, 4):
            print('Coordinates should be from 1 to 3')
            continue
    try:
        y = int(y)
    except ValueError:
        print("You should enter numbers!")
        continue
    else:
        if y not in range(1, 4):
            print('Coordinates should be from 1 to 3')
            continue
    if x == 1:
        if y == 1:
            if cells[6] == " ":
                cells[6] = printable
            else:
                print("This cell is occupied! Choose another one!")
        elif y == 2:
            if cells[3] == " ":
                cells[3] = printable
            else:
                print("This cell is occupied! Choose another one!")
        else:
            if cells[0] == " ":
                cells[0] = printable
            else:
                print("This cell is occupied! Choose another one!")
    elif x == 2:
        if y == 1:
            if cells[7] == " ":
                cells[7] = printable
            else:
                print("This cell is occupied! Choose another one!")
        elif y == 2:
            if cells[4] == " ":
                cells[4] = printable
            else:
                print("This cell is occupied! Choose another one!")
        else:
            if cells[1] == " ":
                cells[1] = printable
            else:
                print("This cell is occupied! Choose another one!")
    else:
        if y == 1:
            if cells[8] == " ":
                cells[8] = printable
            else:
                print("This cell is occupied! Choose another one!")
        elif y == 2:
            if cells[5] == " ":
                cells[5] = printable
            else:
                print("This cell is occupied! Choose another one!")
        else:
            if cells[2] == " ":
                cells[2] = printable
            else:
                print("This cell is occupied! Choose another one!")
    counter += 1
