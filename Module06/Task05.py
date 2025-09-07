def remove_odd(numbers):
    new_list = []
    for n in numbers:
        if n % 2 == 0:
            new_list.append(n)
    return new_list

nums = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = remove_odd(nums)
print(nums)
print(filtered)
