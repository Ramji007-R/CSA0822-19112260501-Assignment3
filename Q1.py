# Daily Rainfall Analysis

rainfall = [i % 20 for i in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(rainfall[i:i + 7])
    for i in range(0, len(rainfall), 7)
]

# Maximum and minimum rainfall
max_rainfall = max(rainfall)
min_rainfall = min(rainfall)

max_day = rainfall.index(max_rainfall) + 1
min_day = rainfall.index(min_rainfall) + 1

# 7-day moving average
moving_average = [
    sum(rainfall[i:i + 7]) / 7
    for i in range(len(rainfall) - 6)
]

# Days with no rainfall
dry_days = [
    i + 1 for i, value in enumerate(rainfall)
    if value == 0
]

print("Weekly Rainfall Totals:", weekly_totals)
print("Maximum Rainfall:", max_rainfall, "on Day", max_day)
print("Minimum Rainfall:", min_rainfall, "on Day", min_day)
print("7-Day Moving Average:", moving_average)
print("Dry Days:", dry_days)
