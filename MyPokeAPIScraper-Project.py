import requests


while True:
    user_input = input('Enter a Pokemon name or type quit to exit: ').lower()
    if user_input == "quit":
        print("Exited program, press 'F5' to try again")
        break
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{user_input}")
    data = response.json()
    
    
    if response.status_code == 200:
        
        print(f"Name: {data['name'].capitalize()}")
        print(f"Height: {data['height']/10} {'Meters'}")
        print(f"Weight: {data['weight']/10} {'Kilograms'}")
        print(f"Ability: {data['abilities'][0].get('ability').get('name')}")

    elif response.status_code == 404:
        print("Could not find that. Please try again.")

    elif response.status_code == 500:
        print("Something went wrong, possible server issue. Please come back later.")
    
    else:
        print("Pokemon names are one word, with hypens instead of spaces. Please try again.")
