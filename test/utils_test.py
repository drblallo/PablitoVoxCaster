from utils import split_at_value
from utils import table_from_list

def test_split_at_value():
    res = [x for x in split_at_value(["one", "two", "three"], 7, len)]
    assert len(res) == 2
    assert res[0] == ["one", "two"]
    assert res[1] == ["three"]

def test_table_from_list():
    table = table_from_list(["row1", "row2"])
    assert table.matching(1)[0].text == "row1"
    assert table.matching(2)[0].text == "row2"
    assert table.matching(3) == []
