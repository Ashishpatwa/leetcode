class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        while n!=1:
            s.add(n)
            sum=0
            while n:
                z=n%10
                sum+=(z*z)
                n//=10
            n=sum
            if n in s:
                return False
        return True
                
        