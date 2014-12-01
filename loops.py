print ('\n\n####LOOPS#### \n')
zahl = int(input('Deine zahl: '))
for i in range(1,11):
    print(i,'x',zahl,'   =',i * zahl)

print ('\n\n####for...[1,2,3,4,5]#### \n')
for i in [1,2,3,4,5]:
	print (i)
	
print ('\n#for and range...range(5)#\n')

for i in range(5):
	print (i)
print ('\nfor... range(4,9)')
for i in range(4,9):
	print (i)

	
print ('\n#for and range with range(0,20,3)#\n')

for i in range(0,20,3):
	print (i)
		
print ('\n#while x <=5:#\n')
x=0
while x <=5:
    print (x)
    x +=1

