import datetime
from sqlalchemy.orm import Session
from app.database.models import Trip, Accommodation, Transfer, Activity
from app.database.session import SessionLocal
import os

def seed_database():
    db = SessionLocal()
    try:
        # First, check if we already have data
        existing_trips = db.query(Trip).count()
        if existing_trips > 0:
            print("Database already has data. Skipping seed operation.")
            return
        
        print("Seeding database with sample itineraries for Phuket and Krabi...")
        
        # Seed Phuket itineraries (2, 3, 4, 5 nights)
        seed_phuket_itineraries(db)
        
        # Seed Krabi itineraries (2, 3, 4, 5 nights)
        seed_krabi_itineraries(db)
        
        db.commit()
        print("Database seeding completed successfully!")
        
    finally:
        db.close()

def seed_phuket_itineraries(db: Session):
    # 2 Nights Phuket
    trip_2n = Trip(
        name="Quick Phuket Escape",
        description="A short 2-night getaway to explore the highlights of Phuket",
        duration_nights=2,
        region="Phuket",
        is_recommended=True,
        total_price=250.0
    )
    db.add(trip_2n)
    db.flush()
    
    # Add accommodations
    db.add(Accommodation(
        trip_id=trip_2n.id,
        hotel_name="Patong Beach Hotel",
        location="Patong",
        room_type="Deluxe Room",
        price_per_night=80.0,
        day_number=1,
        address="123 Patong Beach Road, Patong, Phuket",
        amenities="Swimming pool, Free WiFi, Restaurant, Beach access"
    ))
    
    db.add(Accommodation(
        trip_id=trip_2n.id,
        hotel_name="Patong Beach Hotel",
        location="Patong",
        room_type="Deluxe Room",
        price_per_night=80.0,
        day_number=2,
        address="123 Patong Beach Road, Patong, Phuket",
        amenities="Swimming pool, Free WiFi, Restaurant, Beach access"
    ))
    
    # Add transfers
    db.add(Transfer(
        trip_id=trip_2n.id,
        from_location="Phuket Airport",
        to_location="Patong Beach Hotel",
        transfer_type="Private Van",
        day_number=1,
        price=20.0,
        duration_minutes=45
    ))
    
    db.add(Transfer(
        trip_id=trip_2n.id,
        from_location="Patong Beach Hotel",
        to_location="Phuket Airport",
        transfer_type="Private Van",
        day_number=3,  # Departure day
        price=20.0,
        duration_minutes=45
    ))
    
    # Add activities
    db.add(Activity(
        trip_id=trip_2n.id,
        name="Phi Phi Islands Tour",
        description="Full-day speedboat tour to Phi Phi Islands including Maya Bay and Monkey Beach",
        location="Phi Phi Islands",
        day_number=2,
        price=70.0,
        duration_minutes=480,
        includes_transfer=True
    ))
    
    db.add(Activity(
        trip_id=trip_2n.id,
        name="Patong Night Market & Dinner",
        description="Evening exploration of Patong's vibrant night market with dinner at a local restaurant",
        location="Patong",
        day_number=1,
        price=25.0,
        duration_minutes=180,
        includes_transfer=False
    ))
    
    # 4 Nights Phuket
    trip_4n = Trip(
        name="Phuket Island Explorer",
        description="A 4-night adventure exploring the best beaches and attractions of Phuket",
        duration_nights=4,
        region="Phuket",
        is_recommended=True,
        total_price=520.0
    )
    db.add(trip_4n)
    db.flush()
    
    # Add accommodations
    for day in range(1, 5):
        db.add(Accommodation(
            trip_id=trip_4n.id,
            hotel_name="Kata Beach Resort",
            location="Kata Beach",
            room_type="Ocean View Suite",
            price_per_night=100.0,
            day_number=day,
            address="99 Kata Road, Kata Beach, Phuket",
            amenities="Beachfront, 2 Swimming pools, Spa, 3 Restaurants, Fitness center"
        ))
    
    # Add transfers
    db.add(Transfer(
        trip_id=trip_4n.id,
        from_location="Phuket Airport",
        to_location="Kata Beach Resort",
        transfer_type="Private Car",
        day_number=1,
        price=25.0,
        duration_minutes=60
    ))
    
    db.add(Transfer(
        trip_id=trip_4n.id,
        from_location="Kata Beach Resort",
        to_location="Phuket Airport",
        transfer_type="Private Car",
        day_number=5,  # Departure day
        price=25.0,
        duration_minutes=60
    ))
    
    # Add activities
    activities_4n = [
        Activity(
            trip_id=trip_4n.id,
            name="Big Buddha & Chalong Temple Tour",
            description="Half-day tour to Phuket's iconic Big Buddha statue and the historic Chalong Temple",
            location="Various locations in Phuket",
            day_number=2,
            price=40.0,
            duration_minutes=240,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_4n.id,
            name="Phuket Old Town Walking Tour",
            description="Guided walking tour of Phuket Old Town with its colorful Sino-Portuguese buildings",
            location="Phuket Old Town",
            day_number=3,
            price=30.0,
            duration_minutes=180,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_4n.id,
            name="Phang Nga Bay Sea Canoe",
            description="Full-day sea canoe adventure exploring the limestone karsts of Phang Nga Bay",
            location="Phang Nga Bay",
            day_number=4,
            price=85.0,
            duration_minutes=480,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_4n.id,
            name="Thai Cooking Class",
            description="Learn to prepare authentic Thai dishes with a local chef",
            location="Kata Beach",
            day_number=3,
            price=55.0,
            duration_minutes=240,
            includes_transfer=False
        )
    ]
    for activity in activities_4n:
        db.add(activity)

def seed_krabi_itineraries(db: Session):
    # 3 Nights Krabi
    trip_3n = Trip(
        name="Krabi Beach Getaway",
        description="A relaxing 3-night stay in the stunning beaches and limestone cliffs of Krabi",
        duration_nights=3,
        region="Krabi",
        is_recommended=True,
        total_price=380.0
    )
    db.add(trip_3n)
    db.flush()
    
    # Add accommodations
    for day in range(1, 4):
        db.add(Accommodation(
            trip_id=trip_3n.id,
            hotel_name="Railay Bay Resort & Spa",
            location="Railay Beach",
            room_type="Deluxe Cottage",
            price_per_night=95.0,
            day_number=day,
            address="Railay Beach, Krabi",
            amenities="Beachfront, Swimming pool, Spa, Restaurant, Free kayaking"
        ))
    
    # Add transfers
    db.add(Transfer(
        trip_id=trip_3n.id,
        from_location="Krabi Airport",
        to_location="Ao Nang Pier",
        transfer_type="Shared Minivan",
        day_number=1,
        price=10.0,
        duration_minutes=40
    ))
    
    db.add(Transfer(
        trip_id=trip_3n.id,
        from_location="Ao Nang Pier",
        to_location="Railay Beach",
        transfer_type="Longtail Boat",
        day_number=1,
        price=5.0,
        duration_minutes=15
    ))
    
    db.add(Transfer(
        trip_id=trip_3n.id,
        from_location="Railay Beach",
        to_location="Ao Nang Pier",
        transfer_type="Longtail Boat",
        day_number=4,  # Departure day
        price=5.0,
        duration_minutes=15
    ))
    
    db.add(Transfer(
        trip_id=trip_3n.id,
        from_location="Ao Nang Pier",
        to_location="Krabi Airport",
        transfer_type="Shared Minivan",
        day_number=4,  # Departure day
        price=10.0,
        duration_minutes=40
    ))
    
    # Add activities
    activities_3n = [
        Activity(
            trip_id=trip_3n.id,
            name="Four Islands Tour",
            description="Full-day longtail boat tour to four beautiful islands: Chicken Island, Tup Island, Poda Island, and Phra Nang Cave Beach",
            location="Krabi Islands",
            day_number=2,
            price=40.0,
            duration_minutes=420,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_3n.id,
            name="Rock Climbing at Railay",
            description="Half-day rock climbing experience on Railay's world-famous limestone cliffs (suitable for beginners)",
            location="Railay Beach",
            day_number=3,
            price=60.0,
            duration_minutes=240,
            includes_transfer=False
        ),
        Activity(
            trip_id=trip_3n.id,
            name="Sunset Dinner at The Grotto",
            description="Special dinner at The Grotto restaurant set inside a limestone cave with stunning sunset views",
            location="Railay Beach",
            day_number=3,
            price=70.0,
            duration_minutes=180,
            includes_transfer=False
        )
    ]
    for activity in activities_3n:
        db.add(activity)
        
    # 5 Nights Krabi
    trip_5n = Trip(
        name="Complete Krabi Adventure",
        description="An extensive 5-night exploration of Krabi's mainland and island attractions",
        duration_nights=5,
        region="Krabi",
        is_recommended=True,
        total_price=650.0
    )
    db.add(trip_5n)
    db.flush()
    
    # Add accommodations - 3 nights Ao Nang, 2 nights Koh Lanta
    for day in range(1, 4):
        db.add(Accommodation(
            trip_id=trip_5n.id,
            hotel_name="Centara Grand Beach Resort",
            location="Ao Nang",
            room_type="Deluxe Garden View",
            price_per_night=110.0,
            day_number=day,
            address="396-396/1 Moo 2, Ao Nang, Muang, Krabi",
            amenities="Private beach, Swimming pools, Spa, 4 Restaurants, Water sports"
        ))
    
    for day in range(4, 6):
        db.add(Accommodation(
            trip_id=trip_5n.id,
            hotel_name="Pimalai Resort & Spa",
            location="Koh Lanta",
            room_type="Deluxe Room",
            price_per_night=150.0,
            day_number=day,
            address="99 Moo 5, Ba Kan Tiang Beach, Koh Lanta",
            amenities="Infinity pools, Spa, Fine dining, Tennis courts, Private beach"
        ))
    
    # Add transfers
    transfers_5n = [
        Transfer(
            trip_id=trip_5n.id,
            from_location="Krabi Airport",
            to_location="Centara Grand Beach Resort",
            transfer_type="Private Car",
            day_number=1,
            price=30.0,
            duration_minutes=30
        ),
        Transfer(
            trip_id=trip_5n.id,
            from_location="Centara Grand Beach Resort",
            to_location="Klong Jilad Pier",
            transfer_type="Private Car",
            day_number=4,
            price=15.0,
            duration_minutes=25
        ),
        Transfer(
            trip_id=trip_5n.id,
            from_location="Klong Jilad Pier",
            to_location="Koh Lanta",
            transfer_type="Ferry",
            day_number=4,
            price=20.0,
            duration_minutes=90
        ),
        Transfer(
            trip_id=trip_5n.id,
            from_location="Koh Lanta",
            to_location="Krabi Airport",
            transfer_type="Speedboat and Car",
            day_number=6,
            price=55.0,
            duration_minutes=120
        )
    ]
    for transfer in transfers_5n:
        db.add(transfer)
    
    # Add activities
    activities_5n = [
        Activity(
            trip_id=trip_5n.id,
            name="Emerald Pool and Hot Springs Tour",
            description="Full-day tour to the natural Emerald Pool and relaxing Hot Springs",
            location="Krabi Mainland",
            day_number=2,
            price=50.0,
            duration_minutes=360,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_5n.id,
            name="Hong Island Kayaking",
            description="Full-day sea kayaking adventure around the stunning Hong Islands",
            location="Hong Islands",
            day_number=3,
            price=65.0,
            duration_minutes=420,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_5n.id,
            name="Koh Lanta National Park Excursion",
            description="Half-day guided tour of Koh Lanta National Park with its lighthouse and hiking trails",
            location="Koh Lanta",
            day_number=4,
            price=35.0,
            duration_minutes=240,
            includes_transfer=True
        ),
        Activity(
            trip_id=trip_5n.id,
            name="Four Islands Snorkeling Trip",
            description="Full-day snorkeling trip to Koh Chuek, Koh Mook (with Emerald Cave), Koh Kradan and Koh Ngai",
            location="Islands near Koh Lanta",
            day_number=5,
            price=60.0,
            duration_minutes=480,
            includes_transfer=True
        )
    ]
    for activity in activities_5n:
        db.add(activity)

# Check if we're running in Render or production environment
if os.environ.get("RENDER") or os.environ.get("PRODUCTION"):
    # Auto-run the seed database function when imported in production environment
    seed_database()

if __name__ == "__main__":
    seed_database()