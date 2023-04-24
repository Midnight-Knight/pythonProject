import random

def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        counts[x] += 1

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend([i] * counts[i])

    return sorted_arr

def test_bucketsort():
    for i in range(10):
        n = random.randint(0, 100)
        arr = [random.randint(0, 9) for j in range(n)]
        sorted_arr = bucketsort(arr, 10)
        assert sorted_arr == sorted(arr)

if __name__ == "__main__":
    test_bucketsort()
