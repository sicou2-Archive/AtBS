import random

number_of_streaks = 0
trials = 10_000_000
coin = ['heads', 'tails']
#six_flips = ''
#data = []
for experimentNumber in range(trials):

    six_flips = ''
    for trial in range(6):
        six_flips += f"{random.choice(coin)} "

#    if ('heads heads heads heads heads heads' or 'tails tails tails tails tails tails') in six_flips:
    if 'heads heads heads heads heads heads' in six_flips or 'tails tails tails tails tails tails' in six_flips:
        number_of_streaks += 1
#    if 'tails tails tails tails tails tails' in six_flips:
#        number_of_streaks += 1
#    data.append(six_flips)

#for i in data:
 #   if 'heads heads heads heads heads heads' in i:
  #      number_of_streaks += 1

#print(data)
print(number_of_streaks)
print((number_of_streaks/trials)*100)





#coin = ['heads', 'tails']

#flip = 0

#while len(flip_list) != 6