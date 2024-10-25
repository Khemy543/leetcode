class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = { ')': '(', '}': '{', ']': '[' }
        stack = []

        for a in s:
            if a not in hashMap:
                stack.append(a)
                continue
            if not stack or stack.pop() != hashMap[a]:
                return False
        return not stack