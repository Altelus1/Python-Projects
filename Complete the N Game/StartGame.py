

def setup_empty_board():
	global b_dimension
	global board
	for cell in range(b_dimension):
		board.append([' ']*b_dimension)

def print_board():
	global b_dimension
	global PARTS
	global board
	for y_pos in range(b_dimension):
		for part in range(len(PARTS)):
			for x_pos in range(b_dimension):
				if part == 2:
					print(PARTS[part].format(board[y_pos][x_pos]),end="")
				else:
					print(PARTS[part],end = "")
			print("")

def get_player_coord(player_symbol):
	global board
	str_coord = input("Format 'x y' : ")
	coord = str_coord.split(" ")
	board[int(coord[1])-1][int(coord[0])-1] = player_symbol
	print_board()

def check_pattern()
		global board
			
print("Welcome to Complete the N Game")

player1 = input("Enter Player 1 symbol: ")
player2 = input("Enter Player 2 symbol: ")

MIN_BOX_DIM = 7
MAX_BOX_DIM = 10
MIN_N = 3
MAX_N = 0
OFFSET = 4
round_count = 1
board = []

b_dimension = 0
n_max = 0

while b_dimension < MIN_BOX_DIM or b_dimension > MAX_BOX_DIM:
	b_dimension = int(input("BxB Dimension (MIN {} - MAX {}) : ".format(
						MIN_BOX_DIM,
						MAX_BOX_DIM
	)))
	
MAX_N = (b_dimension - OFFSET)

while n_max < MIN_N or n_max > MAX_N:
	n_max = int(input("N to complete (MIN {} - MAX {}) : ".format(
						MIN_N,
						MAX_N
	)))
	
print("")
PARTS = (" ___ ","|   |","| {} |","|___|")

setup_empty_board()
print_board()

while True:
		get_player_coord(player1)
		get_player_coord(player2)



