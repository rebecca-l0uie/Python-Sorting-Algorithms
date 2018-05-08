import random
# Circa Feburary 2016

def insort(l)
	n=[l.pop()] #makes n not empty
	while l!=[]:
		x=l.pop()
		for i in range(len(n)):
			if x <n[i]:
				n.insert
				break
			if (i==len(n)-1)
				n.insert(i+1,x)
	return n
	
a=[3,2,5,9,8,1,4,7,6]
print insort(a)
