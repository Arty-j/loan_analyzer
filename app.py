# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    print(f"Found {len(bank_data_filtered)} qualifying loans")
    
    return bank_data_filtered



"""Prompts user 'y/n' to save qualifying loans to a csv file or exit the program.
   If answer == True, allows user to elect a file name for their csv file.
   If answer == False, thanks the user and exits the program
    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    If/else:
        statements will re-run the function if a negative response is not entered and verified"""
 
def save_qualifying_loans(qualifying_loans):
    if questionary.confirm("Would you like to save a your qualifying loans to a spreadsheet? (y/n)").ask():
        print ("Your qualifying loans list will be saved to a csv file saved as your last name and the date.")
        csv_file_name = questionary.text("Please type your last name, followed by the date, separated by a dash. Example: 'Smith-02-04-22'").ask()
        save_csv(qualifying_loans, csv_file_name)
        print(f"Your qualifying loans are listed in a cvs file called '{csv_file_name}'.csv")
    else:
        verify = questionary.text("To verify, please enter 'n' once again if you DO NOT wish to save your qualifying loans list.").ask()
        if verify == "n":
            print("Thank you for using the bank loan qualifier app. This app will now exit.")
            sys.exit()
        else:
            save_qualifying_loans(qualifying_loans)    
def save_csv(qualifying_loans, csv_file_name):
    """Saves the qualifying loans to a CSV file, with the file name elected by the user.
    Args:
        qualifying_loans (list of lists): The qualifying bank loans
        csv_file_name (var): the user elected file name
    """
    csv_file_name = csv_file_name + ".csv"
    csvpath = Path(csv_file_name)
    with open(csvpath,'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            for row in qualifying_loans:
                csvwriter.writerow(row)

    



def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )
    
    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)
