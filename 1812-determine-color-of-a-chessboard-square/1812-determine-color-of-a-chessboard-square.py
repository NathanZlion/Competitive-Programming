class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        return ((ord(coordinates[0])-96 + int(coordinates[1]))%2) != 0