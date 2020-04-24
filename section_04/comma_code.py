spam = ['apples', 'bananas', 'tofu', 'cats', 'that', 'simply', 'fun', 'cheese']
bacon =''
for item in spam:
    if (item == spam[-1]):
        bacon += 'and ' + item + '.'

    else:
        bacon += item + ', '
print(bacon)