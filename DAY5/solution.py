def fibonacci(number):
    list1 = [0, 1]
    a = 0
    b = 1
    if number < 0:
        return 'wrong input'
    elif number == 0:
        return a
    elif number == 1:
        return list1
    else:
        for i in range(number):
            c = a + b
            a = b
            b = c
            list1.append(c)
            if c > number:
                break
    list1.pop()  # Removes the last value on the list greater than number
    return list1


print(fibonacci(500))
