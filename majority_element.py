from collections import Counter

nums = [1,1,2,3,2,1,1,1]

counts = Counter(nums)

n = len(nums)

for num ,freg in counts.items():
    if freg > n // 2:
        print(num)
        break