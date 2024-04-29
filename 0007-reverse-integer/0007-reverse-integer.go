func reverse(x int) int {
    var isNegative bool = x < 0;

    if isNegative {
        x = x * -1;
    }

    var reversedNumber int = 0;

    for x > 0 {
        lastDigit := x % 10;
        x = x / 10;

        if reversedNumber > math.MaxInt32 / 10 || (reversedNumber == math.MaxInt32 / 10 && lastDigit > 7) {
            return 0
        }

        reversedNumber = reversedNumber * 10 + lastDigit;
    }

    if isNegative {
        reversedNumber = reversedNumber * -1;
    }

    return reversedNumber;
}
