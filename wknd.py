##Given a signed 32 bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32 bit integer range [-2 31, 2 31, -1] then return 0

class Solution(object):
    def reverse(self, x):
        output = ""
        for letter in str(x)[::-1]:
            if letter == '-':
                output = letter  + output
            else:
                output = output + letter
            output = int(output)
            if output > (2*31-1) or output < (-2**31):
                return 0
            else:
                return output

# what = Solution()
# print(what.reverse(0,4,6,3,8,4,7,4,1,2))

##27. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed. 
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
# what = Solution()
# print(what.removeElement([2,3,3,3],3))

##67. Given two binary strings a & b, return their sum as a binary string

class Solution(object):
    def addBinary(self, a, b):
	    return format(int(a, 2) + int (b, 2), "b")
# what = Solution()
# print(what.addBinary("1010", "0101"))

#9. Given an integer x, return true if x is palindrome integer. An integer is palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not 
class Solution(object):
    def isPalindrome(self, x):
    	return True if x == str(x)[::-1] else False

# what = Solution()
# print (what.isPalindrome(-121))

#3n + 1
#Take a positive integer starting at even or odd, if the number is even divide it by two, if it is odd perform the calculation 3N + 1. 
# After this, take the product of that calculation and repeat the process

def collatz_sequence(x):
    seq = []
    while True:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        seq.append(x)
        if x < 2: break
    
    return seq 

# print(collatz_sequence(0))
# print(collatz_sequence(1))
# print(collatz_sequence(4))
# print(collatz_sequence(5))
# print(collatz_sequence(6))


def find_outlier(integers):
    even_count = 0
    odd_count = 0

    for i in range(0, 3, 1):
        if integers[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    type= 'even' if even_count > odd_count else 'odd'

    for num in integers:
        if type == 'even':
            if(num % 2 == 1):
                return num
        else:
            if(num % 2 == 0):
                return num
print(find_outlier([1, 2, 4, 6, 8, 2]))
