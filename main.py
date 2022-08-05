#faker
from faker import Faker

fake = Faker()
name = "Name" + fake.name()+ "\n"
address = "Address:"+ fake.address()

print(name,address)
