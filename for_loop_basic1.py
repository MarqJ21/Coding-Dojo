from itertools import count


for i in range(151):
    print(i)

for i in range(5, 1000):
    if (i % 5) == 0:
        print(i)

for i in range(1, 100):
    if (i % 10) == 0:
        print("Coding Dojo")
    elif (i % 5) == 0:
        print("Coding")
    else:
        print(i)

for i in range(500000):
    if (i % 2) != 0:
        print(i)

i = 2018
# while i > 0:
#     print (i)
#     i -= 4

# lowNum = 2
# highNum = 10
# mult= 3

# for i in range(lowNum, highNum):
#     if (i % 3) == 0:
#         print(i)

import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')
