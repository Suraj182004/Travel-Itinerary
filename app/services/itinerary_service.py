from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List, Optional

from app.database import models, schemas

class ItineraryService:
    @staticmethod
    def create_trip(db: Session, trip: schemas.TripCreate):
        """Create a new trip with its related entities"""
        # Create trip
        db_trip = models.Trip(
            name=trip.name,
            description=trip.description,
            duration_nights=trip.duration_nights,
            start_date=trip.start_date,
            end_date=trip.end_date,
            total_price=trip.total_price,
            region=trip.region
        )
        db.add(db_trip)
        db.flush()  # Flush to get the trip ID

        # Create accommodations
        if trip.accommodations:
            for accommodation in trip.accommodations:
                db_accommodation = models.Accommodation(
                    trip_id=db_trip.id,
                    **accommodation.dict()
                )
                db.add(db_accommodation)

        # Create transfers
        if trip.transfers:
            for transfer in trip.transfers:
                db_transfer = models.Transfer(
                    trip_id=db_trip.id,
                    **transfer.dict()
                )
                db.add(db_transfer)

        # Create activities
        if trip.activities:
            for activity in trip.activities:
                db_activity = models.Activity(
                    trip_id=db_trip.id,
                    **activity.dict()
                )
                db.add(db_activity)

        db.commit()
        db.refresh(db_trip)
        return db_trip

    @staticmethod
    def get_trips(
        db: Session, 
        skip: int = 0, 
        limit: int = 100, 
        region: Optional[str] = None,
        duration: Optional[int] = None
    ) -> List[models.Trip]:
        """Get all trips with optional filtering"""
        query = db.query(models.Trip)
        
        # Apply filters if provided
        if region:
            query = query.filter(models.Trip.region == region)
        
        if duration:
            query = query.filter(models.Trip.duration_nights == duration)
        
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_trip_by_id(db: Session, trip_id: int) -> Optional[models.Trip]:
        """Get a trip by its ID"""
        return db.query(models.Trip).filter(models.Trip.id == trip_id).first()

    @staticmethod
    def delete_trip(db: Session, trip_id: int) -> None:
        """Delete a trip by its ID"""
        db.query(models.Trip).filter(models.Trip.id == trip_id).delete()
        db.commit()

    @staticmethod
    def get_recommended_itineraries(
        db: Session, 
        nights: int,
        region: Optional[str] = None
    ) -> List[models.Trip]:
        """Get recommended itineraries for the given duration and region"""
        query = db.query(models.Trip).filter(
            models.Trip.is_recommended == True,
            models.Trip.duration_nights == nights
        )
        
        if region:
            query = query.filter(models.Trip.region == region)
        
        return query.all() 