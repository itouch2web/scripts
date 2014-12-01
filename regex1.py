import re
print ('#### Regex #### \n')
string = "Once you have accomplished small things, you may attempt great ones safely."
print ('\n')
print ('String =',string)
# Return all words beginning with character 'a', as a list of strings
x =  re.findall(r"\ba[\w]*", string)
print ('\n')
print (x)
# ['accomplished', 'attempt']

# Return all words beginning with character 'a', as an iterator yielding match objects
it = re.finditer(r"\ba[\w]*", string)
for match in it:
    y =  "'{g}' was found between the indices {s}".format(g=match.group(), s=match.span())
print ('\n')
print (y)
# 'accomplished' was found between the indices (14, 26)
# 'attempt' was found between the indices (49, 56)



# Split string by any character which is not a UNICODE word character
z =  re.split("\W+", string)
print ('\n')
print (z)
# ['Once', 'you', 'have', 'accomplished', 'small', 'things', 'you', 'may', 'attempt',
# 'great', 'ones', 'safely', '']

# Split string by any character which is not a UNICODE word character at most 2 split
p =  re.split("\W+", string, 2)
print ('\n')
print (p)
# ['Once', 'you', 'have accomplished small things, you may attempt great ones safely.']

# If the splitting pattern does not occur in the string,
# string is returned as the first element of the list
q =  re.split("(:)", string)
print ('\n')
print (q)
# ['Once you have accomplished small things, you may attempt great ones safely.']



# Replace all occurrences of space, comma, or dot with colon
r =  re.sub("[ ,.]", ":", string)
print ('\n')
print (r)
# Once:you:have:accomplished:small:things::you:may:attempt:great:ones:safely:

# Replace maximum 2 occurences of pattern
s =  re.sub("[ ,.]", ":", string, 2)
print ('\n')
print (s)
# Once:you:have accomplished small things, you may attempt great ones safely.

# Replace as 'sub', but return a tuple of (new string, number of replacements)
t = re.subn("[ ,.]", ":", string)
print ('\n')
print (t)
# ('Once:you:have:accomplished:small:things::you:may:attempt:great:ones:safely:', 13)



# Find all five characthers long words
u =  re.findall(r"\b\w{5}\b", string)
print ('\n')
print (u)
# ['small', 'great']

# Find all five, six, or seven characthers long words
v = re.findall(r"\b\w{5,7}\b", string)
print ('\n')
print (v)
# ['small', 'things', 'attempt', 'great', 'safely']

# Find all words which are at least 8 characters long
z = re.findall(r"\b\w{8,}\b", string)
print ('\n')
print (z)
# ['accomplished']

