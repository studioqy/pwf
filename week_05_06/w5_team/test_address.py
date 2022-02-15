from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
  assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
  assert extract_city("1234 Random Ave, New York City, NY 98765") == "New York City"
  assert extract_city("5678 Something Ct, Atlanta, GA 13579333") == "Atlanta"
  assert extract_city("92 One Street St, Boston, Massachusetts 08642-1234") == "Boston"
  assert extract_city("436 Waterfall Valley Way, Santa Fe, New Mexico 65487abcd") == "Santa Fe"



def test_extract_state():
  
  assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
  assert extract_state("664 W Center St, Austin, TX 78642") == "TX"
  assert extract_state("712 N Center St, Provo, UT 68974") == "UT"
  assert extract_state("823 E Center St, Miami, FL 79237") == "FL"
  assert extract_state("931 55th St, Nashville, TN 09193") == "TN"
  assert extract_state("0adw8hawd90, 9a0wdjw90da, AL 9jd0a8whd") == "AL"
  assert extract_state("525 S Center St, Rexburg, Idaho 83460") == "Idaho"
  assert extract_state("1st St, dallas, texas 78642") == "texas"

def test_extract_zipcode():
  
  assert extract_zipcode("525 S Center St,Rexburg,ID 83460") == "83460" 
  assert extract_zipcode("525 S Center St,Rexburg,ID 83460") == "83460"
  assert extract_zipcode("5678 Something Ct,Atlanta,GA 1357952") == "1357952"
  assert extract_zipcode("525 S Center St,Rexburg,ID 83460-0304") == "83460-0304"
  assert extract_zipcode("823 E Center St,Miami,FL 79237") == "79237"
  assert extract_zipcode("664 W Center St,Austin,TX 78642") == "78642"

pytest.main(["-v", "--tb=line", "-rN", "test_address.py"])