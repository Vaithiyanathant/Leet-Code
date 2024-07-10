class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stilama =  0
        for i in logs:
            if i[0] == "." and i[1] == ".":
                if stilama:
                    stilama-=1
                    
            elif i[0] != ".":
                stilama+=1
        return stilama
        