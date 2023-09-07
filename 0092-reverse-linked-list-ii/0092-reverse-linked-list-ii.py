class Solution:
    @staticmethod
    def __reverse(prev: Optional[ListNode], curr: Optional[ListNode]) -> None:
        nxt = curr.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt

            if not curr:
                break

            nxt = curr.next


    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1, head)
        curr = dummyHead

        for _ in range(left-1):
            curr = curr.next

        preLeft = curr
        curr = curr.next
        leftPtr = curr

        for _ in range(right-left):
            curr = curr.next

        rightPtr = curr
        nxtRight = rightPtr.next
        rightPtr.next = None

        Solution.__reverse(prev=preLeft, curr=leftPtr)
        preLeft.next = rightPtr
        leftPtr.next = nxtRight

        return dummyHead.next
