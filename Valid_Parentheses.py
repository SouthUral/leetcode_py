class ItemSteck:
    def __init__(self, value, last_elem=None):
        self.value = value
        self.last_elem = last_elem

    def __str__(self):
        return str(self.value)


class Steck:
    def __init__(self, steck_item=None):
        self.steck_item = steck_item
        self.len_steck = 0

    def add(self, new_value):
        if self.steck_item is None:
            self.steck_item = ItemSteck(new_value)
        else:
            old_item = self.steck_item
            self.steck_item = ItemSteck(new_value, old_item)
        self.len_steck += 1

    def get_item(self):
        if self.steck_item:
            return self.steck_item.value
        return None

    def pop_item(self):
        if self.steck_item:
            item = self.steck_item
            self.steck_item = item.last_elem
            self.len_steck -= 1
            return item.value

    def get_list_steck(self):
        steck = []
        last_item = self.steck_item
        while last_item:
            steck.append(last_item.value)
            last_item = last_item.last_elem
        return steck

    def __len__(self):
        return self.len_steck
        

class ParentheseSteck(Steck):
    parentheses = {')': '(', '}': '{', ']': '['}

    def add(self, new_value):
        if self.get_item() == self.parentheses.get(new_value, '0'):
            self.pop_item()
        else:
            super(ParentheseSteck, self).add(new_value)


class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] in (')', ']', '}'):
            return False
        
        steck_obj = ParentheseSteck()
        for i in s:
            steck_obj.add(i)
        return len(steck_obj) == 0


def test_solution():
    obj = Solution()
    test_cases = [("()[]", True), ("(]", False), ('([[[]]])', True), ('()([[]])[(])', False)]
    for counter, item in enumerate(test_cases):
        case = item[0]
        true_answ = item[1]
        res = obj.isValid(case)
        assert res == true_answ, f'{counter} the test failed, received response: {res}, True_received: {true_answ}'


def test_steck():
    obj = Steck()
    assert len(obj) == 0, '1'
    assert obj.get_list_steck() == [], f'2, returned: {obj.get_list_steck()}' 
    assert obj.pop_item() == None, '1.1'
    for i in range(10):
        obj.add(i)
    assert len(obj) == 10, '3'
    assert obj.get_item() == 9, f'4, returned: {obj.get_item()}'
    assert obj.pop_item() == 9, '5'
    assert obj.get_item() == 8, '6'
    assert obj.get_list_steck() == [8, 7, 6, 5, 4, 3, 2, 1, 0], f'7 returned: {obj.get_list_steck()}'


test_steck()
test_solution()
