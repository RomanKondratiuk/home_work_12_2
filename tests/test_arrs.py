import pytest

from utils import arrs


def test_get():
    with pytest.raises(IndexError):
        assert arrs.get([1, 2, 3], 1, "test") == 2
        assert arrs.get([1, 2, 3], 0, "test") == 1
        assert arrs.get([], 0, "test") == "test"
        assert arrs.get([1, 2, 3], -1, "test") == []
        assert arrs.get([1, 4, 3], '1', "test") == 4
        assert arrs.get(['testing', 'test', 3], 1, "test") == 'test'
        assert arrs.get('test', 5, 'testing') == 'Данные должны быть в формате списка'
        assert arrs.get([1, '2', 3], '1', "test") == 'индкес должен быть целым числом'


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
