from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_full_name():
  assert make_full_name("Sally", "Brown") == "Brown; Sally"
  assert make_full_name("sally", "brown") == "brown; sally"
  assert make_full_name("Sally", "Brown-Smith") == "Brown-Smith; Sally"
  assert make_full_name("Elizabeth", "Morganson") == "Morganson; Elizabeth"
  assert make_full_name("Sally-Anne", "Brown") == "Brown; Sally-Anne"
  

def test_extract_family():
  assert extract_family_name("Brown; Sally") == "Brown"
  assert extract_family_name("Smith; Bob") == "Smith"
  assert extract_family_name("Johnsonson; John") == "Johnsonson"
  assert extract_family_name("E; Robert") == "E"
  assert extract_family_name("McDonald; Ron") == "McDonald"
  assert extract_family_name("Smith-Johnson; Joe") == "Smith-Johnson"
  assert extract_family_name("Verylonglastname; Guy") == "Verylonglastname"


def test_extract_given_name():
  assert extract_given_name("Brown; Sally") == "Sally"
  assert extract_given_name("brown; sally") == "sally"
  assert extract_given_name("Brown-Smith; Sally") == "Sally"
  assert extract_given_name("Brown; Emmanuelle") == "Emmanuelle"
  assert extract_given_name("; Sally") == "Sally"
  assert extract_given_name("Brown;") == ""
  assert extract_given_name("Brown; ") == ""
  assert extract_given_name("Brown;Sally") == "Sally"
  assert extract_given_name("Brown; Sally ") == "Sally"
  assert extract_given_name("Brown; Sally-Anne") == "Sally-Anne"



pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])