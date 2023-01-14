
def threeSum(arr):
    arr.sort()
    ans = []
    n = len(arr)
    i = 0
    while i < n and arr[i] < 1 :
        a = arr[i]
        l, r = i+1, n-1
        while l < r:
            if arr[l]+ arr[r] == -1*a:
                ans.append([a, arr[l], arr[r]])
                break
            elif arr[l]+ arr[r] > a:
                r -= 1
            else:
                l += 1
        i += 1

    return ans

arr = [-1,0,1,2,-1,-4]
arr2 = [0, 0, 0, 0]
print(threeSum(arr2))