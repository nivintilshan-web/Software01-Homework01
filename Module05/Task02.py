nums = []
while True:
    x = input("Enter a number (empty to quit): ")
    if x == "":
        break
    nums.append(int(x))

nums.sort(reverse=True)
for i in range(min(5, len(nums))):
    print(nums[i])
