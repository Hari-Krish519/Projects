import requests
pokemon = input("Which of the pokemon you want:")
pokemon = pokemon.lower()

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

req = requests.get(url)


if req.status_code == 200:
    data = req.json()
    print(f"Name is\t\t: {data['name']}")
    print("Abilities")
    for i in data['abilities']:
        #print(i)
        #print(i['ability'])
        print(i['ability'] ['name'])
else:
    print("Pokemon not found")

