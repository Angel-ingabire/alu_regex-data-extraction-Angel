import re
def validate_credit_card(card):
    pattern = r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$'
    return bool(re.match(pattern, card))