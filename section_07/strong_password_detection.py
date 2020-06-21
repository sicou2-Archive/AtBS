import re

lower_re = re.compile(r'[a-z]+')
upper_re = re.compile(r'[A-Z]+')
number_re = re.compile(r'[0-9]+')
length_re = re.compile(r'\w{8,}')

passwords = ['ASDF0987', 'asdf0987', 'asdfASDF', 'asAS09', 'Aa9Ss0Dd8Ff7'
'GDFPVP', 'IJJOULWDRNW', 'vLTTkdzZoWp', 'MvcNGck', 'jd1WS2v', 't4BSE5JPRmijlr',
'iq9p03iyskwjjl', 'ztdsiykhqaabbz', 'M3DnSXGQ4vmOdz3KMV6DjPuJdY',
'vouzsSU87wDUW8FnhPs', 'nvh4YTFUcUEA9G', 'jKck7DWJ', 'UHJHAe']
good_passwords = []
for password in passwords:
    print(password)
    pw_match = []
    mo1 = lower_re.search(password)
    mo2 = upper_re.search(password)
    mo3 = number_re.search(password)
    mo4 = length_re.search(password)

    if mo1:
        pw_match.append(mo1.group)
        print(mo1.group())
    if mo2:
        pw_match.append(mo2.group)
        print(mo2.group())
    if mo3:
        pw_match.append(mo3.group)
        print(mo3.group())
    if mo4:
        pw_match.append(mo4.group)
        print(mo4.group())

    if len(pw_match) == 4:
        good_passwords.append(password)
print(good_passwords)
