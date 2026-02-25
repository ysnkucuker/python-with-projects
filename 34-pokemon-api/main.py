import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon"

# 1️⃣ List the first 10 Pokemon
print("\nFirst 10 Pokemon:\n")

response = requests.get(f"{BASE_URL}?limit=10")
data = response.json()

for i, pokemon in enumerate(data["results"], start=1):
    print(f"{i}. {pokemon['name']}")

# 2️⃣ Ask the user to enter a Pokemon name
pokemon_name = input("\nEnter the name of the Pokemon you want to see details for: ").lower()

# 3️⃣ Fetch Pokemon details
response = requests.get(f"{BASE_URL}/{pokemon_name}")

if response.status_code == 200:
    pokemon_data = response.json()

    print(f"\nPokemon: {pokemon_data['name'].title()}")
    print(f"ID: {pokemon_data['id']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")

    print("\nTypes:")
    for t in pokemon_data['types']:
        print("-", t['type']['name'])

    # Official artwork image
    image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']

    print("\nPokemon Image URL:")
    print(image_url)

else:
    print("Pokemon not found!")