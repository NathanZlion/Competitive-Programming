class Solution:
    def intToRoman(self, num: int) -> str:
        
        normal_cases = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        special_cases = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        normal_numbers = [1, 5, 10, 50, 100, 500, 1000]

        roman: List[str] = []

        def get_significant_num(num):
            shift = 0

            while num > 10**(shift+1):
                shift += 1
            
            return num//(10**shift)*(10**shift)

        def fitting_num(num: int) -> int:
            left = -1
            right = len(normal_numbers)
            
            while right > left + 1:
                mid = (left + right)//2
                if normal_numbers[mid] > num:
                    right = mid
                else:
                    left = mid

            return normal_numbers[left]

        while num > 0:
            # get most significant number value
            most_significant = get_significant_num(num)
            
            if most_significant in special_cases:
                roman.append(special_cases[most_significant])
                num -= most_significant

            else:
                fitting_number = fitting_num(most_significant)
                roman.append(normal_cases[fitting_number])
                num -= fitting_number

        return ''.join(roman)
