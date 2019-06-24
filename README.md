# "Robo Advisor" Project


#Prerequisites

    + Anacoda 3.7
    + Python 3.7
    + Pip

# Installation


# Security
Your project repository should contain a file called ".gitignore" which prevents the ".env" file and its secret credentials from being tracked in version control.

The source code excludes secret API Key value

# Functionality Requirements

Information Input Requirements
The system should prompt the user to input one or more stock symbols (e.g. "MSFT", "AAPL", etc.).

Validation Requirements

# Calculations


# Information Output Requirements
Historical prices are written to a CSV file, file path indicated on output

All prices formatted to USD (doesn't apply to CSV file values)

Displays final recommendation, Yes/No

Justification / context = If the stock's latest closing price is less than 20% above its recent low, "Buy", else "Don't Buy".