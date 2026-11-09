from dadjokes import Dadjoke  # type: ignore[import-untyped]
from faker import Faker

dadjoke = Dadjoke()
fake = Faker()

joke = dadjoke.joke

name = fake.name()
address = fake.address().replace("\n", ", ")

print(f"{name} lives at {address}. {name}'s favorite joke is '{joke}'")
