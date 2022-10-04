# Loan Qualifier Application
This application allows a user to enter basic financial data and compare it to a selected database of bank loans.  With simple, easy to answer questions about their debt, income, desired loan amount, and home value this loan can filter for loans they qualify for, and save them to a csv file. The user can elect the csv file name and use it for reference or conversion to another file type to share with others.
This application is used as a learning project in conjuction with the UC Berkeley FinTech Bootcamp.

##Technologies
This project leverages Python 3.7 with the following packages:
 fire - for the commmand line interface and entry-point
 questionary - for interactive user prompts
 pathlib - for file creation and destination
 csv - for file creation and saving data
 sys - for exiting the project upon completion

##Installation Guide
Before running the application first install the following dependencies.
pip install fire <code>
pip install questionary <code>

##Usage
Tuse use the loan qualifier application, clone the reposity and run the app.py
python app.py <code>

Upon launching the app.py app you will be asked to enter the location of the csv file with the compiled loan data you wish to use.  An example file called "daily_rate_sheet.csv" has been included in the project files, within the data folder.
<photo of image of folder structure with data folder and daily rate sheet circled>

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