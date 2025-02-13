import re


def validate_credit_card(card):
    """Validates credit card numbers with spaces or dashes."""
    pattern = r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$'
    return bool(re.fullmatch(pattern, card))


cards = ["1234 5678 9012 3456", "1234-5678-9012-3456", "1111222233334444"]
for card in cards:
    print(f"{card}: {' Valid' if validate_credit_card(card) else ' Invalid'}")
