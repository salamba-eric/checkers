
import time

rows = 8
columns = 8

grid = [[[0,0,0] for y in range(columns)]for x in range(rows)]

def print_b():
	for x in range(rows):
		print(grid[x])
	print()

def make_black_squares():
	for x in range(columns):
		if x%2 == 0:
			for y in range(1 , columns , 2):
				grid[x][y][0] = 1 #"Black_sq"
		if x%2 != 0:
			for y in range(0 , columns , 2):
				grid[x][y][0] = 1 #"Black_sq"

def set_pieces(blacks_rows , whites_rows):
	for y in range(columns):
		for black in range(blacks_rows):
			if grid[black][y][0] == 1:
				grid[black][y][1] = 1 #"Black_piece"
		for white in range(rows - 1 ,rows - whites_rows - 1 , -1):
			if grid[white][y][0] == 1:
				grid[white][y][1] = 2 #"White_piece"

def occupied(square):
	if grid[square[0]][square[1]][1] != 0:
		return True
	else:
		return False

def possible_moves(square):
	if occupied(square):
		if grid[square[0]][square[1]][2] == 0:
			if grid[square[0]][square[1]][1] == 1:
				possible_moves = [ (square[0] + 1 , square[1] + 1) , (square[0] + 1 , square[1] - 1) ]
			elif grid[square[0]][square[1]][1] == 2:
				possible_moves = [ (square[0] - 1 , square[1] + 1) , (square[0] - 1 , square[1] - 1) ]

		elif grid[square[0]][square[1]][2] == 1 :
			possible_moves = []
	else:
		possible_moves = []
	for point in possible_moves:
		if point == square:
			possible_moves.remove(point)
		for axis in point:
			if axis < 0 or axis > rows:
				possible_moves.remove(point)

	return possible_moves

def moves(square):
	moves = possible_moves(square)
	if grid[square[0]][square[1]][2] == 0:
		for point in possible_moves(square):
			if occupied(point):
				moves.remove(point)
				if grid[point[0]][point[1]][1] != grid[square[0]][square[1]][1]:
					dr = point[0] - square[0]
					dc = point[1] - square[1]
					if not occupied( (point[0] + dr , point[1] + dc) ):
						moves.append( (point[0] + dr , point[1] + dc) )


	print(moves)		
	return moves


grid[2][2] = [1,1,0]
grid[3][3] = [1,2,0]
grid[3][1] = [1,1,0]
print_b()
moves((2,2))

# import pygame 
# from sys import exit

# width = 700
# height = 600

# win_color = (220 , 200 , 200)
# white_piece = (180 , 180 , 180)
# black_piece = (50 , 50 , 50)
# black_color = (90 , 90 , 120)
# possibility_color  = (200 , 30 , 180)

# pygame.init()
# pygame.display.set_caption("Checkers")
# win = pygame.display.set_mode((width,height))

# def draw_board(active_p):

# 	sq_width = int(width/rows)
# 	sq_height = int(height/columns)

# 	thickness = 10
# 	if sq_height <= sq_width:
# 		radius = int(sq_width/2) - 10
# 	else:
# 		radius = int(sq_height/2) - 10

# 	win.fill(win_color)
# 	for x in range(rows):
# 		for y in range(columns):
# 			if grid[x][y][0] == 1:
# 				pygame.draw.rect(win , black_color , pygame.Rect(y * sq_width , x * sq_height , sq_width , sq_height))
# 			if grid[x][y][1] == 1:
# 				pygame.draw.circle(win , black_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius , thickness)
# 				pygame.draw.circle(win , black_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius - thickness -  2 , thickness)
# 			if grid[x][y][1] == 2:
# 				pygame.draw.circle(win , white_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius , thickness)
# 				pygame.draw.circle(win , white_piece , (y*sq_width + int(sq_width/2) , x*sq_height + int(sq_height/2)) , radius - thickness -  2 , thickness)
# 			if active == True:
# 				for p in active_p:
# 					pygame.draw.circle(win , possibility_color , (p[1]*sq_width + int(sq_width/2) , p[0]*sq_height + int(sq_height/2)) , 10 , 7)
# moving_fro_to = []
# active = False
# active_p = []
# player = 1

# while True:
# 	for event in pygame.event.get():
# 		pygame.display.update()
# 		if event.type == pygame.QUIT:
# 			exit()

# 		if event.type == pygame.MOUSEBUTTONDOWN:
# 			position = ( int(event.pos[1] / int(height/rows)) ,int(event.pos[0] / int(width/columns)) )
			

# 			print("Active player..." , player , "Active??" , active)
# 			print("Length..." , len(moving_fro_to) , "Elemets...", moving_fro_to )


# 		draw_board(active_p)


