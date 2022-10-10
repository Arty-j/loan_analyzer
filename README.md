# **Loan Qualifier Application**
---

**This application allows a user to enter basic financial data and compare it to a user selected data file of bank loans.  With simple, easy to answer questions about debt, income, desired loan amount, and asset value, this application can filter for qualifing loans listed in the data file. The user then has the choice to save the qualifying loans to a csv file for future reference or sharing with others.**

*This application is used as a learning project in conjuction with the UC Berkeley FinTech Bootcamp.*

##**Technologies**
This project leverages Python 3.7 with the following packages:
 fire - for the commmand line interface and entry-point
 questionary - for interactive user prompts
 pathlib - for file creation and destination
 csv - for file creation and saving data
 sys - for exiting the project upon completion

##Installation Guide
Before running the application first install the following dependencies.
'''pip install fire
pip install questionary'''

The following libraries should also be imported for proper execution of this program
'''from pathlib import Path
import cvs
import sys'''

This program is modulized into the following folders:
[Main Program]('./app.py') 
[Data Files]('./data') - example data file of bank loans in csv format
[Qualifiers-executable function files]('./qualifiers') - filters, claculators, csv import files

##**Usage**
To use use the loan qualifier application, clone the reposity and run the app.py
'''python app.py'''

Upon launching the '''app.py''' app you will be asked to enter the location of the csv file from which you want to pull bank loan criteria data. An example file called "daily_rate_sheet.csv" has been included in the project files, within the data folder to use as an example of how the program runs.
![image of folder structure with data folder and daily rate sheet circled](/var/folders/4d/z57_76td03j5db8dyv4pwsvr0000gn/T/TemporaryItems/NSIRD_screencaptureui_2gK6kQ/Screen Shot 2022-10-09 at 3.31.02 PM.png)

The application with then prompt the user to enter financial data related to loan qualification.
<image of terminal output with data entered>

The app.py runs the find_qualifying_loans function and uses the user entered data in calculation functions to determine the user's debt to income ratio, and loan to value ratio. These calculaiton funcions are located in the calculations.py file, nested in the qualifier folder. 
<imate of terminal output>
<image of photo of image of folder structure with qualifier folder and calculations.py circled>>

The results of these calculations are used in the filtering funcions which are located in the filters folder, nested in the qualifier folder.
    bank_data_filtered = filter_max_loan_size(loan, bank_data) <code>
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)<code>
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)<code>
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)<code>
    The find_qualifying_loans function prints a statment to the user of how many loans from their data set they qualify for, and returns a list of qualifying loans.
<image of terminal output how many loans qualified for>

Finally, the user is asked if they would like to the qualifing loans list saved to a csv file with 'y/n' prompts.  If/else conditionals are used with user prompts to either save the file to the user's generated file name, or to exit the application. 

<image of code>
<image of terminal output>

##Contributors
This code was written collabratively by UC Berkeley FinTech staff and given some added functionality by myself, Jodi Artman.  artman.jodi@gmail.com

##License
This project is licensed under the terms of the UC Berkeley license.
