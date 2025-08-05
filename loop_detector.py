
def has_loop(arr: list[int]) -> bool:

    for num in arr:
        if num > arr[-1]:
            return True

    return False
#result = has_loop([1, 2, 3, 4, 2])
#result = has_loop([1, 2, 3, 4, 5])
#result = has_loop([3, 2, 1, 6])
#result = has_loop([1, 0])
result = has_loop([0])
print(result)
