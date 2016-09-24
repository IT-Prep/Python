def check(board, row, col):
	#上边

	if row > 7 or col > 7:
		return False

	for i in range(row):
		if board[i][col] == 1:
			return False		
	#左上
	if row == col:
		for i in range(row):
			if board[i][i] == 1:
				return False
	elif row > col:
		for i in range(col):
			if board[row - i - 1][col - i - 1] == 1:
				return False
	else:
		for i in range(row):
			if board[row - i - 1][col - i - 1] == 1:
				return False

	#右上
	t_range = max(row, col)

	for i in range(t_range):
		t_row = row - i - 1
		t_col = col + i + 1
		if t_row > 7 or t_col > 7:
			break
		elif board[t_row][t_col] == 1:
			return False

	return True

def find(board, row):
	for i in range(len(board[row])):
		if board[row][i] == 1:
			return i
	return -1

def eight_queens():

	b = [[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0]]

	current_row = 0
	current_col = 0
	count = 0
	while True:
	# print(current_row, current_col)
		if check(b, current_row, current_col) == True:
			b[current_row][current_col] = 1
			current_row += 1
			current_col = 0

			if current_row == 8: 
				for i in b:
					print(i)
				count += 1
				print()
				current_row -= 1
				t_col = find(b, current_row)
				b[current_row][t_col] = 0
				current_col = t_col + 1

			if current_row < 0 or current_row > 8:
				break

		else:
			current_col += 1
			if current_col > 7:
				current_row -= 1
				t_col = find(b, current_row)
				b[current_row][t_col] = 0
				current_col = t_col + 1

				if current_row < 0 or current_row > 8:
					break
	print("Total Possibility: ", count)	

eight_queens()