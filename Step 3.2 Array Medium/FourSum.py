def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n-3):
        if i != 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n-2):
            if j != i+1 and nums[j] == nums[j-1]:
                continue
            target2 = target - nums[i] - nums[j]
            l, r = j+1, n-1
            while l < r:
                if nums[l] + nums[r] > target2:
                    r -= 1
                elif nums[l] + nums[r] < target2:
                    l += 1
                else:
                    ans.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+= 1
    return ans


nums = [2,2,2,2,2]
nums2 = [1,0,-1,0,-2,2]
target = 8
target2 = 0
print(fourSum(nums2, target2))