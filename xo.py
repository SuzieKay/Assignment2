matrix=[['X','0','X'],['X','O','X'],['O','X','O']]
def checkRows(matrix):
	for i in matrix:
		if i==['X','X','X'] or i==['O','O','O']:
			return True
	return False

print checkRows(matrix)
def checkColumn(matrix):
	for col in range(0,3):
		if matrix[0][col]==matrix[1][col]==matrix[2][col]:
			return True
		return False

print checkColumn(matrix)
def checkDiagonal(matrix):
	for i in range(0,2):
		if matrix[0][i]==matrix[1][i+1]==matrix[2][i+2]:
			return True
		elif matrix[0][2]==matrix[1][1]==matrix[2][0]:
			return True
		return False
print checkDiagonal(matrix)
