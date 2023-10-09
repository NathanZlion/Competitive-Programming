from string import digits, hexdigits

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def hasLeadingZeros(val: str):
            if len(val) == 1 and val == '0':
                return False

            for num in val:
                if num == "0":
                    return True
                break

            return False

        def isValidIpv4Val(val: str) -> bool:
            if  len(val) == 0:
                return False

            if hasLeadingZeros(val):
                return False
            
            for num in val:
                if num not in digits:
                    return False

            return 0 <= int(val) <= 255

        def isValidIpv6Val(val: str) -> bool:
            if  0 >= len(val) or len(val) > 4:
                return False

            for num in val:
                if num not in hexdigits:
                    return False

            return True

        def isValidIpv4(ip: str) -> bool:
            ip = ip.split(".")

            if len(ip) != 4:
                return False
            
            for num in ip:
                if not isValidIpv4Val(num):
                    return False
            
            return True

        def isValidIpv6(ip: str) -> bool:
            ip = ip.split(":")

            if len(ip) != 8:
                return False

            for num in ip:
                if not isValidIpv6Val(num):
                    return False

            return True

        if isValidIpv4(queryIP):
            return "IPv4"

        if isValidIpv6(queryIP):
            return "IPv6"

        return "Neither"