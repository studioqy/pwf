import pytest
from journaling import populate_window, main

# def test_populate_window():
#     finally

def test_populate_window():
    main()
    populate_window(frm_main)
    assert lbl_title == "JOURNAL PROMPT GENERATOR"

test_populate_window()

'''
How do you test tkinter??
'''