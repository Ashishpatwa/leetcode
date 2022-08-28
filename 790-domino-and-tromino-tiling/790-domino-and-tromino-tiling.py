class Solution:
    def numTilings(self, n: int) -> int:
        dp=[-1]*(n+3)
        return self.f(n,dp)
    def f(self,n,dp):
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        if dp[n]!=-1:
            return dp[n]
        dp[n]=2*self.f(n-1,dp)+self.f(n-3,dp)
        return dp[n]%1000000007