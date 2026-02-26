import requests #Get requests
import json

data = {}

def Set_Info():

    url = input("Base url: ")
    key = input("Api key: ")

    # Write the dictionary to a JSON file
    with open('data.json', 'w') as fp:
        json.dump(data, fp) #

    if url == "":
        print("!-----No Base Url-----!")
    
    if key == "":
        print("!-----No API key-----!")
    
    if key == "" or url == "":
        exit("\n---Exiting program---")

def Get_Weather(place):
    print(place, data,)