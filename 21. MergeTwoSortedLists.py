# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            result = ListNode(list2.val)
            list2 = list2.next
        else:
            result = ListNode(list1.val)
            list1 = list1.next
        
        pointer = result
        while list1 and list2:
            if list1.val >= list2.val:
                pointer.next = list2
                list2 = list2.next
            else:
                pointer.next = list1
                list1 = list1.next
            
            pointer = pointer.next
        
        if list1:
            pointer.next = list1
        elif list2:
            pointer.next = list2
        
        return result
            

            
