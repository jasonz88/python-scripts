"s is CCP 10.7 file"

import sys

def GenPrimeNumber(max):
  primes = [2, 3]
	i = 4
	while i <= max:
		if IsPrime(i, primes) == True:
			primes.append(i)
		i += 1
	return  primes
		           
def IsPrime(num, primes):
	i = 0
	while primes[i] * primes[i] <= num:
		if num % primes[i] == 0:
			return False
		i += 1
	return True

def HumbleSort(primeList, n):
	minList = []
	lists = []
	for item in primeList:
		lists.append([item])
	while n > 0:
		compList = []
		for q in lists:
			compList.append(q[0])
		minIndex = GetMin(compList)
		minVal = lists[minIndex].pop(0)
		i = minIndex
		while i < len(lists):
			lists[i].append(minVal * primeList[i])
			i += 1
		minList.append(minVal)
		n -= 1
	return minList
																									          
def GetMin(list):
	min = sys.maxint
	for item in list:
		if item  < min:
			min = item
	return list.index(min)

if __name__ == '__main__':
	list = GenPrimeNumber(100)
	print list
	print HumbleSort(list, 1000)
