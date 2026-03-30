class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = ["()", "[]", "{}"]
        while True:
            original_length = len(s)
            
            for pair in valid_pairs:
                s = s.replace(pair, "")
            
            new_length = len(s)
            if new_length == original_length:
                break
                
        return len(s) == 0



        