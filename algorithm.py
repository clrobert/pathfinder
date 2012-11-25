
# 
#! Format for squares is (y,x)
#! Define grid structure
#! 	Create ability to have unwalkable squares
#! 	Create ability to have start and destination squares	
#
# Letters represent the state of the square / node.
# O (as in omega) is open and untraversed
# T is traversed
# C is current
# X is not traversable
# S is the source square
# D is the destination square
#
grid = [['T','X','O','O','O'],['X','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]

#stub
def findCheapestPath(source, openSquares, travelled, currentSquare, endSquare):
	cheapest = None
	cost = 20 # A magic number to initialize.
	for square in openSquares:
		if getCost(source, square) < cost:
			cost = getF(travelled, currentSquare, endSquare)
			cheapest = square
	return cheapest # may return nil!

def getF(travelled, currentSquare, endSquare):
	return getG(travelled) + getH(currentSquare, endSquare)

def getG(travelled):
	total = 0
	for movement in travelled:
		total = total + movement[0]
	return total

def getH(source, destination):
	y = destination[1] - source[1] 
	x = destination[0] - source[0]
	return x + y

def getCost(source, destination):
	cost = 14
	# If not diagonal
	if (destination[0] - source[0]) == 0:
		cost = 10
	if (destination[1] - source[1]) == 0:
		cost = 10
	if destination == 'X':
		cost = nil
	return cost

def traverse(source, destination, travelled):
	cost = getCost(source, destination)
	travelled.append((cost, source))
	grid[source[0]][source[1]] = 'T'
	grid[destination[0]][destination[1]] = 'C'
	return destination

def isOpen(square):
	open = False
	if square[0] >= 0 and square[0] <= 4 and square[1] >= 0 and square[1] <= 4: # This is to prevent wrapping
		if grid[square[0]][square[1]] == 'O':
			open = True
	return open

def getOpenAdjacentSquares(currentSquare):
	openSquares = []
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if j != 0 or i != 0:
				square = (currentSquare[0] + i, currentSquare[1] + j)
				if isOpen(square):
					openSquares.append(square)

	return openSquares

def thereIsAPath(currentSquare, endSquare, openSquares):
	return currentSquare != endSquare and openSquares

def printGrid():
	print grid[4]
	print grid[3]
	print grid[2]
	print grid[1]
	print grid[0]
	print "-------------------------"


# 
# Pathfind:
#! Get a list of all open adjacent squares
#! Traverse to the shortest path, add the previous square to the closed list and the new square as the
# 	current square.
# Look for the lowest cost square on the open list that is not unwalkable or on the closed list:
# 	If this is a new square: 
#		Add a new square to the open list, make the current square its parent
#!		Grab the movement cost from the starting point to the current location (10 straight, 14 diagonal)
#! 		Calculate the distance from the current location to the goal destination ()
# 		Add the previous two steps together to get the cost of the given square
# 	Else 
#		check if the path to this square is better by using the distance from start to that point
#
# Quit when: destination square is on closed list, or open list is empty.
# Save path and work backwards from target square.
#
# IF you are back at the source square, and all paths have been traversed, there is no solution.
def main():

	travelled = []
	currentSquare = (0,0)
	startSquare = (0,0)
	endSquare = (4,4)
	printGrid()

	openSquares = getOpenAdjacentSquares(currentSquare)
	currentSquare = traverse(currentSquare, (1,1), travelled)
	printGrid()

	while (thereIsAPath(currentSquare, endSquare, openSquares)):
 		cheapest = findCheapestPath(currentSquare, getOpenAdjacentSquares(currentSquare), travelled, currentSquare, endSquare)
 		currentSquare = traverse(currentSquare, cheapest, travelled)
 		printGrid()

main()