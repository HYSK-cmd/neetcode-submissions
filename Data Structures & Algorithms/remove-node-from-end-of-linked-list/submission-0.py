# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        total = 1
        while cur.next:
            cur = cur.next
            total += 1
        target = total - n
        del_node = head
        prev = None
        while target > 0:
            prev = del_node
            del_node = del_node.next
            target -= 1

        if prev is None:
            return head.next
            
        prev.next = del_node.next
        return head
        

