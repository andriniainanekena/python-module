#!/usr/bin/env python3
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def create_valid_station() -> Optional[SpaceStation]:
    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.fromisoformat(
                "2024-01-15T10:30:00"
            ),
            is_operational=True,
            notes="All systems nominal",
        )
        return station
    except ValidationError as e:
        print("Error creating station:")
        for error in e.errors():
            print(error["msg"])
        return None
    except ValueError as e:
        print(f"Invalid date format: {e}")
        return None


def create_invalid_station() -> None:
    try:
        SpaceStation(
            station_id="BAD01",
            name="Bad Station",
            crew_size=25,
            power_level=80.0,
            oxygen_level=90.0,
            last_maintenance=datetime.fromisoformat(
                "2024-01-15T10:30:00"
            ),
        )
    except ValidationError as e:
        print("Expected validation error:")
        for error in e.errors():
            print(error["msg"])
    except ValueError as e:
        print(f"Invalid date format: {e}")


def display_station(station: SpaceStation) -> None:
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    if station.is_operational:
        status = "Operational"
    else:
        status = "Maintenance"
    print(f"Status: {status}")


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    station = create_valid_station()
    if station is not None:
        display_station(station)

    print("=" * 40)

    create_invalid_station()


if __name__ == "__main__":
    main()
