class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        sc = Counter(suits)
        rc = Counter(ranks)
        if len(sc)==1:
            return "Flush"
        print(rc)
        for l, m in rc.items():
            if m >=3:
                return "Three of a Kind"
        for l, m in rc.items():
            if m ==2:
                return "Pair"
        return "High Card"

            
        