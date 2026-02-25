import statistics

# Last 10 days sample data — Gandhinagar
temperatures = [24.5, 25.1, 26.0, 23.9, 24.8, 25.6, 26.2, 24.3, 23.7, 25.0]
humidity = [58, 60, 55, 65, 62, 59, 57, 63, 66, 61]

avg_temp = statistics.mean(temperatures)
median_temp = statistics.median(temperatures)

avg_humidity = statistics.mean(humidity)
median_humidity = statistics.median(humidity)

print("Weather Analysis (Temp & Humidity)")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Median Temperature: {median_temp:.2f} °C")
print(f"Average Humidity: {avg_humidity:.2f} %")
print(f"Median Humidity: {median_humidity:.2f} %")
