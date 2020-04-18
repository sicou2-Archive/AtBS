def eggs(someParameter):
    someParameter.append('Hello')
    print(id(someParameter))

spam = [1,2,3]
print(id(spam))
eggs(spam)
print(spam)