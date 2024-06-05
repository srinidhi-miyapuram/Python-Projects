
# GUI App - Current Temperature for Any Place with Python using FreeSimpleGUI

import requests
import FreeSimpleGUI as fg

api_key = "apiKey"

url = "url"

layout = [[fg.Text("Enter City Name :- "), fg.InputText(key= "-INPUT-")],[fg.Button("Exit"), fg.Button("Get Temperature")], [fg.Text(key= "-OUTPUT-")]]

window = fg.Window("Get Temperature", layout)

while True:
    event, values = window.read()
    if event == fg.WIN_CLOSED or event == "Exit":
        break 
    elif event == "Get Temperature":
        params = {'q': values['-INPUT-'], "appid": api_key, 'units': "metric"}
        response = requests.get(url, params).json()
        text = f"Current temperature in {values['-INPUT-']} is :- {response["main"]["temp"]}{chr(176)}C"
        window['-OUTPUT-'].update(text)
    

window.close()





