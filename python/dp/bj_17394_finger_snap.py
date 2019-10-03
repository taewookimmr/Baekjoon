import math
import sys
    
def is_prime(number):
	if number == 0 or number == 1:
		return False
	sq = int(math.sqrt(number))
	for i in range(2, sq+1, 1):
		if number % i == 0:
			return False
	return True 

def fingersnap(record):

	start = record[0]
	left = record[1]
	right = record[2]

	primes = [e for e in range(left, right+1) if is_prime(e)]
	if len(primes) == 0:
		return -1
	if start in primes:
		return 0

	maxim = max(primes)
	minim = min(primes)
	if start < minim:
		return minim-start 
	
	dic = {}
	queue = [] 
	def searching():
		def determine(e, depth):
			if e in dic.keys():
				if dic[e] > depth+1:
					dic[e] = depth+1
					queue.append([e, depth+1])
					if e in primes :
						return depth+1
			else :
				dic[e] = depth+1
				queue.append([e, depth+1])
				if e in primes :
					return depth+1

		while len(queue) :
			pres, depth = queue.pop(0)
			if maxim < pres:
				for e in [pres //3, pres //2, pres -1]:
					d = determine(e, depth)
					if d != None:
						return d
			elif minim <= pres and pres <= maxim:
				for e in [pres //3, pres //2, pres -1, pres + 1]:
					d = determine(e, depth)
					if d != None:
						return d
			else :
				if pres >= 0:
					for e in [pres+1]:
						d = determine(e, depth)
						if d != None:
							return d
	queue = [[start, 0]]
	return searching()
			
def main():
	n = int(input())
	dataset = []
	for i in range(n):
		record = list(sys.stdin.readline().rstrip().split())
		record = [int(e) for e in record]
		dataset.append(record)

	for record in dataset:
		print(fingersnap(record))
	
main()

  
  