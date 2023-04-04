class Solution:

    def gcd(self, a, b):
        if b == 0:
            return a
        
        return self.gcd(b, a%b)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        freq = defaultdict(int)

        for card in deck:
            freq[card] += 1

        gcdOfValues = freq[deck[0]]
        
        for card in freq:
            gcdOfValues = self.gcd(max(gcdOfValues, freq[card]), min(gcdOfValues, freq[card]))

            if gcdOfValues == 1:
                return False

        return True
