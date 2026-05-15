class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        arr, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(str(s[i:j]))
            i = j + 1
            j = length + i
            arr.append(s[i:j])
            i = j
        return arr


