
# serial-scrambled-json-to-xls

This project was created because the team need a tool to put json data readed on a microcontroller serial port and put it to a spreadsheet on a .xlsx for analysis.

### What does it do?  

This scripts take a raw json data with some fails, extracting useful data and putting it to a .xlsx for analysis, as you can see in the image below.

#### Input file  

![screenshot](https://github.com/LondriBaja/serial-scrambled-json-to-xls/blob/master/screenshots/input_file.PNG)

#### Output file  
![screenshot](https://github.com/LondriBaja/serial-scrambled-json-to-xls/blob/master/screenshots/output_file.PNG)

#### After analysis you can have something like this
![screenshot](https://github.com/LondriBaja/serial-scrambled-json-to-xls/blob/master/screenshots/manipulated_file.PNG)

## Installation

1. Install `Python 3 and pip` on your computer.

2. run `pip install pandas` to install pandas library.

3. Clone/download this folder to your computer.

4. Put input files on input_files/ folder.

5. Modify the `parser.py` script putting the name of your file on `file_path` variable and change the name of your json attributes in the code. (this step is better described on the comments of the code)

4. run `python parser.py` on main project folder.


