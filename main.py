#!!!!! IMPORTANT: Use | pip install -r requirements.txt | to install all dependancies

import time
from Functions import Set_Info, Get_Weather, Get_Local_Weather, Display_Weather, Choose_Options #Get functions

#Api key cc57d655a5444de890d222902262602

#Base url http://api.weatherapi.com/v1

Set_Info()

#Main Loop
while True:
    Display_Weather(Get_Local_Weather())
    time.sleep(10)