class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cal=self.find(n)
        for i in range(31):
            if self.find(2**i)==cal:
                return True
        return False
    def find(self,n):
        sum=0
        while n:
            k=n%10
            sum+=8**k
            n//=10
        return sum
            
        