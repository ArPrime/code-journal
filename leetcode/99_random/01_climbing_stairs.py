'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''


class Solution:
    # method 1
    @staticmethod
    def climbStairs_recursive(n: int) -> int:
        if n <= 2:
            return n

        return Solution.climbStairs_recursive(n-1) + Solution.climbStairs_recursive(n-2)
    
    # method 2
    @staticmethod
    def climbStairs_memo(n: int) -> int:
        memo = {}
        def helper(n: int) -> int:
            if n <= 2:
                return n
            elif n in memo:
                return memo[n]
            else:
                memo[n] = helper(n-1) + helper(n-2)
                return memo[n]
            
        return helper(n)
    
    # method 3
    @staticmethod
    def climbStairs_dp(n: int) -> int:
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    # method 4
    @staticmethod
    def climbStairs_optimized(n: int) -> int:
        if n <= 2:
            return n
        prev_2 = 1
        prev_1 = 2
        for i in range(3, n+1):
            current = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = current
        return current

sol = Solution()
test_number = 4
print(sol.climbStairs_optimized(4))