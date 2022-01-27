# Write your code here

def bord():
    while True:
        s = input("Enter your board dimensions: ").split()
        if len(s) != 2:
            print("Invalid dimensions!")
        elif s[0].isdigit() == False or s[1].isdigit() == False:
            print("Invalid dimensions!")
        elif int(s[0]) < 1 or int(s[1]) < 1:
            print("Invalid dimensions!")
        else:
            return int(s[0]), int(s[1])

def position(a, b):
    while True:
        s = input("Enter the knight's starting position: ").split()
        if len(s) != 2:
            print("Invalid dimensions!")
        elif s[0].isdigit() == False or s[1].isdigit() == False:
            print("Invalid dimensions!")
        elif int(s[0]) > a or int(s[0]) < 1 or int(s[1]) > b or int(s[1]) < 1:
            print("Invalid dimensions!")
        else:
            return int(s[0]) - 1, int(s[1]) - 1

def possibol_position(a, b, x, y, lst):
    if x >= 0 and y >= 0 and x < a and y < b and "_" in lst[y][x]:
        return x, y

def possibol(a, b, x, y, lst):
    s = []
    s.append(possibol_position(a, b, x + 2, y + 1, lst))
    s.append(possibol_position(a, b, x + 2, y - 1, lst))
    s.append(possibol_position(a, b, x + 1, y + 2, lst))
    s.append(possibol_position(a, b, x - 1, y + 2, lst))
    s.append(possibol_position(a, b, x - 2, y + 1, lst))
    s.append(possibol_position(a, b, x - 2, y - 1, lst))
    s.append(possibol_position(a, b, x + 1, y - 2, lst))
    s.append(possibol_position(a, b, x - 1, y - 2, lst))
    s = [i for i in s if i != None]
    return s

def play_bord(a, b, lst):
    ferst_line = " " + ("-" * (x * ((len(str(x * y))) + 1) + 3))
    print(ferst_line)
    count = b
    for i in range(b, 0, -1):
        print(str(i) + "|", * lst[count], "|")
        count -= 1
    print(ferst_line)
    print("  ", *list(range(1, b + 1)), sep=" " * (len(str(a * b))))
    print()

def printSolution(a, b, board):
	ferst_line = " " + ("-" * (a * ((len(str(a * b))) + 1) + 3))
	print(ferst_line)
	count = b - 1
	for i in range(b, 0, -1):
		print(str(i) + "|", * board[count], "|")
		count -= 1
	print(ferst_line)
	print("  ", *list(range(1, a + 1)), sep=" " * (len(str(a * b))))

def next_move(a, b, lst1, lst2, x, y):
    while True:
        s = input("Enter your next move: ").split()
        if len(s) != 2:
            print("Invalid move!", end=" ")
        elif s[0].isdigit() == False or s[1].isdigit() == False:
            print("Invalid move!1", end=" ")
        elif int(s[0]) > a or int(s[0]) < 1 or int(s[1]) > b or int(s[1]) < 1:
            print("Invalid move!2", end=" ")
        elif (int(s[0]) - 1, int(s[1]) - 1) == (x, y):
            print("Invalid move!3", end=" ")
        elif "*" in lst1[int(s[1]) - 1][int(s[0]) - 1]:
            print("Invalid move!4", end=" ")
        elif (int(s[0]) - 1, int(s[1]) - 1) not in lst2:
            print("Invalid move!5", end=" ")
        else:
            return int(s[0]) - 1, int(s[1]) -1

def play_list(old, cell, a, b):
    lst2 = [["_" * cell for _ in range(a)] for _ in range(b)]
    if len(old) == 0:
        return lst2
    else:
        for i, j in old:
            lst2[j][i] = "*".rjust(cell)
        return lst2

def sol():
    while True:
        s = input("Do you want to try the puzzle? (y/n): ")
        if s.lower() == "y" or s.lower() == "n":
            return s.lower()
        else:
            print("Invalid input!")

def isSafe(x, y, board, a, b):
	if x >= 0 and y >= 0 and x < a and y < b and board[y][x] == -1:
		return True
	return False


def printSolution(a, b, board):
	ferst_line = " " + ("-" * (a * ((len(str(a * b))) + 1) + 3))
	print(ferst_line)
	count = b - 1
	for i in range(b, 0, -1):
		print(str(i) + "|", * board[count], "|")
		count -= 1
	print(ferst_line)
	print("  ", *list(range(1, a + 1)), sep=" " * (len(str(a * b))))

def solveKT(a, b, x, y):
	board = [[-1 for i in range(a)] for i in range(b)]
	move_x = [2, 1, -1, -2, -2, -1, 1, 2]
	move_y = [1, 2, 2, 1, -1, -2, -2, -1]
	board[y][x] = "1".rjust(len(str(a * b)))
	pos = 2
	if not solveKTUtil(a, b, board, x, y, move_x, move_y, pos):
		print("No solution exists!")
	else:
         print("Here's the solution!")
         printSolution(a, b, board)

def solveKT1(a, b, x, y):
    board = [[-1 for i in range(a)] for i in range(b)]
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[y][x] = "1".rjust(len(str(a * b)))
    pos = 2
    if not solveKTUtil(a, b, board, x, y, move_x, move_y, pos):
        print("No solution exists!")
        exit()


def solveKTUtil(a, b, board, start_x, start_y, move_x, move_y, pos):
	if pos - 1 == a * b:
		return True

	for i in range(8):
		new_x = start_x + move_x[i]
		new_y = start_y + move_y[i]
		if isSafe(new_x, new_y, board, a, b):
			board[new_y][new_x] = str(pos).rjust(len(str(a * b)))
			if solveKTUtil(a, b, board, new_x, new_y, move_x, move_y, pos+1):
				return True

			# Backtracking
			board[new_y][new_x] = -1
	return False




a, b = bord()
x, y = position(a, b)


cell_size = len(str(a * b))


count = 0
h_num = count
old_moves = []
game = play_list(old_moves, cell_size, a, b)

quest = sol()
if quest == "n":
    if __name__ == "__main__":
        solveKT(a, b, x, y)
else:
    if __name__ == "__main__":
        solveKT1(a, b, x, y)
    while True:
        game[y][x] = "X".rjust(cell_size)
        old_move = (x, y)
        old_moves.append(old_move)
        o_position = possibol(a, b, x, y, game)
        hod_lst = []
        for k, j in o_position:
            hod = [(z, q) for z, q in possibol(a, b, k, j, game) if (z, q) not in old_moves and (z, q) != (x, y)]
            if game[j][k] != "*".rjust(cell_size):
                game[j][k] = " " * (cell_size - 1) + str(len(hod))
                vozmo = (k, j)
            hod_lst.append(vozmo)
        printSolution(a, b, game)
        if len(o_position) == 0:
            break
        count += 1
        h_num = str(count)
        game = play_list(old_moves, cell_size, a, b)
        x, y = next_move(a, b, game, hod_lst, x, y)

    flag = True
    for i in game:
        for k in i:
            if "_" in k:
                flag = False
    if flag:
        print("What a great tour! Congratulations!")
    else:
        print("No more possible moves!")
        print(f"Your knight visited {count +1} squares!")




