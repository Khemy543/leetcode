class Solution:
    def isAnagram(self, s: str, t:str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get[t[i], 0]
        return countS == countT


dict1 = {'a' : 2, 'b': 1, 'c': 1}
dict2 = {'b': 1, 'c': 1, 'a': 2}
print (dict1 == dict2)