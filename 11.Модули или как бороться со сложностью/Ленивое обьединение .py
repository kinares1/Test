import itertools

def concatenate_lists(list1, list2):
    return list(itertools.chain(list1, list2))
result = concatenate_lists([1, 2], [3, 4])
print(result)


"""Эта функция принимает два списка, list1 и list2, и использует функцию itertools.chain() для объединения их в один список."""
