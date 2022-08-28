class Solution:
    def numDecodings(self, s: str) -> int:
        visited=[False]*(len(s)+1)
        dp=[-1]*(len(s)+1)
        ans=self.recursion(s,0,visited,dp)
        return ans if visited[len(s)] else 0
    def check(self,s,i):
        if int(s[i]+s[i+1])<27:
            return True
        return False
    def recursion(self,s,i,visited,dp):
        if i==len(s):
            visited[i]=True
            return 1
        if s[i]=='0':
            return 0
        if dp[i]!=-1:
            return dp[i]
        
        if i+1<len(s) and self.check(s,i):
            dp[i]= self.recursion(s,i+1,visited,dp)+self.recursion(s,i+2,visited,dp)
            return dp[i]
        dp[i]=self.recursion(s,i+1,visited,dp)
        return dp[i]
            
            
        
        
        
        
        
        
#         self.count=0
#         self.recursion(s,0,[[]],count)
#         return self.count
#     def recursion(self,s,i,tmp,count):
      
#         if i==len(s):
#             print(tmp)
#             self.count+=1
#             return
#         tmp1=copy.deepcopy(tmp)
#         tmp2=copy.deepcopy(tmp)
        
        
#         if len(tmp1[-1])<2:
#             if len(tmp1[-1])==0:
#                 if int(s[i])!=0:
#                     tmp1[-1].append(int(s[i]))
#                     self.recursion(s,i+1,tmp1,count)
#             elif tmp1[-1][0]<3 and int(s[i])<7:
#                 tmp1[-1].append(int(s[i]))
#                 self.recursion(s,i+1,tmp1,count)
        
#         #not_taken
        
#         if len(tmp2[-1]) and int(s[i])!=0:
#             tmp2.append([int(s[i])])
            
#             self.recursion(s,i+1,tmp2,count)
        
        
    #     self.count=0
    #     ans=[]
    #     self.recursion([],0,s,ans)
    #     print(self.count,ans)
    #     return 0 if self.count==len(ans)else len(ans)
    # def recursion(self,arr,i,s,ans):
    #     if i==len(s):
    #         if arr:
    #             ans.append(arr)
    #         return
    #     arr1= copy.deepcopy(arr)
    #     arr2=copy.deepcopy(arr)
    #     if int(s[i])>0:
    #         arr1.append([int(s[i])])
    #     else:
    #         arr1=[]
    #     if arr2:
    #         temp=arr2[-1][0]*10+int(s[i])
    #         if temp<27:
    #             c=temp+int(s[i])
    #             arr2.pop()
    #             arr2.append([c])
    #             self.recursion(arr2,i+1,s,ans)
    #     self.recursion(arr1,i+1,s,ans)