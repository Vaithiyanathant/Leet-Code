class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in range(len(operations)):
            if operations[i]=="+":
                score.append(score[-1]+score[-2])
            elif operations[i]=="D":
                score.append(score[-1]*2)
            elif operations[i]=="C":
                score.pop()
            else:
                score.append(int(operations[i]))
        print(score)
        return sum(score)
                

        