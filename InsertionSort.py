import random

def insort(l):
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

