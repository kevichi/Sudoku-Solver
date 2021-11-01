class Solver:
	size = 9
	board = []
	def __init__(self):
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

			
