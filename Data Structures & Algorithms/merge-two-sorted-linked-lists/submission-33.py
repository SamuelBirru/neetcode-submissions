# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = list1
        while curr:
            values.append(curr.val)
            curr = curr.next

        curr2 = list2
        while curr2:
            values.append(curr2.val)
            curr2 = curr2.next

        values.sort()
        Linked = ListNode()
        dummy = Linked
        for num in values:
            dummy.next = ListNode(num)
            dummy = dummy.next

        return Linked.next
