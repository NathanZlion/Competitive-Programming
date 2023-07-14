class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyHash = {" ": " "}
        alphabets = list(string.ascii_lowercase)
        index = 0

        for char in key:
            if char in keyHash:
                continue
            
            keyHash[char] = alphabets[index]
            index += 1

            if len(keyHash) == 27:
                break
        
        decoded = [keyHash[char] for char in message]

        return "".join(decoded)
