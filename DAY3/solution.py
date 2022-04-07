"""day3 : palindrome """
def palindrome(value):
    emp_list = []
    for i in range(value):
        num = i
        reverse = 0

        while num > 0:
            remainder = num % 10
            reverse = (reverse * 10) + remainder
            num = num // 10

        if i == reverse:
            emp_list.append(i)
    print(emp_list)
    print('\nThe total number of all palendrone less than ' + str(value) + ' is : ' + str(len(emp_list)))
palindrome(500)
