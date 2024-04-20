import pytest
from ..main.main import function


@pytest.mark.parametrize('a, b, c, r', [(1, 0, 1, []),
                                        (1, 0, -1, [1, -1]),
                                        (1, 2, 1, [-1])
                                        ])
def test_1(a, b, c, r):
    assert function(a, b, c) == r


@pytest.mark.parametrize('a, b, c, r', [(0, 1, 1, Exception),
                                        ('0', 1, 1, TypeError)
                                        ])
def test_2(a, b, c, r):
    with pytest.raises(r):
        function(a, b, c)


if __name__ == '__main__':
    test_1()
    test_2()
