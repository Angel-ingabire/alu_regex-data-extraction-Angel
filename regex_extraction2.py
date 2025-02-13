import re
def validate_url(url):
    pattern = r'^(https?://)?(www\.)?[\w.-]+\.[a-z]{2,6}(/\S*)?$'
    return bool(re.match(pattern, url))


