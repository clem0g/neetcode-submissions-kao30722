class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            strs.append("$0fT1(~--")
            s = "$0fT1(~--)".join(strs)
            return s
        else:
            s = "$0fT1(~--)".join(strs)
            return s

    def decode(self, s: str) -> List[str]:
        if s == "$0fT1(~--":
            empty = []
            return empty
        else:
            output = s.split("$0fT1(~--)")
            return list(output)
