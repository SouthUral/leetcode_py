'''You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        export_number = lambda x: int(''.join([str(i) for i in x]))
        nodes_int = map(lambda x: export_number(self.unpacking_linked_list(x)), [l1, l2])
        unpack_res = [int(i) for i in str(sum(nodes_int))][::-1]
        return self.init_list_node(unpack_res)

    @staticmethod
    def init_list_node(l_node):
        nodes = []
        for idx ,item in enumerate(l_node, start=-1):
            if idx == -1:
                nodes.append(ListNode(item))
            else:
                new_obj = ListNode(item)
                nodes[idx].next = new_obj
                nodes.append(new_obj)
        return nodes[0]

    @staticmethod
    def unpacking_linked_list(node):
        res = []
        link_node = node
        while link_node.next is not None:
            res.append(link_node.val)
            link_node = link_node.next
        res.append(link_node.val)
        res.reverse()
        return res


node_list_1 = Solution.init_list_node([2, 4, 5])
node_list_2 = Solution.init_list_node([4, 0, 8])
obj_test = Solution()

assert Solution.unpacking_linked_list(node_list_1) == [5, 4, 2], 'распаковка неверна'
assert type(obj_test.addTwoNumbers(node_list_1, node_list_2)) == ListNode 
