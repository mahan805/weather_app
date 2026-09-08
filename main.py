from weather import get_weather

city = input("Enter city name: ")

temperature = get_weather(city)

print(f"Temperature in {city} is {temperature} C")