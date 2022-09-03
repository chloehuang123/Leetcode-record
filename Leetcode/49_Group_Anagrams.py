class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTb = {}

        for str in strs:
            s = ''.join(sorted(str))
            if s not in hashTb:
                hashTb[s] = [str]
            else:
                hashTb[s].append(str)
                
        return [v for v in hashTb.values()]
