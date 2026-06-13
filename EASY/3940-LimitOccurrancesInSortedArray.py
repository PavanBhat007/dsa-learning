"""
3940. Limit Occurrences in Sorted Array [Easy]

You are given a sorted integer array nums and an integer k.
Return an array such that each distinct element appears at most k times, while preserving the relative order of the elements in nums.

Note: If a distinct element appears at least k times, then it must appear exactly k times in the resulting array.
"""

#-------------------------------------------------------------------------------------------------------------------------

def limitOccurrences(nums, k):
    if len(nums) == 1:
        return nums

    prev = nums[0]
    ctr = 0

    answer = []
    for i in range(1, len(nums)):
        curr = nums[i]
        if curr == prev:
            ctr += 1

            if ctr <= k:
                answer.append(prev)
        else:
            if ctr < k:
                answer.append(prev)
            ctr = 0

        prev = curr
        if i == len(nums) - 1 and ctr < k:
            answer.append(prev)

    return answer

if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]
    k = int(input("LIMIT: "))

    answer = limitOccurrences(arr, k)
    print(f"ANSWER: {answer}")