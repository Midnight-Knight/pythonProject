def binary_search(arr, x):
    left = 0
    right = len(arr) - 1 # исправлено, чтобы правый индекс был включен в диапазон
    while left <= right:
        mid = (left + right) // 2 # использовано целочисленное деление
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1 # исправлено, чтобы правый индекс был правильным
    return -1

if __name__ == '__main__':
    # добавлен ввод списка и искомого элемента от пользователя
    arr = list(map(int, input("Введите список чисел через пробел: ").split()))
    x = int(input("Введите число для поиска: "))
    index = binary_search(arr, x)
    if index != -1:
        print(f"Число {x} найдено в позиции {index}.")
    else:
        print(f"Число {x} не найдено в списке.")