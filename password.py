# Strong random password generator in python
# By umang mishra
import secrets
import string as s

length = secrets.choice(range(18,32))
symbols = s.ascii_letters + s.digits + s.punctuation
password = "".join(secrets.choice(symbols)
for i in range(length))

print(password)
