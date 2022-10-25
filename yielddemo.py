def create_list(num):
    for i in range(num):
        yield i
    
listvalue = create_list(4)
print("Value: ", list(listvalue))
print(create_list(4))
