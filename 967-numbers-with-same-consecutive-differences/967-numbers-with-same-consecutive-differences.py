class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans=set()
        tmp=[]
        for i in range(1,10):
            if i<k and k+i<=9:
                tmp.append(str(i))
                self.recursion(n,k,tmp,ans)
            elif i>=k:
                tmp.append(str(i))
                self.recursion(n,k,tmp,ans)
            tmp=[]
        return list(ans)
    def recursion(self,n,k,tmp,ans):
        if len(tmp)>n:
            return 0
        if len(tmp)==n:
            ans.add(int("".join(tmp)))
            return 0
        if int(tmp[-1])+k<=9:
            tmp.append(str(int(tmp[-1])+k))
            self.recursion(n,k,tmp,ans)
            tmp.pop()
        if int(tmp[-1])-k>=0:
            tmp.append(str(int(tmp[-1])-k))
            self.recursion(n,k,tmp,ans)
            tmp.pop()
            
        
        