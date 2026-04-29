class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = []
        for s in strs:
            encode_str.append(f"{len(s)}#{s}")
        return "".join(encode_str)

    def decode(self, s: str) -> List[str]:
        new_list = list()
        n = 0
        while n < len(s):
            l = n
            while s[n] != "#":
                n += 1
            length = int(s[l:n])
            new_list.append(s[n+1:n+length+1])
            n = n+length+1
        return new_list
