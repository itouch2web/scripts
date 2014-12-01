print ('####String and input#### \n\n')
name = str(input('Hello, \nPlease type your name: '))
print('Ok.',name,',')

unit3Done = str(input('Have you done your Unit 3 Controlled Assessment? (Type y or n): ')).lower()
if unit3Done == 'y':
    pass
elif unit3Done == 'n':
    print ('Sorry ',name,',', 'You must have done at least one unit.')
else:
    print ('Sorry',name,'That\'s not a valid answer.')

print ('\n\n####LOOPS#### \n')
print ('\n\n####for...[1,2,3,4,5]#### \n')
for i in [1,2,3,4,5]:
	print (i)
print ('\nfor... range(4,9)')
for i in range(4,9):
	print (i)
		
print ('\n#for and range...range(5)#\n')

for i in range(5):
	print (i)

