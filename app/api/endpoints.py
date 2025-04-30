from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database.session import get_db
from app.database import schemas, models
from app.services.itinerary_service import ItineraryService

router = APIRouter()

@router.post("/trips/", response_model=schemas.Trip, status_code=status.HTTP_201_CREATED)
def create_trip(trip: schemas.TripCreate, db: Session = Depends(get_db)):
    """
    Create a new trip itinerary
    """
    return ItineraryService.create_trip(db=db, trip=trip)

@router.get("/trips/", response_model=List[schemas.Trip])
def get_trips(
    skip: int = 0, 
    limit: int = 100, 
    region: Optional[str] = None,
    duration: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """
    Get all trip itineraries with optional filtering by region and duration
    """
    return ItineraryService.get_trips(db=db, skip=skip, limit=limit, region=region, duration=duration)

@router.get("/trips/{trip_id}", response_model=schemas.Trip)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    """
    Get a specific trip itinerary by ID
    """
    trip = ItineraryService.get_trip_by_id(db=db, trip_id=trip_id)
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip

@router.delete("/trips/{trip_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_trip(trip_id: int, db: Session = Depends(get_db)):
    """
    Delete a trip itinerary
    """
    trip = ItineraryService.get_trip_by_id(db=db, trip_id=trip_id)
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip not found")
    ItineraryService.delete_trip(db=db, trip_id=trip_id)
    return {"message": "Trip deleted successfully"}