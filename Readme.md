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