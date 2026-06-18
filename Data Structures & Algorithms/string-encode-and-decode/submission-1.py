class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "zero"
        else:
            encoded_string = '<code>'.join(strs)[::-1]
            return encoded_string

    def decode(self, s: str) -> List[str]:
        if s == "zero":
            return []
        else:
            reversed_string = s[::-1]
            decoded_string = reversed_string.split("<code>")
            return decoded_string
