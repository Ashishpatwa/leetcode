class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=[]
        for i in range(1,10):
            self.recursion(n,k,str(i),ans)
        return ans
    def recursion(self,n,k,tmp,ans):
        if len(tmp)==n:
            ans.append(int(tmp))
            return 0
        flag=int(tmp[-1])+k
        if flag<=9:
            self.recursion(n,k,tmp+str(flag),ans)
        flag2=int(tmp[-1])-k
        if k>0 and flag2>=0:
            self.recursion(n,k,tmp+str(flag2),ans)
#         ans=[]
#         for i in range(1,10):
#             self.recursion(n-1,k,i,ans)
#         return ans
    
#     def recursion(self,n,k,tmp,ans):
#         if n==0:
#             ans.append(tmp)
#             return 0
#         var=tmp%10

#         if var+k<=9:
#             self.recursion(n-1,k,tmp*10+(var+k),ans)
#         if k>0 and var-k>=0:
#             self.recursion(n-1,k,tmp*10+(var-k),ans)
    
    
            
        
        