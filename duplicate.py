l = [1, 1, 2, 2, 2, 2, 3]
k = []
q = []

for data in l:
	if data not in k:
		k.append(data)
		q.append(l.count(data))
count = 0
for j in q:
	if(q[j] % 2 == 0):
		count = count + 1
print(q)
		

