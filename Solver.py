class Solver:
	size = 9
	board = []
	def __init__(self, board):
		self.board = board
		print("welcome to sudoku solver")
	
	def checkRow(row, value):
		for i in range(size):
			if board [row][i] == value:
				return false
		return true

	def checkColumn(column, value):
		for i in range(size):
			if board [i][column] == value:
				return false
		return true

	def checkBlock(row, column, value):
		xVal = (row // 3) * 3
		yVal = (column // 3) * 3
		for i in range(xVal, xVal +3):
			for j in range(yVal, yVal +3):
				if board[i][j] == value:
					return false
		return true

	def isValid(row, column, value):
		if checkRow(row,value) and checkColumn(column,value) and checkBlock(row,column,value):
			return true

	def getNextBlank(b):
		for i in range(size):
			for j in range(size):
				if b[i][j] == 0:
					return (i,j)

	def solvePuzzle(self,b):
		nextBlock = self.getNextBlank(b)
		xPos = nextBlock[0]
		yPos = nextBlock[1]

		if not getNextBlank(b):
			return true

		for i in range(1,10):
			if isValid(xPos,yPos,i):
				b[xPos][yPos] = i

		solvePuzzle(b)

	


			
sudokuBoard = [
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]


solver = Solver(sudokuBoard)
for x in range(9):
	print(sudokuBoard[x])

solver.solvePuzzle(sudokuBoard)

for x in range(9):
	print(sudokuBoard[x])