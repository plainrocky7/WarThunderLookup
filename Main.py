import requests
import json
vehical = input("What vehicle would you like too lookup? ")
url = f"https://wtvehiclesapi.sgambe.serv00.net/api/vehicles/{vehical}"
req = requests.get(url)
with open(f"{vehical}.json", "w") as f:
    json.dump(req.json(), f, indent=4)
print(f"info about {vehical} has been saved too {vehical}.json")