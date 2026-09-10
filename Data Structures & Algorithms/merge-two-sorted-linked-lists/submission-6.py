# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Empty list cases:
        if not list1 and not list2:
            return None
        if list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2
        # Pick the head
        head = None
        if list1 and list2 and list1.val <= list2.val:
            head = list1
            list1 = list1.next
            head.next = None
        else:
            head = list2
            list2 = list2.next
            head.next = None
        # Merge the list
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
                curr.next = None
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
                curr.next = None
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head
