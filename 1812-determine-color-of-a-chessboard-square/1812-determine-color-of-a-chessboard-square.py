class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        r = coordinates[0]
        c = int(coordinates[1])
        r = ord(r)-96
        
        return ((r+c)%2)!=0