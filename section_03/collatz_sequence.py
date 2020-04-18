def collatz(number):

    while number != 1:
        even_check = number%2
        if even_check == 0:
            number = number//2
            print(number)
            #return number
        else:
            number = 3*number + 1
            print(number)
            #return number
    print('Collatz Sequence complete')
    return 0

print('What number would you like to start the Collatz Sequence at?')
while True:
    try:

        start_number = int(input('> '))
        collatz(start_number)
        break
    except:
        print('Please only enter numberic digits.')
        pass
