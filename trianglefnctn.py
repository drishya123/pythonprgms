l = [5, 0, 2]
def triangle():
	if(l[0] + l[1] > l[2]) and (l[1] + l[2] > l[0]) and (l[2] + l[0] > l[1]):
		print ("correct edges of the triangle")
	else:
		print ("wrong edges of the triangle")
triangle()
	
	
