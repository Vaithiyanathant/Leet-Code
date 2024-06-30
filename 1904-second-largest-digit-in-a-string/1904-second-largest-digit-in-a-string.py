class Solution:
    def secondHighest(self, s: str) -> int:
        lst =[]
        for i in s:
            if i.isdigit():
                lst.append(int(i))
        lst = sorted(set(lst))[::-1]
        print(lst)
        if len(lst)==1 or lst==[]:
            return -1
        else:
            return lst[1]

        