class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack=[]
        cnt = 0 
        for i in range(len(s)):
            if stack and stack[-1]=="b" and s[i]=="a":
                cnt+=1
                stack.pop()
            else:
                stack.append(s[i])
        return cnt
        