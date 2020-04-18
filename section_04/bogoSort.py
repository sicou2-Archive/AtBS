import random

name = ['alice', 'bob', 'carol', 'david']
i = 0

old_name = name[:]
random.shuffle(name)
print(name == old_name)
print(name, old_name)

while name != old_name:

    random.shuffle(name)
    print(name == old_name)
    print(name, old_name)
    print(i)
    i += 1

