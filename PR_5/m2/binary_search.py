def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == '__main__':
    arr = list(map(int, input("Введите список чисел через пробел: ").split()))
    x = int(input("Введите число для поиска: "))
    index = binary_search(arr, x)
    if index != -1:
        print(f"Число {x} найдено в позиции {index}.")
    else:
        print(f"Число {x} не найдено в списке.")