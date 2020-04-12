from talents import TalentsDb, talent_price
from rules import load_criticals, canonical_crit_names
from utils import table_from_file
from serializers import talent_to_embed, text_to_embed
from serializers import critical_to_embed, table_row_to_embed
from serializers import long_text_embed
from quotes import get_thought

class Rulebook:
    def __init__(self):
        self.talentsDb = TalentsDb("./talents/talents.json")
        self.criticalDb = load_criticals("./rules/criticals.json")
        self.insanity_table = table_from_file("./tables/insanity.json")

    def matching_insanity_rows(self, value=None):
        if value is None:
            return self.insanity_table.rows()
        return self.insanity_table.matching(value)

    def talents(self, name=None):
        return talent_to_embed(self.talentsDb, name)

    def get_thought(self):
        return text_to_embed(get_thought())

    def critical(self, type, location, level:int=None):
        try:
            (t, l) = canonical_crit_names(type, location)
        except ValueError as error:
            return text_to_embed(str(error)) 

        return critical_to_embed(self.criticalDb, t, l, level)

    def insanity(self, value:int = None):
        rows = self.matching_insanity_rows(value) 
        return table_row_to_embed(rows, "insanity result")

    def experience(self, tier :int, apts :int):
        try:
            price = talent_price(tier, apts)
            text = "Cost for tier {} talent  with {} matching aptitudes:".format(tier, apts)
                
            embed = long_text_embed(str(price), text, "_", True)
            return embed
        except ValueError as err:
            return text_to_embed(str(err))
