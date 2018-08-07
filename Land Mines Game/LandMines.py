
from pynput.keyboard import Key, Listener
import os

"""
Only Works in windows!!! No mines yet. No collision Walls yet :( Saaad
Courtesy from https://pythonhosted.org/pynput/keyboard.html
"""

def on_press(key):
	global player_pos
	global arrow_keys
	global released
	try:
		if released:
			player_pos[0] += arrow_keys[key][0]
			player_pos[1] += arrow_keys[key][1]
			released = False
	except KeyError:
		pass
	
	
def on_release(key):
	global player_pos
	global released
	print_board(player_pos)
	released = True
	if key == Key.esc:
			return False
	
def print_board(player_pos):
	os.system("cls")
	global y_dimension
	global x_dimension
	print(" "+("+"*x_dimension)+" ")
	#print(("|"+(" "*x_dimension)+"|\n")*y_dimension,end="")
	for row in range(y_dimension):
		print("|",end="")
		if row == player_pos[1]:
			print(" "*player_pos[0]+"#"+" "*(x_dimension - player_pos[0]-1),end="")
		else:
			print(" "*x_dimension,end="")
		print("|\n",end="")
		
	print(" "+("+"*x_dimension)+" ")
	print("Press ESC to end play")

print("Welcome to Land Mines!!!")

released = True

arrow_keys = {

	Key.down : [0,1],
	Key.up : [0,-1],
	Key.left : [-1, 0],
	Key.right : [1, 0]
}

boxes = 0
MIN_XY = (50, 10)
MAX_XY = (100, 15)

player_pos = [0,0]

x_dimension = 0
y_dimension = 0


while x_dimension < MIN_XY[0] or x_dimension > MAX_XY[0]:
	x_dimension = int(input("X Size (MIN - {} | MAX - {} : ".format(MIN_XY[0],
														MAX_XY[0]
	)))

while y_dimension < MIN_XY[1] or y_dimension > MAX_XY[1]:
	y_dimension = int(input("Y Size (MIN - {} | MAX - {} : ".format(MIN_XY[1],
														MAX_XY[1]
	))) 
	
with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
	print_board(player_pos)
	
	
#print_board(MIN_box)
