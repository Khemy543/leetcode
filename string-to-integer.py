class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        numbers = {'0': 0,'1': 1,'2':2,'3': 3,'4': 4,'5': 5,'6': 6,'7':7, '8':8,'9':9}
        index = 0
        n = len(s)
        sign = 1

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        while index < n and s[index] == " ":
            index += 1

        if index < n and s[index] == "+":
            sign = 1
            index += 1
        elif index < n and s[index] == "-":
            sign = -1
            index += 1
        while index < n and s[index] in numbers:
            digit = numbers[s[index]]
            #check if result is in bound
            if (res > INT_MAX) or (res == INT_MAX and digit > INT_MAX % 10):
                return INT_MIN if sign == -1 else INT_MAX

            res = res * 10 + digit
            index += 1
        
        return res
    
print(Solution().myAtoi("42"))