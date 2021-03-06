
# serial-scrambled-json-to-xls

![Python Version](https://img.shields.io/badge/Python-3.8.1-yellow.svg)
![Pandas Version](https://img.shields.io/badge/Pandas-0.25.3-blue.svg)

This project was created because of a need for a tool to put json data readed on a microcontroller serial port and put it to a spreadsheet on a .xlsx for analysis.

### What does it do?  

This scripts take a raw json data with some fails, extracting useful data and putting it to a .xlsx for analysis, as you can see in the images below.

#### Input file and Output file 

<p align="center">
    <img src="https://github.com/LondriBaja/serial-scrambled-json-to-xls/blob/master/screenshots/input_file.PNG"
        height="500" style="margin-right: 500"> <img src="https://github.com/LondriBaja/serial-scrambled-json-to-xls/blob/master/screenshots/output_file.PNG"
        height="500">

#### After analysis you can have something like this
<p align="center">
    <img src="https://github.com/LondriBaja/serial-scrambled-json-to-xls/blob/master/screenshots/manipulated_file.PNG">
</p>


## Installation

1. Install `Python 3 and pip` on your computer.

2. run `pip install pandas` to install pandas library.

3. Clone/download this folder to your computer.

4. Put input files on `input_files/` folder.

5. Modify the `parser.py` script putting the name of your file on `file_path` variable and change the name of your json attributes in the code. (this step is better described on the comments of the code)

6. run `python parser.py` on main project folder.

7. Take output file on `output_files/` folder.


