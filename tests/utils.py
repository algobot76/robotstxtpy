from collections import Counter


def assert_same_elements_in_lists(l1, l2):
    assert Counter(l1) == Counter(l2)
