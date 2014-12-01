print (r"""# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get: """,'\n')

readMe = open('exampleFile.txt','r').read()
print(readMe)

print ('\n\n# this will instead read the file into a python list.\n')
readMe = open('exampleFile.txt','r').readlines()
print(readMe)
