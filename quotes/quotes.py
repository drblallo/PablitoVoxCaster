from datetime import date
from random import choice

def get_quotes(path):
    with open(path, "r") as f:
        return f.readlines()

today = date.today().day
today_quote = choice(get_quotes("./quotes/quotes.txt"))

def get_thought():
    global today
    global today_quote
    if today != date.today().day:
        today = date.today().day
        today_quote = choice(get_quotes("./quotes/quotes.txt"))
    return today_quote
