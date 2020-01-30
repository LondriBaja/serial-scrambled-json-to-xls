import json
import pandas as pd

path = 'raw_files/cvtcarroparado.txt'
file = open(path,'r')
raw_str = file.read()

current_json_str = ''
opened = False
json_array = []

for char in raw_str:
    if char == '{' and not opened:
        opened = True

    if char == '{' and opened:
        current_json_str = ''

    if char == '}' and opened:
        opened = False
        current_json_str += char
        try:
            current_json = json.loads(current_json_str)
            if (current_json['t']):
                json_array.append(current_json)
        except:
            pass  

    if char == '}' and not opened:
        current_json_str = ''
    
    if opened:
        if char == "'":
            char = '"'
        current_json_str += char

pd.read_json(json.dumps(json_array))#.to_excel("output.xlsx")