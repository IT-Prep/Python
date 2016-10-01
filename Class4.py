def find_min(list):
	if len(list) > 0:
		return min(list)
	else:
		return "Invalid"


def find_index(list, item):
	if len(list) > 0:
		for i in range(len(list)):
			if list[i] == item:
				return i
	else:
		return "Invalid"

def selection_sort(list):
	new_list = []
	while len(list) > 0:
		#find min
		x = find_min(list)
		#remove min
		y = find_index(list, x)
		list.pop(y)
		#append min
		new_list.append(x)
	return new_list

def swap(x, y):
	return y, x

def _bubble_sort(list):
	for i in range(1, len(list)):
		index_b = i
		index_a = i - 1

		if list[index_b] < list[index_a]:
			list[index_a], list[index_b] = swap(list[index_a], list[index_b])

def bubble_sort(list):
	if len(list) <= 1:
		return list

	#this is wrong, write me the correct code⬇️
	for _ in list:
		_bubble_sort(list)

	print(list)

a = [5,2,6,7,9,1,0,3]
bubble_sort(a)
# new_list = selection_sort(a)

