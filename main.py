import requests

print("Temperature checker!")
while True:
    user_input = input("Type your city to check its temperature or type 'e' to exit the program:\n")
    if user_input == "e":
        print("heye")
        break

    city = user_input.title()
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]
        print(f"Currently the temperature in your city is {temp}°C\n")
    
    else:
        print("Sorry, something went wrong. Make sPure you type your city correctly.")
