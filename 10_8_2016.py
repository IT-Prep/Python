def getBoard(b_len):
	return [-1] * b_len

def check(board, index):

	max_index = len(board) - 1

	for i in range(index):
		value_i = board[i]
		left = i - (index - board[index])
		right = index - i  + board[index]

		if board[index] == value_i:
			return False
		if left >= 0 and left == value_i:
			return False
		if right <= max_index and right == value_i:
			return False
	return True

def eight_queens(board):

	i = 0
	b_len = len(board)
	max_index = b_len - 1
	solution_count = 0
	
	while True:
		if board[i] >= max_index:
			board[i] = -1
			i -= 1

		if i <= -1:
			return

		for j in range(board[i] + 1, b_len):
			board[i] = j
			if check(board, i):
				i += 1
				break

		if i == b_len:
			solution_count += 1
			print(solution_count, board)
			i = max_index

i = 9
board = getBoard(i)
eight_queens(board)
