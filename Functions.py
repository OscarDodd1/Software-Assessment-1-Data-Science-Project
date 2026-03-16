import requests #Get requests
import json #json for data saving
import geocoder #get users location
from datetime import datetime #to get the current time

baseURL = "http://api.weatherapi.com/v1"

data = {"BASE_URL": baseURL, "API_KEY": ""} #variable to store the base url and the api key (doesnt permanently store it here for security)

saveData = {} #Just the previous searches
#variables in save data include:
#Place, Time/date saved, Temperature, Condition
#Looks like: "search1": {"Place": "Sydney", "Time": "2025-03-13 09:39:00", "Temperature": 24.2, "Condition": "Overcast"}

#File paths
keysFilePath = "keys.json"
saveDataPath = "saveData.json"

#default for the choose_option funciton
defaultList = ["Get Weather From Place", "Get Local Weather", "Show Recent Searches", "Other..."]


#Attempt to load files, if none then it will create them
try:
    with open(keysFilePath, "x") as file:
        json.dump(data, file)
    print(f"File '{keysFilePath}' created successfully.")
except FileExistsError:
    print(f"File '{keysFilePath}' loaded.")

try:
    with open(saveDataPath, "x") as file:
        json.dump(saveData, file)
    print(f"File '{saveDataPath}' created successfully.")
except FileExistsError:
    print(f"File '{saveDataPath}' loaded.")

def Set_Info():
    global data
    global saveData
    
    #read the files
    with open(keysFilePath, "r") as file:
        data = json.load(file)

    with open(saveDataPath, "r") as file:
        saveData = json.load(file)

    #checks if the variables are empty, if they are it asks the user to set them
    if data["BASE_URL"] == "":
        print("!-----No Base Url-----!")
        url = input("Base url: ")

        data["BASE_URL"] = url

    if data["API_KEY"] == "":
        print("!-----No Api key-----!")
        key = input("Api key: ")

        data["API_KEY"] = key

    #Write the dictionary to a json file
    with open(keysFilePath, "w") as file:
        json.dump(data, file)

    with open(saveDataPath, "w") as file:
        json.dump(saveData, file)

    return

def Clear_Info():
    #Clears the info in keys.json (this is here incase the user puts the wrong api key in and wants to change it without going into the files)
    data = {"BASE_URL": "", "API_KEY": ""}

    with open(keysFilePath, "w") as file:
        json.dump(data, file)

    print("Cleared data") #User feedback

    print("\nSet new data")

    Set_Info() #Sets the new data

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
    global data
    global saveData

    complete_url = f"{data["BASE_URL"]}/current.json?key={data["API_KEY"]}&q={place}"

    #gets the current time for data saving
    now = datetime.now()
    formatted_string = now.strftime("%Y-%m-%d %H:%M:%S")

    response = ""

    try:
        response = requests.get(complete_url)
    except:
        return None

    if response.status_code == 200:
        #Save the data
        with open(saveDataPath, "r") as file:
            saveData = json.load(file)

        saveNumStr = f"Search{len(saveData) + 1}"

        saveDictionary = {saveNumStr: {"Place": place, "Time": formatted_string, "Temperature": response.json()["current"]["temp_c"], "Condition": response.json()["current"]["condition"]["text"]}}

        saveData.update(saveDictionary) #Updates the variable

        with open(saveDataPath, "w") as file:
            json.dump(saveData, file)

        with open(saveDataPath, "r") as file:
            saveData = json.load(file)

        # Return the JSON response as a Python dictionary
        return response.json()
    else:
        #Save but with different information since there is no data
        with open(saveDataPath, "r") as file:
            saveData = json.load(file)

        saveNumStr = f"Search{len(saveData) + 1}"

        saveDictionary = {saveNumStr: {"Place": place, "Time": formatted_string, "Temperature": "No Data", "Condition": "No Data"}}

        saveData.update(saveDictionary) #Updates the variable

        with open(saveDataPath, "w") as file:
            json.dump(saveData, file)

        with open(saveDataPath, "r") as file:
            saveData = json.load(file)

        # Return None if there was an error with the request
        return None
    
def Get_Place_From_IP(IP): #Gets a location based on the ip given
    with open(keysFilePath, "r") as file:
        data = json.load(file)
    
    place = ""

    complete_url = f"{data["BASE_URL"]}/ip.json?key={data["API_KEY"]}&q={IP}" #Different search

    response = ""

    try:
        response = requests.get(complete_url)
    except:
        return None

    if response.status_code == 200:
        #return the location if one was found
        place = response.json()["tz_id"]
        return place
    else:
        #return nothing if there is an error
        return None
    
def Get_local_IP(): #Just gets the users public ip
    g = geocoder.ip('me')

    if g:
        return g.ip
    else:
        return None

def Get_Local_Weather(): #Gets the weather at the users location
    localIP = Get_local_IP() #get the ip

    place = Get_Place_From_IP(localIP) #get the location from the ip

    return Get_Weather(place) #return the weather from the place

def Choose_Options(optionsList):
    #Most of this code makes the options list look nice
    #All it does is check if the option string is longer than the max character length, if it is, it will shorten it

    characterLength = 38

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

    #Loops until the users choice is valid
    while choice == None:
        try:
            choice = int(input("Choice: "))
        except:
            choice = None
    
    return choice

def Show_Recent_Searches(): #Shows the recent searches from the saveData.json file
    print(f"-----[{len(saveData)} Recent Searches]-----")
    for search, subsearch in saveData.items():
        print(f"---{subsearch["Place"]} | {subsearch["Time"]}---")
        print(f"Temperature: {subsearch["Temperature"]}")
        print(f"Condition: {subsearch["Condition"]}\n")

def Clear_Recent_Searches(): #Clears all the data from the saveData.json file
    global saveData

    with open(saveDataPath, "w") as file:
        json.dump({}, file)

    with open(saveDataPath, "r") as file:
        saveData = json.load(file)

    print("---Cleared Recent Searches---") #User feedback