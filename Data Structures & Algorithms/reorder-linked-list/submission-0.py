# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head
        while second and second.next:
            first = first.next
            second = second.next.next
        
        tail = first.next
        first.next = None 
        cur = tail
        prev = None 
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        l1 = head
        l2 = prev
        while l2:
            t1 = l1.next
            t2 = l2.next
            l1.next = l2
            l2.next = t1
            l1 = t1
            l2 = t2
            


        
