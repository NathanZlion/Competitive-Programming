import (
    "fmt"
    "math"
)

func mySqrt(x int) int {
    var left = -1;
    var right = 50000;
    
    for right > left + 1 {
        mid := left + ((right - left) / 2);

        if square := int(math.Pow(float64(mid), 2)); square <= x {
            left = mid;
        } else {
            right = mid;
        }
    }

    return left;
}
