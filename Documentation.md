## **Requirements/Specifications**

### **Functional Specifications**

#### **User Requirements**: The user needs to be able to view the current weather, view and delete saved session data and change the api key all through the program and without having to edit the individual files.
#### **Inputs and Outputs**: The program needs to be able to accept inputs from the user when they are prompted and needs to output readable data for the user.
#### **Core Features**: The program needs to be able to get data from an api and convert it into readable information with error handling. The program also needs to be able to save the users data on a file and read it.
#### **User Interaction**: Users will interact with the program through the command line, they will be shown a list of functions that can be run. The user inputs a number corresponding to the function to run, and some of those functions require a string input which is inputed by the user.
#### **Error Handling**: Some error that the program could face are misinputs from the user, for example, the user inputs a string when an integer. These errors will be handled by the program using try except to prevent the program from breaking.

### **Non-Functional Specifications**

#### **Performance**: The program should be able to efficiently peform tasks with minimal delay. The data should be recieved from the api relatively quickly and if it cant connect within a reasonable time, it should timeout and inform the user to maintain their engagement.
#### **Useability/Accessibility**: The program could be more accesible with a proper user interface with elements like buttons and graphs instead of just using the command line, which would greatly improve useability and readability for the user.
#### **Reliability**: The program may have issues with the receiving data from the api, as the user may not be connected to the internet or the user inputs something the api cannot interperate.

### **Use Cases**

### **Main**
#### **Actor**: User
#### **Preconditions**: Internet access; Weather api availiable, and baseurl + api key
#### **1 - Search location**
- User inputs a location (e.g. Sydney), the sytem retrives the data from the api and outputs it as readable data to the user, the data is then saved in a file.
#### **2 - Show recent seaches**
- A list of recent weather searches is outputed to the user which displays the location, time and temperature at the time of the search.
#### **3 - Clear recent searches**
- Clears all of the users recent searches from the save file.
#### **4 - Help**
- Displays helpful information to the user on how to use the program.
#### **Postconditions**: Weather data retrieved, search data is saved/removed, or information is displayed successfully.

## **Design**

### **Gantt Chart**
![Gantt Chart](Images\GanttChart.png "Gantt Chart")

### **Structure Chart**

### **Algoriths**
#### **Flowchart of the whole program**
![Program Flowchart](Images\ProgramFlowchart.png "Program Flowchart")

#### **Main Routine**
#### Pseudocode
    BEGIN main()
        WHILE True
            option = ""
            INPUT option
            IF option is 1 THEN
                place = ""
                INPUT place
                Get_Weather(place) 
            ELIF option is 2 THEN
                Get_Local_Weather()
            ELIF option is 3 THEN
                Show_Recent_Searches()
            ELIF option is 4 THEN
                Help()
            ELIF option is 5 THEN
                option2 = ""
                INPUT option2
                IF option2 is 1 THEN
                    Set_Info()
                ELIF option2 is 2 THEN
                    Clear_Info()
                ELIF option2 is 3 THEN
                    Clear_Recent_Searches()
                ELIF option2 is 4 THEN
                    ip = Get_local_IP()

                    IF no ip THEN
                        DISPLAY "IP not found"
                    ELSE
                        DISPLAY ip
                ELIF option2 is 5 THEN
                    DISPLAY "Exiting program"
                    END PROGRAM
        ENDWHILE
    END main()

#### Flowchart
![Main Flowchart](Images\MainFlowchart.png "Main Flowchart")

#### **Get_Weather**
#### Pseudocode
    BEGIN Get_Weather(place)
        complete_url = BASE_URL + "/current.json?key=" + API_KEY + "&q=" + place

        response = ""

        TRY
            response = api request using complete_url
        EXCEPT
            RETURN None
        
        IF response status code is 200 THEN
            Save_Search(place, temperature from response, condition from response)

            RETURN response data
        ELSE
            Save_Search(place, "No data", "No data")

            RETURN None
    END Get_Weather

#### Flowchart
![Get_Weather Flowchart](Images\Get_WeatherFlowchart.png "Get_Weather Flowchart")

#### **Set_Info**
#### Pseudocode
    BEGIN Set_Info()
        data = global data
        saveData = global saveData

        TRY
            CREATE keys.json
            WRITE data into keys.json
            DISPLAY "keys.json created"
        EXCEPT
            DISPLAY "keys.json loaded"

        TRY
            CREATE saveData.json
            WRITE saveData into saveData.json
            DISPLAY "saveData.json created"
        EXCEPT
            DISPLAY "saveData.json loaded"
        
        READ from keys.json into data

        READ from saveData.json into saveData

        IF BASE_URL is empty THEN
            DISPLAY "No base url"
            url = ""
            INPUT url

            BASE_URL = url
        
        IF API_KEY is empty THEN
            DISPLAY "No Api key"
            key = ""
            INPUT key

            API_KEY = key

        WRITE data into keys.json

        WRITE saveData into saveData.json
    END Set_Info

### Flowchart
![Set_Info Flowchart](Images\Set_InfoFlowchart.png "Set_Info Flowchart")

### **Data Dictionary**
#### Everthing up to pollen in the table is from the weather api website (https://www.weatherapi.com/docs/#), Number of charactes is mostly not applicable as it can be different sizes.
| Variable Name       | Data Type| Format | Size         | Number of characters      | Purpose | Example |
|---------------------|----------|--------|--------------|---------------------------|---------|---------|
| last_updated        | string   | -      | -            | -                         | -       | -       |
| last_updated_epoch  | int      | -      | -            | -                         | -       | -       |
| temp_c              | decimal  | -      | -            | -                         | -       | -       |
| temp_f              | decimal  | -      | -            | -                         | -       | -       |
| feelslike_c         | decimal  | -      | -            | -                         | -       | -       |
| feelslike_f         | decimal  | -      | -            | -                         | -       | -       |
| windchill_c         | decimal  | -      | -            | -                         | -       | -       |
| windchill_f         | decimal  | -      | -            | -                         | -       | -       |
| heatindex_c         | decimal  | -      | -            | -                         | -       | -       |
| heatindex_f         | decimal  | -      | -            | -                         | -       | -       |
| dewpoint_c          | decimal  | -      | -            | -                         | -       | -       |
| dewpoint_f          | decimal  | -      | -            | -                         | -       | -       |
| condition:text      | string   | -      | -            | -                         | -       | -       |
| condition:icon      | string   | -      | -            | -                         | -       | -       |
| condition:code      | int      | -      | -            | -                         | -       | -       |
| wind_mph            | decimal  | -      | -            | -                         | -       | -       |
| wind_kph            | decimal  | -      | -            | -                         | -       | -       |
| wind_degree         | int      | -      | -            | -                         | -       | -       |
| wind_dir            | string   | -      | -            | -                         | -       | -       |
| pressure_mb         | decimal  | -      | -            | -                         | -       | -       |
| pressure_in         | decimal  | -      | -            | -                         | -       | -       |
| precip_mm           | decimal  | -      | -            | -                         | -       | -       |
| precip_in           | decimal  | -      | -            | -                         | -       | -       |
| humidity            | int      | -      | -            | -                         | -       | -       |
| cloud               | int      | -      | -            | -                         | -       | -       |
| is_day              | int      | -      | -            | -                         | -       | -       |
| uv                  | decimal  | -      | -            | -                         | -       | -       |
| gust_mph            | decimal  | -      | -            | -                         | -       | -       |
| gust_kph            | decimal  | -      | -            | -                         | -       | -       |
| short_rad           | decimal  | -      | -            | -                         | -       | -       |
| diff_rad            | decimal  | -      | -            | -                         | -       | -       |
| dni                 | decimal  | -      | -            | -                         | -       | -       |
| gti                 | decimal  | -      | -            | -                         | -       | -       |
| pollen              | element  | -      | -            | -                         | -       | -       |
| BASE_URL            | string   | URL    | a few bytes  | Not applicable     | Used in api requests as the base for the full url | "http://api.weatherapi.com/v1" |
| API_KEY             | string   | alphanumeric string | a few bytes | Not applicable | Used in api requests as they key | "fdjknsjk24ntnjkgjvfdj" |
| saveData | dictionary | Place, Time/date saved, Temperature, Condition | a few bytes but increases in size as more data is saved | Not applicable | Used to save the users recent searches | "search1": {"Place": "Sydney", "Time": "2025-03-13 09:39:00", "Temperature": 24.2, "Condition": "Overcast"} |
| place | string | Inputed string | a few bytes (depends on what the user inputs) | Not applicable | The place the user wants to view the data of | "Sydney" |
| option | int | Inputed integer | a few bytes | 1 charachter most of the time | The users choice | 2 |

## **Maintenence**

## **Final Evaluation**