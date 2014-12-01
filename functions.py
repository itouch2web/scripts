x = 6
def example(modify):
 
    print(modify)
    modify+=5
    print(modify)
    return modify
 
x = example(x)
print(x)
