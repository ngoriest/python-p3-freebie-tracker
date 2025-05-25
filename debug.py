from models import session, Company, Dev, Freebie
from seed import seed_data

def debug():
    print("Seeding data...")
    seed_data()
    
    print("\n=== Testing relationships ===")
    google = session.query(Company).filter_by(name="Google").first()
    print(f"Google's freebies: {[f.item_name for f in google.freebies]}")
    print(f"Alice's companies: {[c.name for c in google.devs[0].companies]}")
    
    print("\n=== Testing Freebie methods ===")
    freebie = google.freebies[0]
    print(f"Print details: {freebie.print_details()}")
    
    print("\n=== Testing Company methods ===")
    microsoft = session.query(Company).filter_by(name="Microsoft").first()
    new_freebie = microsoft.give_freebie(google.devs[0], "Hat", 20)
    print(f"New freebie created: {new_freebie.print_details()}")
    print(f"Oldest company: {Company.oldest_company().name}")
    
    print("\n=== Testing Dev methods ===")
    alice = session.query(Dev).filter_by(name="Alice").first()
    print(f"Alice received a T-shirt? {alice.received_one('T-shirt')}")
    print(f"Alice received a Pen? {alice.received_one('Pen')}")
    
    bob = session.query(Dev).filter_by(name="Bob").first()
    alice.give_away(bob, freebie)
    print(f"After give_away: {freebie.print_details()}")

if __name__ == '__main__':
    debug()