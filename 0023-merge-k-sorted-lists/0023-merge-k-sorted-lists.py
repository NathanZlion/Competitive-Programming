# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        valueToNodeDict = defaultdict(list)
        values = []

        for node in lists:
            while node:
                values.append(node.val)
                valueToNodeDict[node.val].append(ListNode(node.val))
                node = node.next

        heapify(values)
        dummy = ListNode()
        curr = dummy

        for _ in range(len(values)):
            curr.next = valueToNodeDict[heappop(values)].pop()
            curr = curr.next


        return dummy.next
