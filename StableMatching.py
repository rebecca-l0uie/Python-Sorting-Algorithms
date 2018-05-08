#The Gale Shapley Algorithm - The Stable Marriage Algorithm
# Use dictionary
def dump(girl, husband, boy):
	herList=acceptor[girl]
	if herList.index(husband)>herList.index(boy):
		return True
	else:
		return False

Married={}
girls={'taylor':['zack','adam','jack','justin'],'adele':['zack','jack','adam','justin'],'selena':['justin','adam','jack','zack'],'nicki':['jack','justin','zack','adam']}
boys={'justin':['nicki','adele','taylor','selena'],'zack':['adele','taylor','selena','nicki'],'adam':['taylor','selena','adele','nicki'],'jack':['adele','nicki','selena','taylor']}                                                                                                                                                                                                                                                              
 
while len(Married)<len(boys):
	for boy in boys.keys():
		if boy not in Married.values():
			top=boys[boy].pop(0) #return an removes top girl
			if top in Married:
				H=Married[top]
				if dump(top,H, boy):
					Married[top]=boy # replace husband for boy
			else:
				Married[top]=boy
print Married
			
#while len in Married is not 4:
#	for B in boys:
#		G=boys[B].pop(0)
#		if G not in married:
#			M[G]= B
#		if Married.has_key(G):
#			H=Married[G]
#			if G.index(B)> G.index(H):
#				M[G]=B
#			else:
#				Married[top]=boy
#print Married
					
 
