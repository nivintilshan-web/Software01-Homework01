def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [3, 5, 7, 2, 8]
result = sum_list(nums)
print(result)
