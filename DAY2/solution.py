from collections import Counter
def list_to_set(list0):
    list1 = []

    count = Counter(list0)
    mode_ = dict(count)
    mode = [j for j, v in mode_.items() if v == max(list(count.values()))]
    for i in list0:
        if i not in list1:
            list1.append(i)
    return list1, mode

y = list_to_set([1,1,1,2,2,2,5,3,'bayo','bayo','bayo'])
print(y)
