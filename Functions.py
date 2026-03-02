import requests #Get requests
import json
import geocoder

data = {}

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

def Display_Weather(weather_data):
    if weather_data:
        # Extract relevant data from the API response
        location = weather_data["location"]["name"]  # City name
        region = weather_data["location"]["region"]  # Region/State
        country = weather_data["location"]["country"]  # Country
        temperature = weather_data["current"]["temp_c"]  # Temperature in Celsius
        condition = weather_data["current"]["condition"]["text"]  # Weather condition (e.g., Sunny, Rainy)

        # Print the weather details
        print(f"-----Weather in {location}, {country}-----")
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

def Choose_Options():
    #see local weather
    print("a")