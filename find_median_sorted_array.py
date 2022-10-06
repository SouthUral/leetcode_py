def findMedianSortedArrays(nums1, nums2):
        res = nums1 + nums2
        res.sort()
        if len(res) % 2 != 0:
            return res[len(res) // 2]
        median_ar = len(res) // 2 - 1
        return sum(res[median_ar: median_ar + 2])/2

t1 = ([1, 2], [3, 4]), 2.5
t2 = ([3, 1], [2]), 2
t3 = ([1, 2, 3, 4], [3, 5]), 3


def test_func(*args):
    for item in args:
        res_item = findMedianSortedArrays(*item[0])
        tr_answer = item[1]
        assert res_item == tr_answer, f'test faild: {res_item}, true answer: {tr_answer}'
    print('all tests were successful')


test_func(t1, t2, t3)