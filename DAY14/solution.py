import random


def guess(number):
    list1 = []
    for i in range(1, 51):
        list1.append(i)

    check_in = random.choice(list1)
    print(check_in)
    if str(check_in) == str(number):
        print(' correct answer')

    elif str(number) > str(check_in) :
        print('Wrong. The answer is less than ', number)

    elif str(number) < str(check_in):
        print('Wrong. The answer is greater than ', number)


count = 0
while count < 6:
    guess(input('Guess a number between (1-50): '))
    count += 1
