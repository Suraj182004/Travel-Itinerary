# Travel Itinerary Management System

A backend system for managing travel itineraries with the following components:
1. Database architecture for trip itineraries using SQLAlchemy
2. RESTful API endpoints for creating and viewing itineraries
3. MCP server that provides recommended itineraries based on duration

## Features

- Day-wise hotel accommodations, transfers, and activities management
- Relationship between all travel entities
- Seeded database with realistic data for Phuket and Krabi regions in Thailand
- Recommended itineraries ranging from 2-8 nights
- RESTful API endpoints with proper validation and documentation
- MCP server for itinerary recommendations

## Project Structure
```
/
├── app/
│ ├── database/ # Database models and connection
│ ├── api/ # FastAPI endpoints
│ ├── mcp/ # MCP server
│ ├── services/ # Business logic
│ ├── utils/ # Helpers and utilities
│ ├── config.py # Configuration settings
│ └── main.py # Application entry point
├── data/
│ └── seed_data.py # Database seeding script
├── requirements.txt
└── README.md
```

## Setup and Installation

### Prerequisites

- Python 3.9+ installed
- pip package manager
- Git (for cloning the repository)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Travel-Itinerary
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python -m app.main
   ```
   The application will start on http://localhost:8000

5. **Access API documentation**
   
   After starting the server, visit:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Database Setup

The application uses SQLite by default for local development:

1. **Initialize the database**
   ```bash
   # The database tables are automatically created on application startup
   # No additional steps required
   ```

2. **Seed the database with sample data**
   ```bash
   python -m data.seed_data
   ```

## API Usage

### Create a Trip Itinerary

```
POST /api/v1/trips/
```
```json
{
  "name": "Custom Phuket Trip",
  "description": "A personalized 3-night Phuket adventure",
  "duration_nights": 3,
  "region": "Phuket",
  "accommodations": [
    {
      "hotel_name": "Beachfront Resort",
      "location": "Patong Beach",
      "room_type": "Deluxe Ocean View",
      "price_per_night": 120.0,
      "day_number": 1
    }
  ],
  "activities": [
    {
      "name": "Island Hopping Tour",
      "description": "Visit multiple islands around Phuket",
      "location": "Phi Phi Islands",
      "day_number": 2,
      "price": 65.0,
      "duration_minutes": 480,
      "includes_transfer": true
    }
  ]
}
```

### Get Recommendations

```
POST /api/v1/mcp/recommendations/
```
```json
{
  "nights": 3,
  "region": "Phuket"
}
```

