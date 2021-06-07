class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(l1, l2):
        p=ListNode(0)
        head=p
        while l1 and l2:
            if l1.val<=l2.val:
                p.next=l1
                l1=l1.next
            else:
                p.next=l2
                l2=l2.next
            p=p.next

        while l1:
            p.next=l1
            l1=l1.next
            p=p.next

        while l2:
            p.next=l2
            l2=l2.next
            p=p.next

        return head.next