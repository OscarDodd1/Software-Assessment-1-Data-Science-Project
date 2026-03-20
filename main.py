#!!!!! IMPORTANT: Use | pip install -r requirements.txt | to install all dependancies

import sys #Import system for exiting program
import time #Import time to get the time
from Functions import Set_Info, Clear_Info, Get_Weather, Get_Local_Weather, Display_Weather, Choose_Options, Get_local_IP, Show_Recent_Searches, Clear_Recent_Searches, Help 
#Get functions from Functions.py

#Api key cc57d655a5444de890d222902262602 #NO LONGER WORKS

#Base url http://api.weatherapi.com/v1

#Main Loop
def main():
    while True:
        option = Choose_Options(None) #User choice

        print("") #Go to another lineaasazazz

        if option == 1:
            place = input("Place to get weather from: ")
            Display_Weather(Get_Weather(place))
        elif option == 2:
            Display_Weather(Get_Local_Weather())
        elif option == 3:
            Show_Recent_Searches()
        elif option == 4:
            Help()
        elif option == 5:
            option2 = Choose_Options(["Set Info (Checks key data)", "Clear Key Data", "Clear Recent Searches", "Get IP", "Exit Program"])
            if option2 == 1:
                Set_Info()
            elif option2 == 2:
                Clear_Info()
            elif option2 == 3:
                Clear_Recent_Searches()
            elif option2 == 4:
                ip = Get_local_IP()

                if not ip:
                    print("IP not found")
                else:
                    print(ip)
            elif option2 == 5:
                print("\n---Exiting program---")
                sys.exit()

        time.sleep(1)

if __name__ == "__main__":
    #Set info
    Set_Info()

    #Run main loop
    main()