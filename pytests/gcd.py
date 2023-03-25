from hypothesis import given, strategies as st

def gcd(n, m):
    """Compute the GCD of two integers by Euclid's algorithm."""

    n, m = abs(n), abs(m)
    n, m = min(n, m), max(n, m)  # Sort their absolute values.
    if not n:
        return m
    while m % n:         # While `n` doesn't divide into `m`:
        n, m = m % n, n  # update the values of `n` and `m`.
    return n

# @given(st.integers(), st.integers())
@given(st.integers(min_value=1, max_value=100),
    st.integers(min_value=-500, max_value=500),)
def test_gcd(n, m):
    d = gcd(n, m)

    assert d > 0  # 1) `d` is positive
    assert n % d == 0  # 2) `d` divides `n`
    assert m % d == 0  # 3) `d` divides `m`

    # 4) no other number larger than `d` divides both `n` and `m`
    for i in range(d + 1, min(n, m)):
        assert (n % i) or (m % i)
        
        
