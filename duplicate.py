l = [1, 1, 2, 2, 3, 3]
count = 0
for i in l:
	for j in l:
		
		if(i == j):		
			count = count + 1
		else:
			count = count
print(count)

