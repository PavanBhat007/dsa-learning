"""
2574. Left and Right Sum Differences [Easy]

You are given a 0-indexed integer array nums of size n. Define two arrays leftSum and rightSum where:
- leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
- rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.
"""

#-------------------------------------------------------------------------------------------------------------------------

def leftAndRightSumDifferences(nums):
    n = len(nums)
    if n == 1:
        return [0]
    elif n == 2:
        return nums[::-1]
    
    answer = []
    for i in range(n):
        lSum = 0
        rSum = 0

        if i == 0:
            lSum = 0
        else:
            lSum = sum(nums[:i])
        
        if i == n-1:
            rSUm = 0
        else:
            rSum = sum(nums[i+1:])
        
        answer.append(abs(lSum - rSum))
    
    return answer

if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [int(x) for x in input("ARRAY: ").split(" ")]

    answer = leftAndRightSumDifferences(arr)
    print(f"Left and Right Sum differences for the array {arr} = {answer}")