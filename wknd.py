##Given a signed 32 bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32 bit integer range [-2 31, 2 31, -1] then return 0

class Solution(object):
    def reverse(self, x):
        output = ""
	    for letter in str(x)[::-1]:
	        if letter == '-'
		        output = letter  + output
	        else:
		        output = output + letter
	        output = int(output)
            if output > (2*31-1) or output < (-2**31):
		        return 0
	        else:
	            return output

what = Solution()
print (what.reverse(-0463847412))

##27. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed. 
class Solution(object):
    def removeElement(self, nums, val):
	    while val in nums:
    	    nums.remove(val)
	    return len(nums)
what = Solution()
print(what.removeElement([2,3,3,3],3))

##67. Given two binary strings a & b, return their sum as a binary string

class Solution(object):
    def addBinary(self, a, b):
		return format(int(a, 2) + int (b, 2), "b")
what = Solution()
print(what.addBinary("1010", "0101"))

#9. Given an integer x, return true if x is palindrome integer. An integer is palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not 
class Solution(object):
    def isPalindrome(self, x):
    	return True if x == str(x)[::-1] else False

what = Solution()
print (what.isPalindrome(-121))
