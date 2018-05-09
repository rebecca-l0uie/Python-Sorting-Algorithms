import random
'''
def insort(L): #By Robert Arkelitian
	n = [L.pop()]			#Makes n not empty
	while L!=[]:
		x = L.pop()
		for i in range(len(n)):
			if x < n[i]:
				n.insert(i,x)
				break
			if ( i == len(n) -1):
				n.insert(i+1,x)
	return n
'''

def insort(l): #By Ben Chapman-Kish
	n = [l.pop()]
	while len(l) > 0:
		x = len(n)
		while l[-1] < n[x-1] and x > 0:
			x -= 1
		n.insert( x, l.pop())
	return n


a = []
for x in range(10):
	a.append(random.choice(range(100)))
b = insort(a)
print b

