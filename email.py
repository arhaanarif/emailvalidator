import re


def is_valid_email(email):


    email_pattern = re.compile(
        r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    )
    
    return re.match(email_pattern, email) is not None

emails_to_test = [
    "user@example.com",
    "@invaliduser.com",
    "user@subdomain.example.com",
    "python@python",
    "Python@cars.com",
    "plainaddress",
    "@missingusername.com",
    "username@.com",
    "user@domain..com"
]

for email in emails_to_test:
    print(f"{email}: {is_valid_email(email)}")
