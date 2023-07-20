from secondday.app.sample import add
import sys
import pytest

# unconditional skip done here for test cases
@pytest.mark.skip
def test_add():
    retVal = add(2,3)
    assert retVal == 5

#conditional skip don as per the version for test case
@pytest.mark.skipif(sys.version_info > (3,7), reason = "Python version is greater than 3.7")
def test_add_again():
    retVal = add(2,3)
    assert retVal == 5

#if The platform on which this case run is windows 32 then it will raise exception(or we can ignore it)
@pytest.mark.xfail(sys.platform == "win32")
def test_addThird():
    retVal = add("a"+"b")
    assert retVal == "ab"
    raise Exception()