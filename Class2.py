# a = "a" + "b"
# b = "a" * 3
# print(a, b)

# c = 1 + 1
# d = 2 - 1 
# e = 3 * 4
# f = 5 / 6
# print(c, d, e, f)

# g = 1.0 + 1.1
# h = 2.3 - 1.5
# i = 3.9 * 8.8
# j =9.0 / 2.5
# print(g, h, i, j)

# k = 5 % 2
# l = -5 % 2
# m = 5.0 % 2
# print(k, l, m)

# cond = False
# if cond:
# 	print("I'm true")
# else:
# 	print("I'm false")
# counter = 0
# cond = True
# while cond:
# 	counter = counter + 1
# 	print(counter)
# 	if counter == 3:
# 		cond = False
# else: 
# 	print("I'm false")

# for i in range(5):
#     print(i)

# for i in range(1, 5):
#     print(i)

# counter = 0
# for i in "abc a;jtr234":
#     if i.isdigit():
#     	counter = counter + 1

# print(counter)

# a = input()
# char_counter = 0
# num_counter = 0
# for i in a:
#     if i.isalpha():
#         char_counter += 1
#     if i.isdigit():
#     	num_counter += 1

# print("You enter", char_counter, "character(s)")
# print("You enter", num_counter, "digit(s)")

# my_sum = 0
# iteration = 0
# while iteration <= 10:
# 	my_sum += iteration
# 	iteration += 1
# print(my_sum)

# n = input()
# if n.isdigit():
# 	n = int(n) + 1
# 	s1 = 0
# 	s2 = 0
# 	s3 = 0
# 	for i in range(1, n):
# 		s1 += i
# 		s2 += (2 * i - 1)
# 		s3 += (2 * i)
# 	print(s1, s2, s3)
# else:
# 	print("You enter something non-digit")

# s2 = 0
# current = 1
# counter = 0
# end = 10
# while True:
# 	if counter == end:
# 		break
# 	elif current % 2 == 0:
# 		s2 += current
# 		counter += 1
	
# 	current += 1

# print(s2)

n = input()
m = int(n)
n = int(n) + 1

for i in range(1, n):
	print("*" * i)
print("="*n * 2 )

for i in range(1, n):
	print(" " * (m - i) + "*" * i)
print("="*n * 2 )

for i in range(1, n):
	print(" " * (m - i) + "*" * (2 * i - 1))
print("="*n * 2 )

for i in range(0, m):
	print("*" * (m - i) + " " * i)
print("="*n * 2 )

for i in range(0, m):
	print(" " * i + "*" * (m - i))
print("="*n * 2 )

for i in range(0, m):
	print(" " * i + "*" * (2 * (m - i) - 1))
print("="*n * 2 )

for i in range(0, m):
	if i < m / 2:
		print(" " * (m - i - 1) + "*" * (2 * i + 1))
	else:
		print(" " * i + "*" * (2 * (m - i) - 1))