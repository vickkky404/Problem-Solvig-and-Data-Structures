class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculate the number of distinct ways to climb a staircase with n steps.
        You can climb either 1 or 2 steps at a time.
      
        This uses dynamic programming with space optimization.
        The solution is based on the Fibonacci sequence pattern.
      
        Args:
            n: The total number of steps in the staircase
          
        Returns:
            The number of distinct ways to reach the top
        """
        prev_prev, prev = 0, 1
      
        
        for _ in range(n):
           
            prev_prev, prev = prev, prev_prev + prev
              return prev
