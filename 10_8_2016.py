b = [-1] * 8

def check(index):
	for i in range(index):
		value_i = b[i]
		left = i - (index - b[index])
		right = index - i  + b[index]

		if b[index] == value_i:
			return False
		if left >= 0 and left == value_i:
			return False
		if right <= 7 and right == value_i:
			return False
	return True

def eight_queens():
	i = 0
	solution_count = 0
	while True:
		if b[i] >= 7:
			b[i] = -1
			i -= 1

		if i <= -1:
			return

		for j in range(b[i] + 1, 8):
			b[i] = j
			if check(i):
				i += 1
				break

		if i == 8:
			solution_count += 1
			print(solution_count, b)
			i = 7

eight_queens()