class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        """
        Given X, binary format
        
        7, 10
        
        00000111
        00001010
        
        3 flips
        """

        return (start ^ goal).bit_count()
