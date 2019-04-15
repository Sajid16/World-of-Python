list = [1,2,3,4,5,6]
print(list)

test = list[2:5]
print(test)

test.append(8)
print(test)

test.append(10)
print(test)

print(len(test))

l = len(test)
test[l:] = [12, 13, 45]
print(test)
