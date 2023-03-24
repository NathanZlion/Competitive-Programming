class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.validIpAddresses = []
        self.runningIpAddress = []
        n = len(s)

        def backTrack(left):
            if len(self.runningIpAddress) == 4:
                if left == n:
                    self.validIpAddresses.append(".".join(self.runningIpAddress))
                return

            if left >= n or s[left] == '0':
                self.runningIpAddress.append('0')
                backTrack(left+1)
                self.runningIpAddress.pop()
                return

            for right in range(left+1, n+1):
                if int(s[left:right]) > 255:
                    return

                self.runningIpAddress.append(s[left:right])
                backTrack(right)
                self.runningIpAddress.pop()

        backTrack(0)
        return self.validIpAddresses
