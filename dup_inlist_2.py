from collections import Counter

nums = [1,1,1,2,2,3,3,3,4]
counts = Counter(nums)

seen = {}

for i in range(len(nums) - 1, -1, -1):
    num = nums[i]
    seen[num] = seen.get(num, 0) + 1
    if seen[num] > 2:
        del nums[i]        
        
print(nums)
