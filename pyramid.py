l = input()
l.split()
l1 = []
for i in l:
	l1.append(i)
num = 1
for j in range(0, len(l1)+1):
	num = 1
	for k in range(j+1, len(l1)):
		print(num, end = " ")
		num = num + 1
	print("\r")


 
   
      
      
     
       



