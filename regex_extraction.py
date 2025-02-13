import re

def validate_email(email):
    """Validates an email address."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.fullmatch(pattern, email))

# Test Cases
emails = ["user@example.com", "firstname.lastname@company.co.uk", "wrong@format", "test@com"]
for email in emails:
    print(f"{email}: {' Valid' if validate_email(email) else 'Invalid'}")



