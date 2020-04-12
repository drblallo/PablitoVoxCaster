import json

class TableRow:
    def __init__(self, text, minV, maxV=None):
        self.text = text
        self.min = minV 
        self.max = minV if maxV is None else maxV

    def in_range(self, val):
        return self.min <= val <= self.max

def row_from_dict(d):
    t = d["text"]
    mn = d["min"]
    mx = mn + 1 if "max" not in d.keys() else d["max"]
    return TableRow(t, mn, mx)

class Table:
    def __init__(self, rows):
        self.mrows = rows

    def rows(self):
        return self.mrows

    def matching(self, val=None):
        if val is None:
            return self.mrows
        return [x for x in self.mrows if x.in_range(val)]

def table_from_file(path):
    with open(path) as f:
        js = json.load(f)
        rows = [row_from_dict(d) for d in js]
        return Table(rows)

def table_from_list(list, start=1):
    return Table([TableRow(text, i) for i, text in enumerate(list, start)])
