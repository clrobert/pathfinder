
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
grid = [['C','O','O','O','O'],['O','O','O','X','O'],['O','O','O','X','O'],['O','O','O','X','O'],['O','O','O','X','D']]
LOWER_BOUND = 0
UPPER_BOUND = 4
MAX_COST = 2000

#stub
def findCheapestPath(source, openSquares, travelled, currentSquare, endSquare):
	cheapest = None
	cheapestCost = MAX_COST
	for square in openSquares:
		totalCost = getF(travelled, square, endSquare)
		if totalCost < cheapestCost:
			cheapest = square
			cheapestCost = totalCost
	return cheapest # may return nil!

def getF(travelled, square, endSquare):
	return getG(travelled) + getH(square, endSquare)

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
	print destination
	print source
	cost = getCost(source, destination)
	travelled.append((cost, source))
	grid[source[0]][source[1]] = 'T'
	grid[destination[0]][destination[1]] = 'C'
	return destination

def isOpen(square):
	open = False
	# This is to prevent wrapping
	if square[0] >= LOWER_BOUND and square[0] <= UPPER_BOUND and square[1] >= LOWER_BOUND and square[1] <= UPPER_BOUND: 
		if grid[square[0]][square[1]] == 'O' or grid[square[0]][square[1]] == 'D' :
			open = True
	return open


# If no new squares are found, return the path from which you came
def getOpenAdjacentSquares(currentSquare, travelled):
	openSquares = []
	for i in [-1, 0, 1]:
		for j in [-1, 0, 1]:
			if j != 0 or i != 0:
				square = (currentSquare[0] + i, currentSquare[1] + j)
				if isOpen(square):
					openSquares.append(square)
	if travelled:
		openSquares.append(travelled[-1][1])
	return openSquares

# This covers the two END conditions:
# 1. You have reached the destination
# 2. You have returned to the start and the only path is traversed.
def thereIsAPath(currentSquare, endSquare, startSquare, openSquares, travelled):
	return currentSquare != endSquare and (openSquares[0] != travelled[-1][1] and currentSquare != startSquare)

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

	openSquares = getOpenAdjacentSquares(currentSquare, travelled)
	cheapest = findCheapestPath(currentSquare, openSquares, travelled, currentSquare, endSquare)
	currentSquare = traverse(currentSquare, cheapest, travelled)
	printGrid()

	while (thereIsAPath(currentSquare, endSquare, startSquare, openSquares, travelled)):	
		openSquares = getOpenAdjacentSquares(currentSquare, travelled)
 		cheapest = findCheapestPath(currentSquare, openSquares, travelled, currentSquare, endSquare)
 		currentSquare = traverse(currentSquare, cheapest, travelled)
 		printGrid()

main()