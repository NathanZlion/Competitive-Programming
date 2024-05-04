import (
    "fmt"
    "strings"
    "strconv"
)

type IndexOutOfBoundError struct{}

func (m *IndexOutOfBoundError) Error() string {
	return "Error, String index is out of bound"
}


func getAtIndex(slice []string, index int) (int, error) {
    if index < len(slice) {
        res, err := strconv.ParseInt(slice[index], 10, 64)
        return int(res), err;
    }
    return 0, &IndexOutOfBoundError{};
}

func compareVersion(version1 string, version2 string) int {
    var version1Slice []string = strings.Split(version1, ".");
    var version2Slice []string = strings.Split(version2, ".");
    ptr1 := 0;
    ptr2 := 0;
    
    for ptr1 < len(version1Slice) || ptr2 < len(version2Slice) {
        version1NumberAtIndex, err1 := getAtIndex(version1Slice, ptr1);
        version2NumberAtIndex, err2 := getAtIndex(version2Slice, ptr2);
        
        if version1NumberAtIndex > version2NumberAtIndex {
            return 1;
        }

        if version1NumberAtIndex < version2NumberAtIndex {
            return -1;
        }

        ptr1 ++;
        ptr2 ++;
    }

    return 0;
}
