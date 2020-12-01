import csv
import random
from faker import Faker

faker = Faker("en_US")

with open("fakeleads.csv", "a", newline="") as fakeleads:
    columns = ["FirstName",
               "LastName",
               "Email",
               "Phone",
               "Address",
               "City",
               "State",
               "Zip",
               "Agent",
               "Notes",
               "LeadSource"]
    writer = csv.DictWriter(fakeleads, fieldnames=columns)
    if fakeleads is None:
        writer.writeheader()
    for i in range(1000):
        fakeData = [
            faker.first_name(),
            faker.last_name(),
            faker.email(),
            f"({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}",
            faker.street_address(),
            faker.city(),
            faker.state(),
            faker.postalcode(),
            "",
            "",
            ""
        ]
        writer.writerow({field: data for field, data in zip(columns, fakeData)})
