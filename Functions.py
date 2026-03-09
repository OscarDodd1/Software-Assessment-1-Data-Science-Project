import requests #Get requests
import json
import geocoder

data = {}

defaultList = ["Get Weather From Place", "Get Local Weather", "Other..."]

def Set_Info():
    with open("data.json", "r") as fp:
        data = json.load(fp)

    if data["BASE_URL"] == "":
        print("!-----No Base Url-----!")
        url = input("Base url: ")

        data["BASE_URL"] = url

    if data["API_KEY"] == "":
        print("!-----No Api key-----!")
        key = input("Api key: ")

        data["API_KEY"] = key

    # Write the dictionary to a JSON file
    with open("data.json", "w") as fp:
        json.dump(data, fp)

    return

def Display_Weather(weather_data):
    if weather_data:
        # Extract relevant data from the API response
        location = weather_data["location"]["name"]  # City name
        region = weather_data["location"]["region"]  # Region/State
        country = weather_data["location"]["country"]  # Country
        temperature = weather_data["current"]["temp_c"]  # Temperature in Celsius
        condition = weather_data["current"]["condition"]["text"]  # Weather condition (e.g., Sunny, Rainy)
        last_updated = weather_data["current"]["last_updated"]

        # Print the weather details
        print(f"-----Weather in {location}, {country} as of {last_updated}-----")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
    else:
        # Print an error message if data could not be retrieved
        print("Error retrieving weather data.")

def Get_Weather(place):
    with open("data.json", "r") as fp:
        data = json.load(fp)

    complete_url = f"{data["BASE_URL"]}/current.json?key={data["API_KEY"]}&q={place}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        # Return the JSON response as a Python dictionary
        return response.json()
    else:
        # Return None if there was an error with the request
        return None
    
def Get_Place_From_IP(IP):
    with open("data.json", "r") as fp:
        data = json.load(fp)
    
    place = ""

    complete_url = f"{data["BASE_URL"]}/ip.json?key={data["API_KEY"]}&q={IP}"

    response = requests.get(complete_url)

    if response.status_code == 200:
        place  =  response.json()["tz_id"]
        # Return the JSON response as a Python dictionary
        return place
    else:
        # Return None if there was an error with the request
        return None
    
def Get_local_IP():
    g = geocoder.ip('me')

    if g:
        return g.ip
    else:
        return None

def Get_Local_Weather():
    localIP = Get_local_IP()

    place = Get_Place_From_IP(localIP)

    return Get_Weather(place)

def Choose_Options(optionsList):
    # Most of this code makes the options list look nice
    characterLength = 35

    if optionsList == None:
        optionsList = defaultList

    lineString = ""

    for i in range(characterLength):
        lineString += "-"

    print(f"\n{lineString}")

    for i, option in enumerate(optionsList):
        changed = False

        fullString = f"| [{i + 1}] - {option}"

        if len(fullString) > (characterLength - 4):
            changed = True
            fullString = fullString[:characterLength - 4 -len(fullString)]

        if changed:
            fullString += "..."

        for i in range(characterLength - 1 - len(fullString)):
            fullString += " "

        fullString += "|"

        print(fullString)

    print(f"{lineString}\n")
    
    choice = None

    while choice == None:
        try:
            choice = int(input("Choice: "))
        except:
            choice = None
    
    return choice