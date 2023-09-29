import java.util.List;
import java.util.ArrayList;

class TrieNode {
    TrieNode[] children;

    TrieNode() {
        children = new TrieNode[2];
    }
}

class Trie {
    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    void insert(int num) {
        TrieNode curr = root;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[bit] == null) {
                curr.children[bit] = new TrieNode();
            }
            curr = curr.children[bit];
        }
    }

    int findMaxXor(int num) {
        TrieNode curr = root;
        int xor = 0;
        for (int i = 30; i >= 0; i--) {
            int bit = (num >> i) & 1;
            if (curr.children[1 - bit] != null) {
                xor |= (1 << i);
                curr = curr.children[1 - bit];
            } else {
                curr = curr.children[bit];
            }
        }
        return xor;
    }
}

class Solution {
    public int findMaximumXOR(int[] nums) {
        Trie trie = new Trie();
        trie.insert(nums[0]);
        int maxXor = 0;
        for (int i = 1; i < nums.length; i++) {
            int num = nums[i];
            maxXor = Math.max(maxXor, trie.findMaxXor(num));
            trie.insert(num);
        }
        return maxXor;
    }
}