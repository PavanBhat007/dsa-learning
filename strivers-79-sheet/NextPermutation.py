"""
    31. Next Permutation [MEDIUM]

    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
    More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
    then the next permutation of that array is the permutation that follows it in the sorted container. 
    If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.
"""

"""
--- ALGORITHM ---

ind = -1
for i = n-2 to 0 {
  if arr[i] < arr[i+1] {
    ind = i
    break
  }
}

if ind = -1 => reverse the array because arr is already biggest and reverse(arr) = smallest

for i = n-1 to 0 {
  if arr[i] > arr[ind] {
    swap arr[i] and arr[ind]
    break
  }
}

reverse arr from ind+1 to n-1
"""

def reverse_array(arr, start, end):
  while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1

  return arr

def next_permutation(n, arr):
  # find breakpoint index where dip is found in increasing curve
  # i.e., find the longest prefix possible
  ind = -1
  for i in range(n-2, -1, -1): # n-1 to 0
    if arr[i] < arr[i+1]:
      ind = i # breakpoint found
      break
  
  # if no breakpoint => arr is largest => reverse to get smallest which is the solution
  if ind == -1:
    arr = reverse_array(arr, 0, n-1)
    return arr

  # find smallest element from right side of breakpoint
  for i in range(n-1, ind, -1): # n-1 to ind+1
    if arr[i] > arr[ind]:
      # swap smallest on right side and breakpoint element
      arr[i], arr[ind] = arr[ind], arr[i]

  # reverse the right side of array to smallest value
  arr = reverse_array(arr, ind+1, n-1)
  return arr

if __name__ == "__main__":
  n = int(input("SIZE: "))
  arr = [int(x) for x in input("ARRAY: ").strip().split(" ")]

  next_perm = next_permutation(n, arr)
  print(next_perm)