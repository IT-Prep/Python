b = [-1] * 8

def check(index):
	for i in range(index):
		value_i = b[i]
		left = i - (index - b[index])
		right = index - i  + b[index]

		if b[index] == value_i:
			print("UP WRONG")
			return False
		if left >= 0 and left == value_i:
			print("UP LEFT WRONG")
			return False
		if right <= 7 and right == value_i:
			print("UP RIGHT WRONG")
			return False
	return True

def eight_queens():

	for j in range(8):
		b[index] = j
		if check(index):
			break

	print(b)

eight_queens()