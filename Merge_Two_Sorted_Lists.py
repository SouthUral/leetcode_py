
from cgi import test
from struct import unpack


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:

    def mergeTwoLists(self, list1, list2):
        nodes_s = self.unpack_nodes(list1)
        nodes_s.extend(self.unpack_nodes(list2))
        nodes_s.sort()
        head_node = None
        tail_node = None
        for item in nodes_s:
            node = ListNode(item)
            if head_node is None:
                head_node = node
            elif tail_node is None:
                head_node.next = node
                tail_node = node
            else:
                tail_node.next = node
                tail_node = node
        return head_node

    def unpack_nodes(self, node_head):
        nodes = []
        while node_head != None:
            nodes.append(node_head.val)
            node_head = node_head.next
        return [] if nodes == [0] else nodes




def view_nodes_list(head_node_list):
    node = head_node_list
    nodes = []
    while node != None:
        nodes.append(node.val)
        node = node.next
    return nodes


def test_1():
    obj = Solution()
    node1 = ListNode(10)
    node2 = ListNode(17)
    node3 = ListNode(16, node2)
    obj.node_head = node1
    assert obj.node_head == node1
    assert obj.node_tail == None
    obj.node_head = node3
    assert obj.node_head == node3
    assert obj.node_tail == node2
    print('test_1 comlited')


def test_2():
    obj = Solution()
    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(4)))
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = [1, 1, 2, 3, 4, 4]
    assert res == try_res, f'test_2 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_2 comlited')

def test_3():
    obj = Solution()
    node1 = ListNode(1, ListNode(2, ListNode(4)))
    node2 = ListNode(1, ListNode(3, ListNode(4, ListNode(7))))
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = [1, 1, 2, 3, 4, 4, 7]
    assert res == try_res, f'test_3 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_3 comlited')

def test_4():
    obj = Solution()
    node1 = ListNode(1)
    node2 = ListNode(3)
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = [1, 3]
    assert res == try_res, f'test_4 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_4 comlited')

def test_5():
    obj = Solution()
    node1 = ListNode(1, ListNode(5))
    node2 = ListNode(3)
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = [1, 3, 5]
    assert res == try_res, f'test_5 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_5 comlited')

def test_6():
    obj = Solution()
    node1 = ListNode()
    node2 = ListNode()
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = []
    assert res == try_res, f'test_6 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_6 comlited')

def test_7():
    obj = Solution()
    node1 = ListNode(1)
    node2 = ListNode()
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = [1]
    assert res == try_res, f'test_7 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_7 comlited')

def test_8():
    obj = Solution()
    node1 = ListNode(14)
    node2 = ListNode(1, ListNode(3, ListNode(4, ListNode(7))))
    res = view_nodes_list(obj.mergeTwoLists(node1, node2))
    try_res = [1, 3, 4, 7, 14]
    assert res == try_res, f'test_8 failed, list returned: "{res}", try list: "{try_res}"'
    print('test_8 comlited')


# test_1()
test_2()
test_3()
test_4()
test_5()
test_6()
test_7()
test_8()


# l1_h = ListNode(1, ListNode(2, ListNode(4)))
# l2_h = ListNode(1, ListNode(3, ListNode(4)))
# obj = Solution()





