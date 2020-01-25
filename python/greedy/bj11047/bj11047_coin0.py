def solution():
	n,s = list(map(int, input().split()))
	result, coins =0, []
	for _ in range(n):
		c = int(input())
		if c<=s: coins.append(c)
	for c in coins[::-1]:
		result, s = result+s//c, s%c
		if s == 0: break
	print(result)

solution()
	
