
# kn = 0

# for i in range(100):
# 	pre = kn
# 	kn = pre * 2 + 1

# print(kn)


# def kn(n):
# 	if n == 1:
# 		return 0
# 	return kn(n - 1) * 2 + 1

# print(kn(101))

# kn = 1
# kn_1 = 1
# kn_2 = 0

# for i in range(200 - 2):
# 	kn_2 = kn_1
# 	kn_1 = kn
# 	kn = kn_1 + kn_2
# 	print(kn)

# def fib(n):
# 	if n <= 2:
# 		return 1 
# 	return fib(n - 1) + fib(n - 2)

memo = {0:0, 1:1}

def m_fib(n):
  if n not in memo:
    memo[n] = m_fib(n-1) + m_fib(n-2)
  return memo[n]

print(m_fib(200))