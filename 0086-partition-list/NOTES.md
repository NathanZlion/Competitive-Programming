# Question
The question is really to partition this linked list into 2 parts. One part is those with calues less than x and the other part is those with value greater than or equal to x. And the relative order of each half should be preserved
​
# Intuition
In a brute force approact we could use two separate arrays that hold each half. And because we use an  append method to put the reference to the nodes into the array their relative position will still be preserved. Finally we can traverse one more time through the 2 arrays to connect the nodes. then return the first node in the first nonempty array.
​
## Modificaiton
Now let's think of a way that does't use additional space and does the job in the original linked list. What I found to be a better approach is to go through the linked list to get to the final node which I called `end`.
​
Then I go through the linked list one more time, whenever I find a node with value greater than or equal to the value x I remove it from that position using an O(1) operation and insert it to the end of the Linked List.