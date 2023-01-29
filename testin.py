# FROM :
# https://realpython.com/pytest-python-testing/

# def test_uppercase():
#     assert "loud noises".upper() == "LOUD NOISES"

# def test_reversed():
#     assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

# def test_some_primes():
#     assert 37 in {
#         num
#         for num in range(2, 50)
#         if all(num % div != 0 for div in range(2, num))
#     }

# Fixtures: Managing State and Dependencies
import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1
    
def format_data_for_display(people):
    ...# Implement this!

def format_data_for_excel(people):
    ...# Implement this!
    
@pytest.fixture
def example_people():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people):
    assert format_data_for_display(example_people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",]
    
def test_format_data_for_excel(example_people):
    assert format_data_for_excel(example_people) == """given,family,title
    Alfonsa,Ruiz,Senior Software Engineer
    Sayid,Khan,Project Manager
    """

test_format_data_for_display(example_people)
test_format_data_for_excel(example_people)

# doesn't work    # 

@pytest.mark.parametrize("palindrome", [
"",
"a",
"Bob",
"Never odd or even",
"Do geese see God?",])

def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)

@pytest.mark.parametrize("non_palindrome", [
    "abc",
    "abab",
])

def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)