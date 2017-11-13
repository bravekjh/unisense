from unisense.util import is_subset

import pytest


@pytest.mark.parametrize('top_list, sub_list, expected',
                         [([1, 2, 3], [3, 1], True),
                          ([1, 2, 3], [2, 4], False),
                          ([1, 2, 3], [1, 1, 2], True)])
def test_is_subset(top_list, sub_list, expected):
    assert is_subset(top_list, sub_list) == expected

