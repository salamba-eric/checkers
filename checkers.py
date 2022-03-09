import time

rows = 8
columns = 8

blacks_rows = 3
whites_rows = 3

norm = 1

grid = [[[0,0,0] for y in range(columns)]for x in range(rows)]

def print_b():
	for x in range(rows):
		print(grid[x])
	print()

def player_switch(player):
	if player == 1:
		player = 2
	elif player == 2:
		player = 1
	return player

def __win__(score):
	if score[1] == blacks_rows * (columns/2):
		print("PLayer One <<White>> wins")
		score[0] -= 1
		score[1] = 0
		make_black_squares()
		set_pieces(blacks_rows , whites_rows , norm)
	elif score[2] == whites_rows * (columns/2):
		print("Player Two <<Black>> wins")
		score[0] += 1
		score[2] = 0
		make_black_squares()
		set_pieces(blacks_rows , whites_rows , norm)

def promote( x , y ):
	if grid[x][y][1] == 1 and x == rows - 1:
		grid[x][y][2] = 1
	elif grid[x][y][1] == 2 and x == 0:
		grid[x][y][2] = 1
		
def make_black_squares():
	for x in range(rows):
		for y in range(columns):
			grid[x][y][1] = 0
			grid[x][y][2] = 0
	for x in range(columns):
		if x%2 == 0:
			for y in range(1 , columns , 2):
				grid[x][y][0] = 1 #"Black_sq"
		if x%2 != 0:
			for y in range(0 , columns , 2):
				grid[x][y][0] = 1 #"Black_sq"


def set_pieces(blacks_rows , whites_rows , norm):
	for y in range(columns):
		for black in range(blacks_rows):
			if grid[black][y][0] == norm:
				grid[black][y][1] = 1 #"Black_piece"
		for white in range(rows - 1 ,rows - whites_rows - 1 , -1):
			if grid[white][y][0] == norm:
				grid[white][y][1] = 2 #"White_piece"

def occupied(square):
	if grid[square[0]][square[1]][1] != 0:
		return True
	else:
		return False

def king_moves(point):
	possible_moves = list()
	moves_r1 = []
	moves_r2 = []
	moves_l1 = []
	moves_l2 = []
	for x in range(1 , rows):
		if point[0] + x < rows and point[1] + x < columns:
			moves_r1.append( (point[0] + x , point[1] + x) )
		if point[0] - x >= 0 and point[1] - x >= 0:
			moves_l1.append( (point[0] - x , point[1] - x) )
		if point[0] - x >= 0 and point[1] + x < columns:
			moves_r2.append( (point[0] - x , point[1] + x))
		if point[0] + x < rows and point[1] - x >= 0:
			moves_l2.append( (point[0] + x , point[1] - x))
	possible_moves = [moves_r1,moves_r2,moves_l1,moves_l2]

	for n in range(len(possible_moves)):
		for item in possible_moves[n]:
			if occupied(item):
				print("Possible moves and item occupied",item , possible_moves)
				possible_moves[n] = possible_moves[n][:possible_moves[n].index(item) + 1]
				break

	return possible_moves

def possible_moves(square):
	# Ensure a piece is clicked on
	if occupied(square):
		# If piece is not a king
		if grid[square[0]][square[1]][2] == 0:
			if grid[square[0]][square[1]][1] == 1:
				possible_moves = [ (square[0] + 1 , square[1] + 1) , (square[0] + 1 , square[1] - 1) ]
			elif grid[square[0]][square[1]][1] == 2:
				possible_moves = [ (square[0] - 1 , square[1] + 1) , (square[0] - 1 , square[1] - 1) ]
			# Removing outof bounds squares
			for point in possible_moves:
				if point == square:
					possible_moves.remove(point)
				elif point[0] < 0 or point[0] > rows - 1 or point[1] < 0 or point[1] > columns - 1:
					possible_moves.remove(point)
		# If player is a king
		elif grid[square[0]][square[1]][2] == 1 :
			possible_moves = king_moves(square)

	

	return possible_moves

def moves(square):
	
	n = 0
	k = 0
	sp_moves1 = []
	sp_moves2 = []

	moves = possible_moves(square)
	if grid[square[0]][square[1]][2] == 0:
		for itterations in range(len(moves)):
			for point in moves:
				if occupied(point):
					moves.remove(point)
					if grid[point[0]][point[1]][1] != grid[square[0]][square[1]][1]:
						dr = point[0] - square[0]
						dc = point[1] - square[1]

						if point[0]+dr < rows and point[0]+dr >= 0 and point[1]+dc < columns and point[1]+dc >= 0 :
							if not occupied( (point[0] + dr , point[1] + dc) ):
								sp_moves1.append(point)
								sp_moves2.append( (point[0] + dr , point[1] + dc) )

		if len(sp_moves1) > 0:
			for actual in sp_moves1:
				sp_moves.update( {actual : sp_moves2[n]} )
				n += 1

	elif grid[square[0]][square[1]][2] == 1:
		if len(moves) > 0:
			for n in range(len(moves)):
				last_index = len(moves[n]) - 1
				if last_index >= 0:
					if occupied(moves[n][last_index]):
						if grid[moves[n][last_index][0]][moves[n][last_index][1]][1] == grid[square[0]][square[1]][1]:
							moves[n].remove(moves[n][last_index])
						else:
							if n == 0:
								add = (  1 , 1 )
							elif n == 1:
								add = ( -1 , 1 )
							elif n == 2:
								add = ( -1 , -1)
							elif n == 3:
								add = ( 1 , -1 )
							nxt_point = (( moves[n][last_index][0] + add[0] , moves[n][last_index][1] + add[1] ))
							if nxt_point[0] < rows and nxt_point[0] >= 0 and nxt_point[1] < columns and nxt_point[1] >= 0:
								if occupied(nxt_point):
									moves[n].remove(moves[n][last_index])
								else:
									sp_moves1.append(moves[n][last_index])
									sp_moves2.append(nxt_point)
							else:
								moves[n].remove(moves[n][last_index])

			if len(sp_moves1) > 0 :
				for actual in sp_moves1:
					sp_moves.update( {actual : sp_moves2[k]} )
					k += 1


	return moves

def transpose(fro , to):
	grid[to[0]][to[1]] = grid[fro[0]][fro[1]]
	grid[fro[0]][fro[1]] = [norm,0,0]


make_black_squares()
set_pieces(blacks_rows , whites_rows , norm)


from pygame import MOUSEBUTTONDOWN as MouseButtonDown
from pygame import display as display
from pygame import event as evnt
from pygame import QUIT as quit
from pygame import Rect as Rect
from pygame import draw as draw
from sys import exit

width = 700
height = 600

win_color = (220 , 200 , 200)
white_piece = (180 , 180 , 180)
king = (120 , 70 , 90)
pick_color = (70 , 60 , 20)
black_piece = (50 , 50 , 50)
black_color = (90 , 90 , 120)
possibility_color  = (200 , 30 , 180)

display.set_caption("Checkers")
win = display.set_mode((width,height))

def draw_board(pos , active_p , sp_moves):
	sq_width = int(width/rows)
	sq_height = int(height/columns)

	thickness = 10
	if sq_height <= sq_width:
		radius = int(sq_width/2) - 10
	else:
		radius = int(sq_height/2) - 10

	win.fill(win_color)
	for x in range(rows):
		for y in range(columns):
			promote( x , y )
			if grid[x][y][0] == 1:
				draw.rect(win , black_color , Rect(y * sq_width , x * sq_height , sq_width , sq_height))
			if grid[x][y][1] == 1:
				draw.circle(win , black_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius , thickness)
				if grid[x][y][2] == 0:
					draw.circle(win , black_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius - thickness -  2 , thickness)
				elif grid[x][y][2] == 1:
					draw.circle(win , king , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius - thickness -  2 , thickness)
			if grid[x][y][1] == 2:
				draw.circle(win , white_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius , thickness)
				if grid[x][y][2] == 0:
					draw.circle(win , white_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius - thickness -  2 , thickness)
				elif grid[x][y][2] == 1 :
					draw.circle(win , king , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius - thickness -  2 , thickness)
			if active == True:
				draw.circle(win , "RED" , ( ((pos[1]*sq_width) + int(sq_width/2)),((pos[0]*sq_height) + int(sq_height/2))) , 7 , 7 )
				for p in active_p:
					if type(p) == tuple:
						draw.circle(win , possibility_color , (p[1]*sq_width + int(sq_width/2) , p[0]*sq_height + int(sq_height/2)) , 10 , 7)
					elif type(p) == list:
						for q in p:
							draw.circle(win , possibility_color , (q[1]*sq_width + int(sq_width/2) , q[0]*sq_height + int(sq_height/2)) , 10 , 7)
			if len(sp_moves) > 0:
				for q in sp_moves:
					r = sp_moves[q]
					draw.circle(win , pick_color , (q[1]*sq_width + int(sq_width/2) , q[0]*sq_height + int(sq_height/2)) , 10 , 7)
					draw.circle(win , pick_color , (r[1]*sq_width + int(sq_width/2) , r[0]*sq_height + int(sq_height/2)) , 10 , 7)

moving_fro_to = []
sp_moves = dict()
active = False
force_pick = False
active_p = []
score = [0 , 0 , 0]
pos = []
player = 1

while True:
	for event in evnt.get():
		display.update()
		if event.type == quit:
			exit()
		# On clicking enter 
		if event.type == MouseButtonDown:
			pos = ( int(event.pos[1] / int(height/rows)) ,int(event.pos[0] / int(width/columns)) )

			# If user clicks on their piece and no other has previously been clicked...add the piece that's been clicked
			if len(moving_fro_to) == 0 and  grid[pos[0]][pos[1]][1] == player:
				active = True
				active_p = moves(pos)
				moving_fro_to.append(pos)

			# Otherwise if another piece has been clicked on and now clicked on position is in available moves
			elif len(moving_fro_to) == 1 and pos in active_p:
				transpose(moving_fro_to[0] , pos)
				player = player_switch(player)
				active = False
				moving_fro_to.clear()
				sp_moves.clear()

			# If clicked on position is not in possible moves...
			elif len(moving_fro_to) == 1 and pos not in active_p:
				print("Moving to fro one",moving_fro_to)
				if pos in sp_moves or pos in sp_moves.values():
					print("\n<< Alternate move picking...>>")
					if pos in sp_moves.keys():
						transpose(moving_fro_to[0] , sp_moves[pos])
						grid[pos[0]][pos[1]] = [norm,0,0]

					if pos in sp_moves.values():
						transpose(moving_fro_to[0] , pos)
						for key in sp_moves.keys():
							if sp_moves[key] == pos:
								grid[key[0]][key[1]] = [norm,0,0]
					print("this where issue is")
					player = player_switch(player)
					active = False
					moving_fro_to.clear()
					sp_moves.clear()

					if player == 1:
						score[1] += 1
					else:
						score[2] += 1


				elif len(moving_fro_to) == 1 and grid[moving_fro_to[0][0]][moving_fro_to[0][1]][2] == 1:
					for n in range(len(active_p)):
						if pos in active_p[n]:
							transpose(moving_fro_to[0] , pos)
							active = False
							player = player_switch(player)
							moving_fro_to.clear()
							sp_moves.clear()
						elif pos not in active_p[0] and pos not in active_p[1] and pos not in active_p[2] and pos not in active_p[3]:
							active = False
							moving_fro_to.clear()
							sp_moves.clear()
				else:
					active = False
					moving_fro_to.clear()
					sp_moves.clear()

			print("active player..." , player , "active??" , active , "....Score" , score)
			print("Length..." , len(moving_fro_to) , "Elemets...", moving_fro_to )
			print("Special moves..." , sp_moves , "Active points..." , active_p)


		draw_board(pos , active_p , sp_moves)
		__win__(score)