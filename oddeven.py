list = []
for i in range(0,10):
	list.append(i)
oddArray = []
evenArray = []
for d in list:
	if(d % 2 == 0):
		evenArray.append(d)
	else:
		oddArray.append(d)
#print("evenArray")
#print("oddArray")
print(evenArray)
print(oddArray)
