import pytest

def isleapyear(year):
    if(year%4 == 0) and (year%100 != 0):
        return "leap year"
    elif(year%400 == 0)and (year%100 == 0):
        return "leap year"
    else:
        return "not leap year"
    
def leapyear(year,expectedVal):
    print(year)
    retval = isleapyear(year)
    assert retval == expectedVal

# @pytest.mark.parametrize("year, expectedVal", [
#     (2004, "leap year"),
#     (2000, "leap year"),
#     (1900, "not leap year"),
#     (2024, "leap year"),
#     (2021, "not leap year"),
# ])


def test_cases():
    leapyear(2004, "leap year")

def test_first():
    leapyear(1995,"not leap year")

def test_second():
    leapyear(2007,"not leap year")

def test_third():
    leapyear(2014,"not leap year")

    

