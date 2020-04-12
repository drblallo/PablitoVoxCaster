from rules import canonical_type_name, canonical_location_name

def test_canonical_crit_name():
    assert canonical_type_name("explsive") is not None
    assert canonical_type_name("e") is not None

def test_canonical_location_name():
    assert canonical_location_name("hed") is not None
    assert canonical_location_name("h") is not None
