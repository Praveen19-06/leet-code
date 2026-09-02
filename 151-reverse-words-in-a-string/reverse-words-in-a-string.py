class Solution(object):
    def reverseWords(self, s):
    
        a=s.split()
        ans=a[::-1]

        return " ".join(ans)
        