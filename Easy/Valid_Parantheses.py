class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ("(", "[", "{"):
                stack.append(i)
            else:
                if not stack:
                    return False
                pop = stack.pop()
                if (i == ")" and pop != "(") or (i == "]" and pop != "[") or (i == "}" and pop != "{"):
                    return False
        return not stack
        