
from .duozhuayu import _chunk, chunk

import pytest

def test_chunk():
    assert chunk([1,2,3,4,5,6], 2) == [[1, 2], [3, 4], [5, 6]]
    assert chunk([1,2,3,4,5], 2) == [[1,2],[3,4],[5]]

