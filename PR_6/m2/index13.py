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

def make_list(*args):
    if not args:
        return None
    else:
        return pair(args[0], make_list(*args[1:]))

def list_to_string(lst):
    if lst is None:
        return ""
    else:
        return str(head(lst)) + " " + list_to_string(tail(lst))

def list_range(low, high):
    if low > high:
        return None
    else:
        return pair(low, list_range(low + 1, high))

def foldl(func, lst, acc):
    if lst is None:
        return acc
    else:
        return foldl(func, tail(lst), func(acc, head(lst)))

def list_sum(lst):
    return foldl(lambda acc, x: acc + x, lst, 0)

def fact(n):
    lst = list_range(1, n)
    return foldl(lambda acc, x: acc * x, lst, 1)

def list_to_py(lst):
    return foldl(lambda acc, x: acc + [x], lst, [])

def list_reverse(lst):
    return foldl(lambda acc, x: pair(x, acc), lst, None)

def foldr(func, lst, acc):
    if lst is None:
        return acc
    else:
        return func(head(lst), foldr(func, tail(lst), acc))

def list_map(func, lst):
    return foldr(lambda x, acc: pair(func(x), acc), lst, None)

def list_filter(pred, lst):
    return foldr(lambda x, acc: pair(x, acc) if pred(x) else acc, lst, None)

def sum_odd_squares(lst):
    odd_numbers = list_filter(lambda x: x % 2 == 1, lst)
    odd_squares = list_map(lambda x: x ** 2, odd_numbers)
    return list_sum(odd_squares)



if __name__ == "__main__":
    lst = pair(1, pair(2, pair(3, pair(4, pair(5, None)))))
    result = sum_odd_squares(lst)
    print(result)  


