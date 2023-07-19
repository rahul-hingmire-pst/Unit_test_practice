import pytest
from Checkout import Checkout

@pytest.fixture
def checkout():
    checkout = Checkout()
    checkout.additemprice("a",4)
    checkout.additemprice("b",1)
    return checkout

# def test_canaddItemPrice(checkout):
#     checkout.additemprice("a",2)

# def test_canaddItemCheckout(checkout):
#     checkout.additem("a")

def test_cancalculatetotal(checkout):
    checkout.additem("a")
    assert checkout.calculatetotal() == 4

def test_cancalculatetotalwithmultiple(checkout):
    checkout.additem("a")
    checkout.additem("b")
    assert checkout.calculatetotal() == 5

def test_canadddiscount(checkout):
    checkout.adddiscount("a",3,2)

def test_canaddiscountrule(checkout):
    checkout.adddiscount("a",3,2)
    checkout.additem("a")
    checkout.additem("a")
    checkout.additem("a")
    checkout.additem("a")
    print(checkout.calculatetotal())
    assert checkout.calculatetotal() == 6

    


