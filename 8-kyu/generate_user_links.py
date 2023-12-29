from urllib.parse import quote

def generate_link(user):
    encoded_username = quote(user)
    return f"http://www.codewars.com/users/{encoded_username}"