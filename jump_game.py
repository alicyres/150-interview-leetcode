nums = [2,0,0,1,4]

farthest = 0

for i in range(len(nums)):
    if i > farthest:
        print("False")
    farthest = max(farthest, i + nums[i])
