class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sm=0
        st= set()
        while True:
            while n:
                z=n%10
                sm+=(z*z)
                n=n//10
            if sm==1:
                return True
            elif sm in st:
                return False
            else:
                n=sm
                st.add(sm)
                sm=0
        