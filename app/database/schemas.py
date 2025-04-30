from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

# Base Schemas
class ActivityBase(BaseModel):
    name: str
    description: Optional[str] = None
    location: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    day_number: int
    price: Optional[float] = None
    duration_minutes: Optional[int] = None
    includes_transfer: bool = False

class AccommodationBase(BaseModel):
    hotel_name: str
    location: str
    check_in_date: Optional[datetime] = None
    check_out_date: Optional[datetime] = None
    room_type: Optional[str] = None
    price_per_night: Optional[float] = None
    day_number: int
    address: Optional[str] = None
    amenities: Optional[str] = None

class TransferBase(BaseModel):
    from_location: str
    to_location: str
    transfer_type: str
    departure_time: Optional[datetime] = None
    arrival_time: Optional[datetime] = None
    day_number: int
    price: Optional[float] = None
    duration_minutes: Optional[int] = None

class TripBase(BaseModel):
    name: str
    description: Optional[str] = None
    duration_nights: int
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    total_price: Optional[float] = None
    region: str

# Create Schemas
class ActivityCreate(ActivityBase):
    pass

class AccommodationCreate(AccommodationBase):
    pass

class TransferCreate(TransferBase):
    pass

class TripCreate(TripBase):
    accommodations: Optional[List[AccommodationCreate]] = None
    transfers: Optional[List[TransferCreate]] = None
    activities: Optional[List[ActivityCreate]] = None

# Response Schemas
class Activity(ActivityBase):
    id: int
    trip_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Accommodation(AccommodationBase):
    id: int
    trip_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Transfer(TransferBase):
    id: int
    trip_id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Trip(TripBase):
    id: int
    is_recommended: bool
    created_at: datetime
    updated_at: datetime
    accommodations: List[Accommodation]
    transfers: List[Transfer]
    activities: List[Activity]

    class Config:
        orm_mode = True

# MCP Request Schema
class RecommendationRequest(BaseModel):
    nights: int = Field(..., ge=2, le=8, description="Number of nights for the trip (between 2-8)")
    region: Optional[str] = None