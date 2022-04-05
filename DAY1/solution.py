"""List into list"""
def list_to_set(list0):
    list1 = []
    for i in list0:
        if i not in list1:
            list1.append(i)
    return list1


y = list_to_set([1,2,3,3])
print(y)


"""list into set """
def list_to_set(list0):
    list1 = []
    for i in list0:
        list1.append(i)
    list2 = set(list1)
    return list2


y = list_to_set([1,2,3,3,'dad','dad'])
print(y)
