class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in s:
            if i == ")":
                sub =""
                while( st and st[-1] != "("):
                    sub+=st.pop()
                st.pop()
                print(sub)
                st.extend(list(sub))
            else:
                st.append(i)
        return "".join(st)
                                   