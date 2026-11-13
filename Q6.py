# Railway Timetable Management

trains = {
    101: {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00"),
            ("Vellore", "08:00"),
            ("Bangalore", "11:00")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    102: {
        "name": "Pandian Express",
        "stops": [
            ("Chennai", "21:00"),
            ("Madurai", "05:00")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    103: {
        "name": "Vaigai Express",
        "stops": [
            ("Chennai", "13:00"),
            ("Trichy", "17:00"),
            ("Madurai", "20:00")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    104: {
        "name": "Kovai Express",
        "stops": [
            ("Chennai", "06:10"),
            ("Salem", "10:00"),
            ("Coimbatore", "13:00")
        ],
        "days": {"Wednesday", "Thursday", "Sunday"}
    },

    105: {
        "name": "Nellai Express",
        "stops": [
            ("Chennai", "20:00"),
            ("Tirunelveli", "06:00")
        ],
        "days": {"Tuesday", "Friday", "Sunday"}
    }
}

# Create Station Index
station_index = {}

for train_no, details in trains.items():
    for station, departure in details["stops"]:
        station_index.setdefault(station, []).append(train_no)

# Search trains by station and day
search_station = input("Enter Station: ").strip()
search_day = input("Enter Day: ").strip().capitalize()

available_trains = []

for train_no in station_index.get(search_station, []):
    train = trains[train_no]

    if search_day in train["days"]:
        for station, departure in train["stops"]:
            if station == search_station:
                available_trains.append(
                    (departure, train_no, train["name"])
                )

# Display results sorted by departure time
available_trains.sort()

print("\nAvailable Trains:")

if available_trains:
    for departure, train_no, name in available_trains:
        print(train_no, name, "Departure:", departure)
else:
    print("No trains available.")
