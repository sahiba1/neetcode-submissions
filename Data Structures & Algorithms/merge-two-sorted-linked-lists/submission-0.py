# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        dummy = curr
        li1 , li2 = list1 , list2
        while li1 and li2:
            if li1.val < li2.val:
                dummy.next = li1
                li1 = li1.next
            else:
                dummy.next = li2
                li2 = li2.next

            dummy = dummy.next
        dummy.next = li1 if li1 else li2

        return curr.next
