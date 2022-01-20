class Solution:
    def divide_unhandled(self, dividend: int, divisor: int) -> int:
        res = 0
        neg = 0
        if dividend<0:
            neg += 1
            divisor = -divisor
        if divisor < 0:
            neg+=1
            divisor = -divisor   

        
        while dividend-divisor >= 0:
            res+=1
            dividend-=divisor
        if neg == 1:
            res = -res
        return res
    
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        neg = 2
        if dividend > 0:
            neg-=1
            dividend = -dividend
        
        if divisor > 0:
            neg -= 1
            divisor = -divisor
        quot = 0
        while dividend-divisor <=0 :
            quot-=1
            dividend = dividend-divisor
            
        return -quot if neg != 1 else quot
    
    def divide_bitwise(self, dividend, divisor):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        res = 0
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        return res
s = Solution()
dividend = 7
divisor = -3
print(s.divide(dividend, divisor))