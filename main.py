#!!!!! IMPORTANT: Use | pip install -r requirements.txt | to install all dependancies

import time
from Functions import Set_Info, Get_Weather, Get_Local_Weather, Display_Weather, Choose_Options, Get_local_IP #Get functions

#Api key cc57d655a5444de890d222902262602

#Base url http://api.weatherapi.com/v1

#Set info
Set_Info()

#Main Loop
while True:
    option = Choose_Options(None)
    if option == 1:
        place = input("Place to get weather from: ")
        Display_Weather(Get_Weather(place))
    elif option == 2:
        Display_Weather(Get_Local_Weather())
    elif option == 3:
        option2 = Choose_Options({"Set Info", "Get IP"})
        if option2 == 1:
            Set_Info()
        elif option2 == 2:
            ip = Get_local_IP()

            if not ip:
                print("IP not found")
            else:
                print(ip)

    time.sleep(1)