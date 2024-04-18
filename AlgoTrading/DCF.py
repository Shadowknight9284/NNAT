from edgar import Company, TXTML

def get_cash_flow(company_name, cik, years_back=1):
    # Initialize a Company object with the provided company name and CIK
    company = Company(company_name, cik)

    # Get the list of available filings for the company
    filings = company.get_filings(
        filing_type="10-K",  # 10-K filings typically contain annual financial statements
        prior_to="2022-01-01",  # Limit filings to those before this date
        ownership="include",
    )

    # Filter the filings to get the most recent 'years_back' years of 10-K filings
    recent_filings = filings[:years_back]

    # Iterate through the recent filings to find the cash flow statement
    for filing in recent_filings:
        # Get the filing documents
        documents = filing.get_documents()

        # Iterate through the documents to find the cash flow statement
        for document in documents:
            if document.type == "10-K":
                # Get the cash flow statement from the filing
                cash_flow_statement = document.get_tables("CONSOLIDATED STATEMENTS OF CASH FLOWS")
                if cash_flow_statement:
                    # Return the first cash flow statement found
                    return cash_flow_statement[0]

    # If no cash flow statement is found, return None
    return None

# Example usage:
company_name = "Microsoft Corporation"
cik = "0000789019"  # CIK for Microsoft Corporation
years_back = 1  # Retrieve the cash flow statement from the most recent year
cash_flow_statement = get_cash_flow(company_name, cik, years_back)
if cash_flow_statement:
    print("Cash Flow Statement:")
    print(cash_flow_statement)
else:
    print("Cash flow statement not found for the specified company.")
