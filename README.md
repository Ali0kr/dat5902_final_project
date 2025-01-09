# dat5902_final_project
The final project for module DAT5902 including code for the analysis and unit testing.
There are several files in this repository:
initial_explorations.py - this file has the data processing and analysis in it. it must be in the same directory as "testcenterdata.xlsx". This file also outputs three image files in the same directory it is saved in when ran: fig1.png, fig2.png and fig3.png.
testing.ipynb - this file has mostly the same code as initial_explorations.py but is in cells in a jupyter notebook for ease of editing and troubleshooting.
requirements.txt - this contains the required libraries to be installed by circleci when the unit tests are running
unit_tests.py - this file contains the unit tests and is linked to circleci to be ran every time a commit is made; it checks the "testcenterdata.xlsx" file size and that it exists and if not fails the unit tests. 
hidden folders: .circleci and .vscode are not to be deleted and are used as dependencies for vscode(which this repository was created in) and for the unit tests
testcenterdata.xlsx - the excel file containing the data required for this project - it is as was downloaded and can be sourced at https://www.gov.uk/government/statistical-data-sets/driving-test-and-theory-test-data-cars. the only sheet used is the 2023-2024 sheet
