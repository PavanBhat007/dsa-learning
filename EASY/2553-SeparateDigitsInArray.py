"""
2553. Separate the Digits in an Array [Easy]

Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums 
after separating them in the same order they appear in nums.
To separate the digits of an integer is to get all the digits it has in the same order.
"""

#-------------------------------------------------------------------------------------------------------------------------

def separation(num):
    digits = []

    if num > 9:
        while num != 0:
            rem = num%10
            digits.append(rem)
            num = int(num/10)
    else:
        digits.append(num)
        
    digits.reverse()
    return digits

def separate_digits_in_array(nums):
    separated = []

    for num in nums:
        separated += separation(num)
    
    return separated

if __name__ == "__main__":
    n = int(input("ARRAY LEN: "))
    arr = [ int(x) for x in input("ARRAY: ").split(" ") ]

    digits_array = separate_digits_in_array(arr)
    print(f"Separated digits of given array: {digits_array}")