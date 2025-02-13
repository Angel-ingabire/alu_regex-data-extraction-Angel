import re
def validate_url(url):
    pattern = r'^(https?://)?(www\.)?[\w.-]+\.[a-z]{2,6}(/\S*)?$'
    return bool(re.match(pattern, url))

def validate_url(url):
    """Validates URLs (http, https, subdomains, and paths)."""
    pattern = r'^(https?://)?(www\.)?[\w.-]+\.[a-z]{2,6}(/\S*)?$'
    return bool(re.fullmatch(pattern, url))


