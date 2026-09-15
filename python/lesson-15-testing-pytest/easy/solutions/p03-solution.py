"""SOLUTION: Fixture sample_list (Easy)"""
import pytest

@pytest.fixture
def sample_list():
    return [3, 1, 4, 1, 5]

def test_max(sample_list):
    assert max(sample_list) == 5

def test_len(sample_list):
    assert len(sample_list) == 5

if __name__ == "__main__":
    sl = [3, 1, 4, 1, 5]
    assert max(sl) == 5
    assert len(sl) == 5
    print("All tests passed!")
