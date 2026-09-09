class Solution(object):
    def climbStairs(self, n):
        a = 1
        b = 2
        
        if n==1:
            return a
        for i in range(3, n + 1):
            temp_a=a
            temp_b=b
            
            b=temp_a + temp_b
            a=temp_b

        return b
        