
"""
Added Player class, added win checker, no documentation yet.
"""

class Player:
	
	def __init__(self, player_symbol):
		self.player_symbol = player_symbol
		self.positions = []
	
	def append_positions(self, posx, posy):
		for index in range(len(self.positions)):
			if posy <= self.positions[index][1] and posx <= self.positions[index][0]:
				self.positions.insert(index,[posx,posy])
				return
		self.positions.append([posx,posy])
		
	def get_symbol(self):
		return self.player_symbol
	
	def get_positions(self):
		return self.positions
	
	def check_win(self):
		global n_max
		direction = [[1,-1],[1,0],[1,1],[0,1]]
		for coord in self.positions:
			for path in direction:	
				for count in range(1,n_max):
					offset_x = path[0]*count
					offset_y = path[1]*count
					if [coord[0]+offset_x, coord[1]+offset_y] not in self.positions:
						break
					if count+1 == n_max:
						return True
		return False
					
					
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

def get_player_coord(player):
	global board
	str_coord = input("Format 'x y' : ")
	coord = str_coord.split(" ")
	board[int(coord[1])-1][int(coord[0])-1] = player.get_symbol()
	player.append_positions(int(coord[0]),int(coord[1]))
	print_board()
			
print("Welcome to Complete the N Game")

player1_symbol = input("Enter Player 1 symbol: ")
player1 = Player(player1_symbol)
player2_symbol = input("Enter Player 2 symbol: ")
player2 = Player(player2_symbol)

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
		print("Player1 positions: {}".format(player1.get_positions()))
		if(player1.check_win()):
			print("Player 1 wins")
			break
		get_player_coord(player2)
		print("Player2 positions: {}".format(player2.get_positions()))
		if(player2.check_win()):
			print("Player 2 wins")
			break



