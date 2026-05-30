"""
961. N-Repeated Element in Size 2N Array [Easy]

You are given an integer array nums with the following properties:
    - nums.length == 2 * n.
    - nums contains n + 1 unique values, n of which occur exactly once in the array.
Exactly one element of nums is repeated n times. Return the element that is repeated n times.
"""

#-------------------------------------------------------------------------------------------------------------------------

def nRepeatedElement(nums):
    n = len(nums)/2
    occurences = {}

    for num in nums:
        try:
            num_occurences = occurences[num] # will throw KeyError if first time seeing number
            if (num_occurences+1) == n:
                # num occurred n-1 times before and counting current = n 
                return num
            else:
                # num has occurred < n-1 times till now, so increment occurence count
                occurences[num] += 1
        except KeyError as e:
            # first time finding this num
            occurences[num] = 1

if __name__ == "__main__":
    n = int(input("ARRAY LEN (2n): "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]

    answer = nRepeatedElement(arr)
    print(f"Element {answer} occurred {int(n/2)} times in array.")