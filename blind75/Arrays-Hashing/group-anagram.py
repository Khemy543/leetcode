from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) #hashmap mapping character count to list of Anagrams
        # defaultdict(list) sets the default value of the keys in the object to an empty array
        for str in strs:
            count = [0] * 26 # a...z

            for s in str:
                count[ord(s) - ord('a')] += 1 # ord gets the number value for the characters

            result[tuple(count)].append(str) # cannot use list as key in python so we convert it to tuple
        
        return result.values()
    

print(Solution.groupAnagrams('a', ["act","pots","tops","cat","stop","hat"]))