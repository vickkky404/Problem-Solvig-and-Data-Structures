	# Recursive Solution

class Solution:

	    def climbStairs(self, n: int) -> int:

	        if n == 1:

	            return 1

	        if n == 2:

	            return 2

	        

	        return self.climbStairs(n-2) + self.climbStairs(n-1)

	        # Time: O(2^n)

	        # Space: O(n)

	 
