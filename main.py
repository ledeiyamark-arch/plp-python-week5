from helpers import tables_needed, welcome
from password_generator import make_password


print(welcome("Amina"))

print("Tables needed:", tables_needed(10, 4))

print("Password:", make_password(8))