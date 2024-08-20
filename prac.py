# find if the arr 2 is the subset of an array

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


# find if there are two equal numbers present and distance is less than or equal to k

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
 


#  Count all the (i,j) Pairs such that b[i] + b[j] == k (count of such pairs.) [i<j] 

def count_pairs_of_sum(arr, k ):
    count = 0
    seen = {}

    for num in arr:
        complement_number = k - num #6-1 = 5 / 6-2 = 4 / 6-3=3 / 6-4=2 / 6-5=1 
        if complement_number in seen:
            count +=1
            print(complement_number, seen)
        seen[num] = True
        print(seen)
    return count





if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 6
    count = count_pairs_of_sum(arr, k)
    print(f'Count of pairs with sum {k} is {count}')



#Count All ((i,j) pairs such that b[i] - b[j] == k (count of such pairs.) [i<j] 

from collections import defaultdict
 
def count_pairs_optimized(b, k):
    count = 0
    freq_map = defaultdict(int)
    for num in b:
        target = num + k
        count += freq_map[target]
        freq_map[num] += 1
    return count
 
def main():
    b = [1, 5, 3, 4, 2]
    k = 2
    print("Count of pairs:", count_pairs_optimized(b, k))
 
if __name__ == "__main__":
    main()
 

 #brute
def count_pairs_brute_force(b, k):
    count = 0
    n = len(b)
    for i in range(n):
        for j in range(i + 1, n):
            if b[i] - b[j] == k:
                count += 1
    return count
 
b = [1, 5, 3, 4, 2]
k = 2
print("Count of pairs:", count_pairs_brute_force(b, k))
 



 #sum of target present in the array
def twoSum(nums, target):
	hm = dict()
	for i, v in enumerate(nums):# print(enumerate(nums))
		if target - v in hm:
			return [hm[target - v], i]
		else:
			hm[v] = i
 
	return [-1, -1]
 
 #{1:2, 2:7, 3:11, 4:15}
nums = [2,7,11,15]
target = 18
 
print(twoSum(nums, target))