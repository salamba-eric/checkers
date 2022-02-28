# Help in aesthetics and time is the actual frame rate
import time , random

# Grid ADT's dimentions... work proportionally with window
rows = 100
cols = 100

# For manual input of first live squares and time the game runs in seconds
live_cells = []
max_iterations = 60

# Creating the grid ADT
grid = [[0 for y in range(cols)]for x in range(rows)]

# Drawing the grid in 2D array form
def draw_grid():
	for x in range(rows):
		print(grid[x])

# Auto clears the grid
def __clear__():
	for x in range(rows):
		for y in range(cols):
			grid[x][y] = 0

# Sets all points in given list to 1 on the grid
def set_live(live_cells):
	__clear__()
	for co_ordinate in live_cells:
		grid[co_ordinate[0]][co_ordinate[1]] = 1

# Checks if given cell/point is live
def is_live(row , col):
	if grid[row][col] == 1:
		return True
	else:
		return False

# Returns "Full" if board is full and "Empty" if thats the case
def is_full():
	empty = 0
	occupied = 0
	for x in range(rows):
		for y in range(cols):
			if grid[x][y] == 0:
				empty += 1
			else:
				occupied += 1
	if occupied == rows*cols:
		return "Full"
	elif empty == rows*cols:
		return "Empty"

# Bears rules for reproduction and deaths
def rules():
	new_life = []
	for col in range(cols):
		for row in range(rows):
			live_neighbours = 0
			for point in neighbours(row , col):
				if grid[point[0]][point[1]] == 1:
					live_neighbours += 1
			if live_neighbours > 2:
				new_life.append((row,col))
			elif live_neighbours == 2 and grid[row][col] == 1:
				new_life.append((row,col))
			elif live_neighbours < 2 and grid[row][col] == 1:
				print("To die out..." , (row,col))
	
	print()
	set_live(new_life)
	
# Checking for all neighbours then eliminating unreqisited ones		
def neighbours(row , col):
	neighbours = []
	eliminated = []
	if rows > row and cols > col:
		for x in range(-1 , 2):
			for y in range(-1 , 2):
				neighbours.append((row + x , col + y))
		for n in range(len(neighbours)):
			for point in neighbours:
				if point[0] < 0 or point[1] < 0:
					eliminated.append(point)
					neighbours.remove(point)
				elif point == (row , col):
					eliminated.append(point)
					neighbours.remove(point)
				elif point[0] >= rows or point[1] >= cols:
					eliminated.append(point)
					neighbours.remove(point)
	else:
		print("One of the dimentionds too large..." , (row , col) , "Being referenced")
	return neighbours

# Picks "quantity" number of random points on the grid
def random_points(rows , cols , quantity):
	x_opt = []
	y_opt = []
	rando_list = []
	for row in range(rows):
		x_opt.append(row)
	for col in range(cols):
		y_opt.append(col)
	for n in range(quantity):
		x = random.choice(x_opt)
		y = random.choice(y_opt)
		rando_list.append((x,y))
	return rando_list

import pygame
from sys import exit

width = 600
height = 500

sq_color = (50 , 200 , 50)
win_color = (220 , 220 , 120)
live_color = (230 , 100 , 70)

pygame.display.set_caption("Game of life")
win = pygame.display.set_mode((width , height))

# Draws a relatively proportional grid on the window
def draw():
	win.fill(win_color)
	for x in range(rows):
		for y in range(cols):
			# Green square every where
			pygame.draw.rect(win , sq_color , pygame.Rect(int(width/cols)*y + 2 , int(height/rows)*x + 2, int(width/cols) - 2, int(height/rows) - 2))
			# Redish where grid == 1
			if is_live(x , y):
				pygame.draw.rect(win , live_color , pygame.Rect(int(width/cols)*y + 2 , int(height/rows)*x + 2, int(width/cols) - 2, int(height/rows) - 2))

set_live(random_points(rows , cols , 450))

# draw , apply rules ...then rinse and repeat for time*max_iteration times
for n in range(max_iterations):
	draw()
	rules()

	if is_full() == "Full":
		print("Board fulled at generation...", n + 1)
		break

	elif is_full() == "Empty":
		print("Board clear at generation...", n + 1)
		break

	pygame.display.update()
	time.sleep(0.5)