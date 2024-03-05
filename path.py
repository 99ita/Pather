from itertools import permutations

def calculate_total_time(path, hourly_matrices, start_hour):
    total_time = 0.0
    current_hour = start_hour * 60  # Convert start hour to minutes
    arrival_times = []

    for i in range(len(path) - 1):
        travel_time = hourly_matrices[current_hour // 60 % 14][path[i]][path[i+1]]
        total_time += travel_time
        arrival_times.append(current_hour)
        current_hour += travel_time

    # Return to the starting city
    arrival_times.append(current_hour)

    return total_time, arrival_times

def convert_to_time(minutes):
    hours, minutes = divmod(int(minutes), 60)
    return f"{hours:02d}:{minutes:02d}"

def brute_force_tsp(hourly_matrices, city_names):
    num_cities = len(hourly_matrices[0][0])  # Assuming the same number of cities for all matrices
    min_time = float('inf')
    optimal_path = None
    optimal_arrival_times = None
    optimal_start_hour = None

    for start_hour in range(14):
        all_paths = permutations(range(1, num_cities))  # Exclude the first city from permutations
        for path in all_paths:
            path = (0,) + path + (0,)  # Add the first city at the beginning and end
            time, arrival_times = calculate_total_time(path, hourly_matrices, start_hour)
            if time < min_time:
                min_time = time
                optimal_path = path
                optimal_arrival_times = arrival_times
                optimal_start_hour = start_hour

    return optimal_path, min_time, optimal_arrival_times, optimal_start_hour

# Example usage:
city_names = ["City A", "City B", "City C", "City D"]  # Replace with your actual city names

optimal_path, min_time, optimal_arrival_times, optimal_start_hour = brute_force_tsp(hourly_matrices, city_names)
print(f"\nOptimal Path (Starting at {optimal_start_hour + 7:02d}:00):")
for city_index in optimal_path:
    print(f"{city_names[city_index]} -> ", end="")
print(f"\nMinimum Time: {min_time:.2f} minutes")  # Display min_time with 2 decimal places

# Print departure and arrival times for each city
for i, city_index in enumerate(optimal_path[:-1]):
    departure_time = optimal_arrival_times[i]
    arrival_time = optimal_arrival_times[i+1]
    print(f"Departure from {city_names[city_index]} at {convert_to_time(departure_time)}, Arrival time: {convert_to_time(arrival_time)}")
