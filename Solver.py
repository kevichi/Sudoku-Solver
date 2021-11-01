class Solver:
	size = 9
	board = []
	def __init__(self, board):
		self.board = board
		self.size =9

		print("Welcome to Sudoku solver, developed by Hai Muo Cui")
	
	def checkRow(self, row, value):
		for i in range(9):
			if self.board [row][i] == value:
				return False
		return True

	def checkColumn(self, column, value):
		for i in range(9):
			if self.board [i][column] == value:
				return False
		return True

	def checkBlock(self, row, column, value):
		xVal = (row // 3) * 3
		yVal = (column // 3) * 3
		for i in range(xVal, xVal +3):
			for j in range(yVal, yVal +3):
				if self.board[i][j] == value:
					return False
		return True

	def isValid(self, row, column, value):
		if self.checkRow(row,value) and self.checkColumn(column,value) and self.checkBlock(row,column,value):
			return True

	def getNextBlank(self,b):
		for i in range(self.size):
			for j in range(self.size):
				if b[i][j] == 0:
					return (i,j)

		return None

	def solvePuzzle(self,b):
		nextBlock = self.getNextBlank(b)
		

		if not self.getNextBlank(b):
			return True
		else:
			xPos = nextBlock[0]
			yPos = nextBlock[1]

		

		for i in range(1,10):
			if self.isValid(xPos,yPos,i):
				b[xPos][yPos] = i


				if self.solvePuzzle(b):
					return True


				b[xPos][yPos] = 0

		return False

	


			
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
print()
print("Completed Sudoku puzzle")

for x in range(9):
	print(sudokuBoard[x])