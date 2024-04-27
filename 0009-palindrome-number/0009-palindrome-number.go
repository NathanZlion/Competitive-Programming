import (
    "fmt" 
    "strconv"
)

func isPalindrome(x int) bool {
    if x < 0 {
        return false;
    }

    strX := strconv.Itoa(x);
    for i := 0; i <= len(strX) / 2; i ++ {
        if strX[i] != strX[len(strX) - i - 1] {
            return false;
        }
    }
    return true;
}
