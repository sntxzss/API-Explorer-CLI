import jokes_api as joke
import weather_api as wea
import history as hist

def show_menu():
    while True:
        print("1. Weather")
        print("2. Joke")
        print("3. History")
        print("0. Exit")
        choose = input("Choose: ").strip()
        if choose == '0':
            break
        elif choose == '1':
            city = input("Tell me your city: ").strip()
            result = wea.get_forecast(city)
            if result and "error" not in result:
                print(f"Temperature: {result['temperature_2m']}°C")
                print(f"Wind: {result['wind_speed_10m']} km/h")
                hist.save_history("weather", city, f"Temp: {result['temperature_2m']}°C, Wind: {result['wind_speed_10m']} km/h")
            elif result and "error" in result:
                print(result["error"])
            else:
                print("Місто не знайдено")
        elif choose == '2':
            result = joke.get_joke()
            if isinstance(result, dict) and "error" in result:
                print(result["error"])
            else:
                setup, punchline = result
                print(setup)
                wh = input("Wanna hear punchline? y/n ").strip().lower()
                if wh == 'y':
                    print(punchline)
                else:
                    print("Ugh, okay")
                hist.save_history("joke", "random", f"{setup} - {punchline}")
        elif choose == '3':
            records = hist.get_history()
            if records:
                for i, record in enumerate(records, 1):
                    print(f"{i}. [{record['type']}] {record['time']}")
                    print(f"   Query: {record['query']}")
                    print(f"   Result: {record['result']}\n")
            else:
                print("No history yet")
        else:
            print("No such choice.")

if __name__ == "__main__":
    show_menu()