import re

def clean_data(text):
    text = str(text).lower
    text = re.sub(r"https\S+","",text)
    text = re.sub(r"[^a-zA-z]","",text)
    text = re.sub("\S+"," ",text)

    return text
