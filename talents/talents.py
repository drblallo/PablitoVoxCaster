import json

class Talent:
    def __init__(self, jsonDict):
        self.name = jsonDict["name"]
        self.aptitude1 = jsonDict["aptitude1"]
        self.aptitude2 = jsonDict["aptitude2"]
        self.effect = jsonDict["effect"]
        self.tier = jsonDict["tier"]
        self.prerequisite = jsonDict["prerequisite"]
        self.has_specializations = False
        if "specialisations" in jsonDict:
            self.has_specializations = True
            self.specializations = jsonDict["specialisations"]


    def prettyString(self):
        return self.name + "\n" + self.effect

class TalentsDb:
    def __init__(self, path):
        self.talents = load_talents(path)

    def names(self):
        return self.talents.keys()

    def items(self):
        return self.talents.items()

    def matching_name(self, name):
        for key, talent in self.items():
            if name.upper() in key.upper():
                yield talent
            

def load_talents(path):
    with open(path) as f:
        talents = json.load(f) 
        return {x["name"]: Talent(x) for x in talents}

def talent_price(tier,apts):
    if tier in range(1,4) and apts in range(0,3): 
        return int(600*(1+(0.5*(tier-1)))/(apts+1))
    return "Wrong parameters"
