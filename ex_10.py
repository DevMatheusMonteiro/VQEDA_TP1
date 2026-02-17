def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

print(bubble_sort(["z", "f", "a", "b"]))
print(bubble_sort(["maça", "uva", "banana", "laranja"]))
print(bubble_sort(["God of War", "Assassins Creed", "Spider Man", "The Last of Us"]))