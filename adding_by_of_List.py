def add_num(n):
    return lambda x:x+n
#print(add_num(14))
add_num = lambda n :lambda x:x+n
add_num=add_num(1)
print(add_num(3))