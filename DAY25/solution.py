def bubble_sort(list1, order):
    try:
        if order == "ascending":
            list1.sort(reverse=True)
            return list1

        elif order == "descending":
            list1.sort(reverse=False)
            return list1
    except:
        return 'Invalid Input'


print(bubble_sort(['x', 'c', 'b', 'v', 'z', 'a'], "descending"))
