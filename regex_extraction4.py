import re

def validate_phone_number(phone):
    """Validates phone numbers (various formats)."""
    pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.fullmatch(pattern, phone))


phones = ["(123) 456-7890", "123-456-7890", "123.456.7890", "000-000"]
for phone in phones:
    print(f"{phone}: {' Valid' if validate_phone_number(phone) else ' Invalid'}")

