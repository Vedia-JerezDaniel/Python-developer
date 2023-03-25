from hypothesis import given, strategies as st

def my_sort(int_list):
    if not int_list:
        return []
    s = sorted(set(int_list))
    return s + [s[-1]] * (len(int_list) - len(s))

@given(st.integers())
def test_int_str_roundtripping(x):
    assert x == int(str(x))
    
@given(st.lists(st.integers()))
def test_my_sort(int_list):
    result = my_sort(int_list)
    assert len(result) == len(int_list)  # Should have same length.
    assert set(result) == set(int_list)  # Same numbers as input.
    for a, b in zip(result, result[1:]):  # Result is actually sorted.
        assert a <= b
        
def test_my_sort_specific_examples():
    assert my_sort([]) == []
    assert my_sort(list(range(10)[::-1])) == list(range(10))
    assert my_sort([42, 73, 0, 16, 10]) == [0, 10, 16, 42, 73]