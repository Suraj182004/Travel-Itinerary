from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database.session import get_db
from app.database import schemas
from app.services.itinerary_service import ItineraryService

router = APIRouter()

@router.post("/recommendations/", response_model=List[schemas.Trip])
def get_recommendations(request: schemas.RecommendationRequest, db: Session = Depends(get_db)):
    """
    Get recommended itineraries based on the number of nights
    
    - **nights**: Number of nights for the trip (2-8 nights)
    - **region**: Optional region filter (e.g., "Phuket", "Krabi")
    """
    # Get recommended itineraries for the given duration
    recommendations = ItineraryService.get_recommended_itineraries(
        db=db, 
        nights=request.nights,
        region=request.region
    )
    
    if not recommendations:
        raise HTTPException(
            status_code=404, 
            detail=f"No recommended itineraries found for {request.nights} nights"
        )
    
    return recommendations