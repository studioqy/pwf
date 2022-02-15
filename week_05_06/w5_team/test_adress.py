from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
  assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
  assert extract_city("1234 Random Ave, New York City, NY 98765") == "New York City"
  assert extract_city("5678 Some Ct, Atlanta, GA 13579") == "Atlanta"
  assert extract_city("9012 A Street St, Boston, Massachusetts 08642") 


def test_extract_state():
  assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
  assert extract_state("") == ""
  assert extract_state("") == ""
  assert extract_state("") == ""

def test_extract_zipcode():
  assert extract_zipcode("") == ""
  assert extract_zipcode("") == ""
  assert extract_zipcode("") == ""
  assert extract_zipcode("") == ""
  assert extract_zipcode("") == ""
  assert extract_zipcode("") == ""





# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])