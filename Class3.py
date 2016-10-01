b = [[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]]

def check(row, col):
	#上边

	if row > 7 or col > 7:
		return False

	for i in range(row):
		if b[i][col] == 1:
			return False		
	#左上
	if row == col:
		for i in range(row):
			if b[i][i] == 1:
				return False
	elif row > col:
		for i in range(col):
			if b[row - i - 1][col - i - 1] == 1:
				return False
	else:
		for i in range(row):
			if b[row - i - 1][col - i - 1] == 1:
				return False

	#右上
	t_range = max(row, col)

	for i in range(t_range):
		t_row = row - i - 1
		t_col = col + i + 1
		if t_row > 7 or t_col > 7:
			break
		elif b[t_row][t_col] == 1:
			return False

	return True

def find(row):
	for i in range(len(b[row])):
		if b[row][i] == 1:
			return i
	return -1

def back_tracking(row):
	row -= 1
	t_col = find(row)
	b[row][t_col] = 0
	col = t_col + 1

	return row, col

def eight_queens():
	

	current_row = 0
	current_col = 0
	count = 0
	while True:
	# print(current_row, current_col)
		if check(current_row, current_col) == True:
			b[current_row][current_col] = 1
			current_row += 1
			current_col = 0

			if current_row == 8: 
				for i in b:
					print(i)
				print()
				count += 1
				current_row, current_col = back_tracking(current_row)

			if current_row < 0 or current_row > 8:
				break

		else:
			current_col += 1
			if current_col > 7:

				current_row, current_col = back_tracking(current_row)

				if current_row < 0 or current_row > 8:
					break
	print("Total Possibility: ", count)	

eight_queens()