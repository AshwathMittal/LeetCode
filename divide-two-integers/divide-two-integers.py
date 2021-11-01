class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = dividend/divisor
        if int(a) > 2**31 -1:
            return (2**31) -1
        elif int(a) < -2**31:
            return (-2**31)
        else:
            return int(a)
