# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val: int):
        if not head:
            return ListNode()
        dummy = ListNode(None, head)
        last_item = dummy
        link_item = last_item.next
        while link_item:
            if link_item.val != val:
                last_item.next = link_item
                last_item = link_item
            else:
                last_item.next = None
            link_item = link_item.next
        return dummy.next
        
t1 = [7, 7, 7], 7
def nodes_gen(array):
    head = ListNode(array[0])
    last_item = head
    for i in array[1:]:
        second_item = ListNode(i)
        last_item.next = second_item
        last_item = second_item
    return head

def decode_link_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

t_head = nodes_gen(t1[0])
obj = Solution()
print(decode_link_list(t_head))
res = obj.removeElements([], 7)
print(decode_link_list(res))