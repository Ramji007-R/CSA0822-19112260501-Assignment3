# Tuple as Dictionary Key

bus_stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar",
    (13.0569, 80.2425): "Vadapalani"
}

print("Bus Stop Locations:")
for coordinates, name in bus_stops.items():
    print(coordinates, ":", name)

# Demonstrating the List Aliasing Problem
rows = 3
cols = 4

bad_grid = [[0] * cols] * rows
bad_grid[0][1] = 7

print("\nBad Grid:", bad_grid)

# Correct Method Using List Comprehension
good_grid = [[0 for _ in range(cols)] for _ in range(rows)]
good_grid[0][1] = 7

print("Good Grid:", good_grid)

# Shallow Copy and Deep Copy
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 100

print("\nOriginal:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)

# Tuple Immutability
location = ("T. Nagar", 13.0418, 80.2341)
print("\nLocation:", location)
print("Bus Stop Name:", location[0])
