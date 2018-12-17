from itertools import permutations
n=int(input("Enter No.of Digits : "))
num=[]
for i in range(0,n):
	k=int(input("Enter The Number : "))
	num.append(k)
for i in range(0, len(num)+1):
	for subset in permutations(num, i):
		print(subset)
