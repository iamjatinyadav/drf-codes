from faker import Faker
from faker.providers import internet

fake = Faker()

name = fake.name()

# print(fake.name())
# print(fake.address())
# print(fake.phone_number())
# print(fake.msisdn())
# print(fake.credit_card_full())
# print(fake.add_provider(internet))

# for _ in range(10):
#   print(fake.name())



