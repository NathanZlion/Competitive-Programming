class Codec:
    def __init__(self):
        self.curr_available_id = 0
        self.decodingMap = {}
        self.encodingMap = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        if longUrl not in self.encodingMap:
            self.encodingMap[longUrl] = self.curr_available_id
            self.decodingMap[self.curr_available_id] = longUrl
            self.curr_available_id += 1

        return self.encodingMap[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.decodingMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))