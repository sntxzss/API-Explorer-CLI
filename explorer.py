import jokes_api as joke
import weather_api as wea
def show_menu():
    while True:
        print("1. Weather")
        print("2. Joke")
        print("3. History")
        print("0. Exit")
        choose = input("Choose: ")
        if choose == '0':
          break
        elif choose == '1':
         city = input("Tell me your city: ")

        elif choose == '2':
         setup, punchline = joke.get_joke()
         print(setup)
         wh = input("Wanna hear punchline? y/n ").lower()
         if wh == 'y':
          print(punchline)
         else:
          print("Ugh, okay")
        elif choose == '3':
          
        else:
          print("No such choice.")