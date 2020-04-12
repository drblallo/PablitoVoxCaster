from talents import talent_price

def test_talent_price():
    assert talent_price(1, 0) == 600

def test_talent_price_wrong_tier():
    try:
        talent_price(0, 0), ValueError
    except ValueError:
        assert True
    except: 
        assert False 

def test_talent_price_wrong_apts():
    try:
        talent_price(1, -1), ValueError
    except ValueError:
        assert True
    except: 
        assert False 

