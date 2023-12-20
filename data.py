import json
import sys


# Specify the path to your JSON file
json_file_path = 'data420.json'

# Read JSON data from the file
with open(json_file_path, 'r') as file:
    json_data = file.read()

# Load JSON data
data = json.loads(json_data)

# Extract latitude and longitude

for i in range(len(data["result"]["elements"])):
    name = data["result"]["elements"][i]["data"]["properties"]["name"]
    latitude = data["result"]["elements"][i]["data"]["properties"]["lat"]
    longitude = data["result"]["elements"][i]["data"]["properties"]["lng"]




    #print
    with open('test.txt', 'a') as file:
        print(f"{name}, {latitude}, {longitude}", file=file)
        print("\n")
    
    

print(len(data["result"]["elements"]))

