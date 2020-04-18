def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        #print('Error: Invalid argument')
        return 'Error: Invalid argument' # Got it, this has to return something and
        # instead of None from above line you get the prefered message

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))