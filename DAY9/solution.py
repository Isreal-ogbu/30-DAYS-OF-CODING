def is_prime(number):
    list_check = [2, 3, 5, 7, 11]
    if number in list_check:
        print(number, 'is a prime number')
    elif number <= 1:
        print(number, 'is not a prime number')
        pass
    else:
        if number % 2 == 0 or number % 3 == 0:
            print(number, 'is not a prime number')
            pass
        elif number % 5 == 0 or number % 7 == 0:
            print(number, 'is not a prime number')
            pass
        elif number % 11 == 0:
            print(number,'is not a prime number')
            pass
        else:
            print(number, 'is a prime number')


is_prime(97)
