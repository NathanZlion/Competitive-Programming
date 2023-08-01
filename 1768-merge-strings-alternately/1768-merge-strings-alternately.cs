public class Solution {
    public string MergeAlternately(string word1, string word2) {        
        int ptr1 = 0;
        int ptr2 = 0;

        char[] merged = new char[word1.Length + word2.Length];
        int ptr = 0;

        while (ptr1 < word1.Length && ptr2 < word2.Length){
            merged[ptr] = word1[ptr1];
            ptr1++;
            ptr++;

            merged[ptr] = word2[ptr2];
            ptr2++;
            ptr++;
        }

        while (ptr1 < word1.Length){
            merged[ptr] = word1[ptr1];
            ptr1++;
            ptr++;
        }

        while (ptr2 < word2.Length){
            merged[ptr] = word2[ptr2];
            ptr2++;
            ptr++;
        }

        return new string(merged);
    }
}