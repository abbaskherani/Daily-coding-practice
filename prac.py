def isSubset(arr1, n1, arr2, n2):
    mp = {}
    for i in range(n1):
        if arr1[i] in mp:
            mp[arr1[i]] += 1
        else:
            mp[arr1[i]] = 1
    print(mp)
    for i in range(n2):
        if arr2[i] not in mp or mp[arr2[i]] == 0:
            print(arr2)
            return False
        mp[arr2[i]] -= 1
        print(mp)
    return True
 
arr1 = [6, 7,2, 3, 2]
arr2 = [6, 7, 2, 2]
n1 = len(arr1)
n2 = len(arr2)
 
if isSubset(arr1, n1, arr2, n2):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is not a subset of arr1")



def contains_nearby_duplicate_optimized(nums, k):
    num_indices = {}
    for i, num in enumerate(nums):
        print(i, num)
        if num in num_indices and i - num_indices[num] <= k:
            return True
        num_indices[num] = i
        print(num_indices)
    return False
 
def main():
    nums = [1, 3,2, 1, 2, 3]
    k = 2
    if contains_nearby_duplicate_optimized(nums, k):
        print("There are two equal numbers within distance", k)
    else:
        print("No two equal numbers found within distance", k)
 
if __name__ == "__main__":
    main()
 