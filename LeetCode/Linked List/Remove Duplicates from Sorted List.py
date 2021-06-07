class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p1, p2 = head, head.next
        found_dup = False
        while p2:
            if p2.val == p1.val:
                p2 = p2.next
                found_dup = True
                continue
            if found_dup:
                p1.next = p2
                found_dup = False
            p1 = p1.next
            p2 = p2.next
        
        if found_dup:
            p1.next = p2
            
        return head