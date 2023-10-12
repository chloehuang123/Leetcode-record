class Solution:
    def romanToInt(self, s: str) -> int:

        res = 0

        digital_value = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }

        for i in range(len(s) - 1):
            if digital_value[s[i]] >= digital_value[s[i+1]]:
                res += digital_value[s[i]]
            else:
                res -= digital_value[s[i]]
        
        res += digital_value[s[-1]]

        return res
