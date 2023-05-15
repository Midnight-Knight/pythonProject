def pair(head, tail):
    return (head, tail)

def head(lst):
    return lst[0]

def tail(lst):
    return lst[1]

def is_empty(lst):
    return lst is None

def prepend(elem, lst):
    return pair(elem, lst)

def append(elem, lst):
    if is_empty(lst):
        return pair(elem, None)
    else:
        return pair(head(lst), append(elem, tail(lst)))

def length(lst):
    if is_empty(lst):
        return 0
    else:
        return 1 + length(tail(lst))

def reverse(lst):
    def reverse_helper(lst, result):
        if is_empty(lst):
            return result
        else:
            return reverse_helper(tail(lst), prepend(head(lst), result))
    return reverse_helper(lst, None)

def map_list(fn, lst):
    if is_empty(lst):
        return None
    else:
        return pair(fn(head(lst)), map_list(fn, tail(lst)))

def filter_list(pred, lst):
    if is_empty(lst):
        return None
    elif pred(head(lst)):
        return pair(head(lst), filter_list(pred, tail(lst)))
    else:
        return filter_list(pred, tail(lst))

def foldl_list(fn, acc, lst):
    if is_empty(lst):
        return acc
    else:
        return foldl_list(fn, fn(acc, head(lst)), tail(lst))

def foldr_list(fn, acc, lst):
    if is_empty(lst):
        return acc
    else:
        return fn(head(lst), foldr_list(fn, acc, tail(lst)))


if __name__ == "__main__":
    lst = pair(1, pair(2, pair(3, None)))

    print(head(lst))  # 1

    print(head(tail(lst)))  # 2

    lst = prepend(0, lst)
    print(head(lst))  # 0

    lst = append(4, lst)
    print(head(tail(tail(tail(tail(lst))))))  # 4

    print(length(lst))  # 5

    lst = reverse(lst)
    print(head(lst))  # 4

    lst = map_list(lambda x: x * 2, lst)
    print(head(lst))  # 8

    lst = filter_list(lambda x: x > 5, lst)
    print(head(lst))  # 8

    sum = foldl_list(lambda acc, x: acc + x, 0, lst)
    print(sum)  # 16

    product = foldr_list(lambda x, acc: x * acc, 1, lst)
    print(product)  # 8