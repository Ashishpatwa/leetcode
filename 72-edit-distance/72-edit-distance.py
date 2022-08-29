class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(word1)
        n=len(word2)
        dp=[[-1]*(n+1) for i in range(m+1)]
        return self.recursive(word1,word2,m,n,dp)
    def recursive(self,word1,word2,m,n,dp):
        if n==0:
            dp[m][n]=m
            return m
        if m==0:
            dp[m][n]=n
            return n
        if dp[m][n]!=-1:
            return dp[m][n]
        if word1[m-1]==word2[n-1]:
            dp[m][n]=self.recursive(word1,word2,m-1,n-1,dp)
            return dp[m][n]
        else:
            dp[m][n]=1+min(self.recursive(word1,word2,m-1,n-1,dp),min(self.recursive(word1,word2,m-1,n,dp),self.recursive(word1,word2,m,n-1,dp)))
            return dp[m][n]
        