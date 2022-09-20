class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_g=[[-1]*(3) for i in range(len(prices)+1)]
        dp_f=[[-1]*(3)  for i in range(len(prices)+1)]
        
        def g(prices,i,k):
            if i==len(prices)-1:
                dp_g[i][k] = prices[i]
                return dp_g[i][k]
            if dp_g[i][k]!=-1:
                return dp_g[i][k]
            notsell=g(prices,i+1,k)
            sell=prices[i]+f(prices,i+1,k+1)
            dp_g[i][k] = max(notsell, sell)
            return dp_g[i][k]
        def f(prices,i,k):
            if k>1:
                return 0
            if i>=len(prices)-1:
                dp_f[i][k]= 0
                return dp_f[i][k]
            if dp_f[i][k]!=-1:
                return dp_f[i][k]
            notbuy=f(prices,i+1,k)
            buy=-prices[i]+g(prices,i+1,k)
            dp_f[i][k] = max(buy,notbuy)
            return dp_f[i][k]
        return f(prices,0,0)
        