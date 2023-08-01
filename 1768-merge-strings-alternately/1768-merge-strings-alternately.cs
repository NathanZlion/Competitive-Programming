public class Solution {
    public string MergeAlternately(string word1, string word2) {
        // start from the first Word
        bool FirstTurn = true;
        
        int ptr1 = 0;
        int ptr2 = 0;
        char[] chars = new char[word1.Length + word2.Length];

        while (ptr1 < word1.Length && ptr2 < word2.Length){
            if (FirstTurn){
                chars[ptr1 + ptr2] = word1[ptr1];
                ptr1++;
            }
            else
            {
                chars[ptr1 + ptr2] = word2[ptr2];
                ptr2++;
            }
            FirstTurn = !FirstTurn;
        }

        while (ptr1 < word1.Length){
            chars[ptr1 + ptr2] = word1[ptr1];
            ptr1++;
        }

        while (ptr2 < word2.Length){
            chars[ptr1 + ptr2] = word2[ptr2];
            ptr2++;
        }

        return new string(chars);
    }
}