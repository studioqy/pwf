from words import prefix, suffix
import pytest

def test_prefix():
    assert prefix("","") == ""
    assert prefix("","correct") == ""
    assert prefix("clear," "") == ""

# def test_suffix():
#     return None


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_words.py"])