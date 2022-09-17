class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        hashTb = set()

        for r in range(len(s)):
            while s[r] in hashTb:
                hashTb.remove(s[l])
                l += 1
            hashTb.add(s[r])
            res = max(res, (r - l + 1))
        return res

      
      
      
###############################################################################################
# 思路：凡是l, r中间有重复的就挪l，直到没有再挪r


# 注意：长度是 r - l + 1, 别忘加一
###############################################################################################
