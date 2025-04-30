from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Trip(Base):
    __tablename__ = "trips"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    duration_nights = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    total_price = Column(Float, nullable=True)
    is_recommended = Column(Boolean, default=False)
    region = Column(String(100), nullable=False)  # e.g., "Phuket", "Krabi"
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    accommodations = relationship("Accommodation", back_populates="trip", cascade="all, delete-orphan")
    transfers = relationship("Transfer", back_populates="trip", cascade="all, delete-orphan")
    activities = relationship("Activity", back_populates="trip", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Trip {self.name} ({self.duration_nights} nights)>"


class Accommodation(Base):
    __tablename__ = "accommodations"
    
    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    hotel_name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    check_in_date = Column(DateTime, nullable=True)
    check_out_date = Column(DateTime, nullable=True)
    room_type = Column(String(100), nullable=True)
    price_per_night = Column(Float, nullable=True)
    day_number = Column(Integer, nullable=False)  # Which day of the itinerary (1-based)
    address = Column(Text, nullable=True)
    amenities = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    trip = relationship("Trip", back_populates="accommodations")
    
    def __repr__(self):
        return f"<Accommodation {self.hotel_name} (Day {self.day_number})>"


class Transfer(Base):
    __tablename__ = "transfers"
    
    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    from_location = Column(String(255), nullable=False)
    to_location = Column(String(255), nullable=False)
    transfer_type = Column(String(100), nullable=False)  # e.g., "Taxi", "Ferry", "Flight"
    departure_time = Column(DateTime, nullable=True)
    arrival_time = Column(DateTime, nullable=True)
    day_number = Column(Integer, nullable=False)  # Which day of the itinerary (1-based)
    price = Column(Float, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    trip = relationship("Trip", back_populates="transfers")
    
    def __repr__(self):
        return f"<Transfer {self.from_location} to {self.to_location} (Day {self.day_number})>"


class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=False)
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    day_number = Column(Integer, nullable=False)  # Which day of the itinerary (1-based)
    price = Column(Float, nullable=True)
    duration_minutes = Column(Integer, nullable=True)
    includes_transfer = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    trip = relationship("Trip", back_populates="activities")
    
    def __repr__(self):
        return f"<Activity {self.name} (Day {self.day_number})>"