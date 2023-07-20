from secondday.app.student import student
from datetime import datetime
import pytest

@pytest.fixture(scope = "function")
def dummy_student():
    return student("nikhil",datetime(2001,7,1),5)

def test_age(dummy_student):
    cur_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == cur_age

def test_credits(dummy_student):
    assert dummy_student.get_credits() == 5