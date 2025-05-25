# seed.py
from models import session, Company, Dev, Freebie

def seed_data():
    # Clear existing data
    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()
    session.commit()

    # Create companies
    google = Company(name="Google", founding_year=1998)
    microsoft = Company(name="Microsoft", founding_year=1975)
    apple = Company(name="Apple", founding_year=1976)

    # Create devs
    dev1 = Dev(name="Alice")
    dev2 = Dev(name="Bob")
    dev3 = Dev(name="Charlie")

    # Add and commit
    session.add_all([google, microsoft, apple, dev1, dev2, dev3])
    session.commit()

    # Create freebies
    freebie1 = Freebie(item_name="T-shirt", value=15, dev=dev1, company=google)
    freebie2 = Freebie(item_name="Sticker", value=5, dev=dev2, company=microsoft)
    freebie3 = Freebie(item_name="Mug", value=10, dev=dev3, company=apple)
    freebie4 = Freebie(item_name="Laptop", value=1000, dev=dev1, company=apple)

    session.add_all([freebie1, freebie2, freebie3, freebie4])
    session.commit()

if __name__ == '__main__':
    seed_data()