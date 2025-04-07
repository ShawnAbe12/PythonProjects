import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# ==================== Set up the Flight Search ====================

data_manager = DataManager()
sheet_data = data_manager.get()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Set your origin airport
ORIGIN_CITY_IATA = "DFW"

# ==================== Update the Airport Codes in Google Sheet ====================
counter = 2
for row in sheet_data:
    if row["iataCode"] == "":
        response = flight_search.get_destination_code(row["city"])
        row["iataCode"] = response
        push = {"price": row}
        data_manager.put(push, counter)
    counter +=1

# ==================== Search for Flights and Send Notifications ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
counter = 2


for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)

    # ==================== Search for indirect flight if N/A ====================

    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["cost"]:
        notification_manager.send_message(destination["city"], cheapest_flight.price)
        notification_manager.send_email(destination["city"], cheapest_flight.price, cheapest_flight.stops)
        destination["cost"] = cheapest_flight.price
        push = {"price": destination}
        data_manager.put(push, counter)
    counter +=1



